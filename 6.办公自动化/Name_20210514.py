# 使用Python 提取SQL语句中的表名
import ply.lex as lex, re


def extract_table_name_from_sql(sql_str):

    # remove the /* */ comments
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)

    # remove whole line -- and # comments
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]

    # remove trailing -- and # comments
    q = " ".join([re.split("--|#", line)[0] for line in lines])

    # split on blanks, parens and semicolons
    tokens = re.split(r"[\s)(;]+", q)

    # scan the tokens. if we see a FROM or JOIN, we set the get_next
    # flag, and grab the next one (unless it's SELECT).

    result = []
    get_next = False
    for token in tokens:
        if get_next:
            if token.lower() not in ["", "select"]:
                result.append(token)
            get_next = False
        get_next = token.lower() in ["from", "join"]

    return result

sql2="""
进行中任务:
load
*
;
select
	zt.id as 任务id,
	concat('http://172.18.20.83/zentaopdm/www/task-view-',zt.id,'.html') as 单据链接,
	zt.project as 所属项目id,
	zp.name as 所属项目,
	zt.module as 所属模块id,
	zm.name as 所属模块,
	if(zm.parent=0,null,zm.parent) as 所属上一级模块id,
	zm1.name as 所属上一级模块,
	zt.story as 相关需求id,
	zs.branch as 分支id,  /*通过需求获取分支ID*/
	zb2.name as 分支,
	zs.sourceNote as 需求提出者,
    zs.playtime as 需求截止时间,
	zt.name as 任务名称,
	zt.type as 任务类型id,
	(case zl.value
	when '支持&amp;结项' then '支持&结项'
	when '培训&amp;上线' then '培训&上线'
	else zl.value
	end
	)as 任务类型,
	zt.pri as 优先级,
	zt.estimate as 最初预计,
	zt.consumed as 总计消耗,
	zt.estStarted as 预计开始,
    zt.realStarted as 实际开始,
	zt.deadline as 截止日期,
	zt.status as 任务状态id,
	(case
		zt.status
		when 'done' then '已完成'
		when 'wait' then '未开始'
		when 'closed' then '已关闭'
		when 'cancel' then '已取消'
		when 'doing' then '进行中'
        when 'pause' then '已暂停'
		else '其他' end) as 任务状态,
	zt.openedBy as 由谁创建id,
	zu1.realname as 由谁创建,
	zt.openedDate as 创建日期,
	zt.assignedTo as 指派给,
	if( zt.assignedTo ='closed','closed',zu.realname) as 指派者姓名,
	zu.dept as 指派者部门,
	zu.team as 指派者团队,
	zu.role as 指派者职位id,
	zl2.value as 指派者职位,
	zd.name as 部门名称,
	if(isnull(zd.name)=0,(case
		zd.name
		when 'ITAD' then 'ITAD'
		when 'ITPS' then 'ITPS'
		when 'ITBP' then 'ITBP'
		when '业务顾问' then '业务顾问'
		when '开发顾问' then '开发顾问'
		when '测试顾问' then '测试顾问'
		 when 'EPA' then 'EPA'
        when 'ITMO' then 'ITMO'
        when 'NVT-IT' then 'NVT-IT'
        when 'PTL-IT' then 'PTL-IT'
        when '设计开发组' then '设计开发组'// update by ZhongRF 20210529
        when '基础架构组' then '基础架构组'
        when '业务实施组' then '业务实施组'
        when '运维服务组' then '运维服务组'    
		else '业务部门' end),zd.name) as 所属组别,	
	zt.assignedDate as 指派日期,
	zt.finishedBy as 由谁完成id,
	zu2.realname as 由谁完成,
	zt.finishedDate as 实际完成,
	zt.canceledBy as 由谁取消,
	zt.canceledDate as 取消时间,
	zt.closedBy as 由谁关闭id,
	zu3.realname as 由谁关闭,
	zt.closedDate as 关闭时间,
	zt.closedReason as 关闭原因,
	b.BUG数量 as BUG数量,
	b.severity as BUG级别,
	zp1.id as 产品id,
	zp1.name as 产品名称,
	(case zp1.line
	when 160 then 'IT智慧平台'
	when 161 then '集团ETE流程' 
	end) as 产品线,
	zt.develuser as 开发人员id,
	zu4.realname as 开发人员,
	zt.develscore as 开发质量分	
from
	zt_task zt
left join zt_project zp on
	zt.project = zp.id
	and ZP.DELETED = '0'
left join zt_module zm on
	zt.module = zm.id
	and zm.deleted = '0'
	and zm.`type` ="story"
left join zt_product zp1 on
     zm.root = zp1.id
     and zp1.deleted = '0'
left join zt_user zu1
  on zt.openedBy = zu1.account 
left join zt_lang zl on
	zt.type = zl.key
left join zt_user zu on
	zt.assignedTo = zu.account
	and zu.deleted = '0'
left join zt_lang zl2 on 
    zu.`role` =zl2.`key` 
    and zl2.module ='user'
    and zl2.`section` ='roleList'
left join zt_dept zd on
	zu.dept = zd.id
left join zt_story zs on    /*关联story*/
	zt.story = zs.id
	and zs.deleted = '0'
left join zt_branch zb2 on zs.branch = zb2.id /*取分支名称*/
left join zt_module zm1 on
	zm.parent = zm1.id
	and zm1.deleted = '0'
left join zt_user zu2
  on zt.finishedBy = zu2.account 
left join zt_user zu3
  on zt.closedBy = zu3.account 
left join zt_user zu4               /*开发人员*/
on zt.develuser=zu4.account
 left join 
(select zb.task,zb.severity,count(zb.id)as BUG数量 from zt_bug zb where task<>0 and deleted ='0' group by zb.task,zb.severity) b
on zt.id=b.task
where 
	 zt.deleted = '0';


left Join
select 
ztm.id as 所属模块id,
//ztm.name as 模块名称,
ztm.oneno as 一级模块id,
zm1.name as 一级模块,
ztm.twono as 二级模块id,
zm2.name as 二级模块,
ztm.threeno as 三级模块id,
zm3.name as 三级模块,
ztm.fourno as 四级级模块id,
zm4.name as 四级模块,
ztm.fiveno as 五级模块id,
zm5.name as 五级模块
from (
select 
zm.id,
zm.name,
substring_index(substring_index(path,',',2),',',-1) as oneno,
substring_index(substring_index(path,',',3),',',-1) as twono,
substring_index(substring_index(path,',',4),',',-1) as threeno,
substring_index(substring_index(path,',',5),',',-1) as fourno,
substring_index(substring_index(path,',',6),',',-1) as fiveno 
from 
zt_module zm 
where zm.type='story' and zm.deleted ='0') as ztm
left join zt_module zm1
on ztm.oneno = zm1.id
left join zt_module zm2
on ztm.twono = zm2.id
left join zt_module zm3
on ztm.threeno = zm3.id
left join zt_module zm4
on ztm.fourno = zm4.id
left join zt_module zm5
on ztm.fiveno = zm5.id;
"""
print(extract_table_name_from_sql(sql2))


