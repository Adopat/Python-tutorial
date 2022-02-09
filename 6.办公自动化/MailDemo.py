# 使用Python+ schedule 实现自动发送outlook 邮件
# 安装方法 使用 pip install pypiwin32
import win32com.client
import schedule
import time


# 自动群发邮件
def send_group_mail():
    outlook = win32com.client.Dispatch("Outlook.Application")
    # 创建一个邮件对象
    mail = outlook.CreateItem(0)
    # 对邮件的各个属性进行赋值
    mail.To = "test@qq.com"  # 收件邮箱列表,如多人用;隔开
    mail.CC = 'test@qq.com'  # 抄送邮箱列表
    # mail.BCC = "test@outlook.com" # 密抄邮箱列表，谨慎使用
    mail.Subject = "邮件测试"
    mail.BodyFormat = 2  # 2: Html format
    # mail.Body = "邮件正文"  # 如不需要HTML格式使用
    mail.HTMLBody = '这是一封测试邮件'
    # mail.Attachments.Add("附件绝对路径")
    # 添加多个附件
    # mail.Attachments.Add("附件1绝对路径")
    # mail.Attachments.Add("附件2绝对路径")...
    # 邮件发送
    mail.Send()


# if __name__ == '__main__':
#     send_group_mail()
# schedule.every(10).minutes.do(send_group_mail)       #部署每10分钟执行一次job()函数的任务
# schedule.every().hour.do(send_group_mail)            #部署每×小时执行一次job()函数的任务
# schedule.every().day.at("10:30").do(send_group_mail) #部署在每天的10:30执行job()函数的任务
# schedule.every().monday.do(send_group_mail)          #部署每个星期一执行job()函数的任务
# schedule.every().wednesday.at("13:15").do(send_group_mail)#部署每周三的13：15执行函数的任务
schedule.every(100).seconds.do(send_group_mail)  # 每2s执行一次job()函数

while True:
    schedule.run_pending()
    time.sleep(1)
