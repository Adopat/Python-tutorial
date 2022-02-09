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


sql2 = """
select
	zs.id as 需求id,
	concat('http://172.18.20.83/zentaopdm/www/story-view-',zs.id,'.html') as 需求链接,
	zs.title as 需求名称,
	zs.pri as 优先级,
	b.tasknum as 任务数,
	zs.source as 需求来源,
	zl.value as 需求来源组别,
	zs.sourceNote as 提出者,
	zs.stage as 所处阶段id,
	zl2.value as 所处阶段名称,
	zs.status as 当前状态id,
	(case
	zs.status
	when 'draft' then '未开始'
	when 'active' then '进行中'
	when 'closed' then '已关闭'
	when 'changed' then '已变更'
	else ''
	end) as 当前状态,
	zs.openedBy as 创建者工号,
	zu3.realname as 创建者,
	zs.openedDate as 创建日期,
	zs.assignedTo as 指派者id,
	if(zs.assignedTo ='closed','closed',zu.realname) as 指派者,
	zs.storyBP as 需求BP工号,
	zu4.realname as 需求BP,
	zd.name as 需求BP组别,
	zs.branch as 分支,
	zb.name as 分支名称, 
	zs.closedBy as 由谁关闭工号,
	zu2.realname as 由谁关闭,
	zs.closedDate as 关闭日期,
	zs.product as 产品名称id,
	zp.name as 所属产品,
	zp.line as 产品线id,
	(case 
	zp.line 
	when 160 then 'IT智慧平台'
	when 161 then '集团ETE流程'
	end
	)as 产品线,
	zp3.project as 所属项目id,
	zp4.name as 所属项目,
	zs.plan as 所属计划,
	zp2.title as 计划标题,
	zs.module as 所属模块id,
	zm.name as 所属模块,
	zs.deadline as 期望完成,
	zs.playtime as 计划交付,
	// 增加 设计截止 开发截止 系统测试截止 BP测试截止 用户测试截止 20210603 zhongrf
	zs.sysdeadline as 设计截止,
	zs.devdeadline as 开发截止,
	zs.testdeadline as 系统测试截止,
	zs.bpdeadline as BP测试截止,
	zs.userdeadline as 用户测试截止,
	zs.storyClass as 需求类别id,
	zs.closedReason as 关闭原因id,
	zl_closedReason.value as 关闭原因,
	(case
	zs.storyClass
	when 'createFea' then '新增功能'
	when 'PerformanceUpg' then '性能提升'
	when 'FeaturesOpt' then '功能优化'
	when 'questionDeal' then '问题处理'
	else zs.storyClass
	end) as 需求类别
from
	zt_story zs
left join zt_branch zb on zb.id = zs.branch 
left join zt_product zp on zp.id = zs.product
left join zt_productplan zp2 on zp2.id = zs.plan
left join zt_module zm  on zm.id = zs.module 
left join zt_user zu on zu.account = zs.assignedTo 
left join zt_user zu2 on zu2.account = zs.closedBy 
left join zt_user zu3 on zu3.account = zs.openedBy 
left join zt_user zu4 on zu4.account = zs.storyBP   /*需求BP*/
left join zt_dept zd on zu4.dept = zd.id            /*需求BP组别*/
left join zt_lang zl on zl.`key` = zs.source and zl.module = 'story' and zl.`section` = 'sourceList' 
left join zt_lang zl2 on zl2.`key` = zs.stage and zl2.module = 'story' and zl2.`section` = 'stageList' 
left join zt_projectstory zp3 on zp3.story = zs.id and zp3.product = zs.product 
left join zt_project zp4 on zp4.id = zp3.project and zp4.deleted = '0'
left join (select zt.story as story,count(zt.id) as tasknum from zt_task zt 
where zt.deleted ='0' and zt.story<>0 group by zt.story) b on b.story=zs.id
left join zt_lang zl_closedReason on zl_closedReason.key=zs.closedReason  and zl_closedReason.module ='story' and zl_closedReason.`section` ='reasonList' /*关闭原因*/
where zs.deleted ='0' order by zs.id;


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
