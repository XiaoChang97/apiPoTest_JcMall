import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail:

    # 初始化服务器信息
    def __init__(self,mail_host, mail_user, mail_pass, sender, receives):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender
        self.receivers = receives

    # 以文本的形式发送邮件
    def make_email_by_text(self,context, subject, from_address, to_address):
        message = MIMEText(context, 'plain', 'UTF-8')
        message['Subject'] = subject  # 邮件标题
        message['From'] = Header(from_address, "utf-8")  # 邮件主体中发送者名称
        message['To'] = Header(to_address, "utf-8")  # 邮件主体中接收者名称
        self.send_email(message)

    # 以文本和附件的形式发送邮件
    def make_email_by_att(self,content,file_path,subject, from_address, to_address):
        message = MIMEMultipart()
        message['Subject'] = subject  # 邮件标题
        message['From'] = Header(from_address, "utf-8")  # 邮件主体中发送者名称
        message['To'] = Header(to_address, "utf-8")  # 邮件主体中接收者名称
        # with open(file_path,'r',encoding='utf-8') as f:
        #     file_text = f.read()
        body = MIMEText(content,'plain','utf-8')
        message.attach(body)
        # att = MIMEText(file_text,'base64','utf-8')
        att = MIMEApplication(open(file_path, 'rb').read())
        att.add_header('Content-Disposition','attachment',filename='allure测试报告.zip')
        # att["Content-Type"] = 'application/octet-stream'
        # att["Content-Disposition"] = 'attachment; filename="allure测试报告.txt"'
        message.attach(att)
        self.send_email(message)

    # 登录并进行发送
    def send_email(self,message):

        # 进行登录发送
        try:
            smtpobj = smtplib.SMTP_SSL(self.mail_host)
            smtpobj.ehlo(self.mail_host)
            # smtpobj.connect(self.mail_host,25)
            smtpobj.login(self.mail_user,self.mail_pass)
            smtpobj.sendmail(self.sender,self.receivers,message.as_string())
            smtpobj.quit()
            print('success')
        except Exception as e:
            print(f'error: {e}')
            raise e



if __name__ == '__main__':
    mail_host = "smtp.qq.com"
    mail_user = "372109913"
    mail_pass = "fyrwqnzwikyicbdg"
    sender = '372109913@qq.com'
    receivers = ['smilepassed@163.com']

    send = SendEmail(mail_host, mail_user, mail_pass, sender, receivers)

    content = "测试已经执行完毕，这是接口自动化测试报告，详情请看附件allure报告，不需要回复。"
    file_path = '../report/index.html'
    Subject = '一封来自测试的信'  # 邮件标题
    From = "Jie的QQ邮箱" # 邮件主体中发送者名称
    To = "Jie的邮箱" # 邮件主体中接收者名称
    send_att = send.make_email_by_att(content,file_path,Subject,From,To)