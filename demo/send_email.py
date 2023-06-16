import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
def send_email():
    # 配置发件人和收件人
    sender_email = 'jjlee7447@gmail.com'
    receiver_email = 'jjlee7447@qq.com'

    # 创建 MIME 邮件对象
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Python 邮件测试'

    # 添加邮件正文
    body = '这是一封使用 Python 发送的邮件。'
    message.attach(MIMEText(body, 'plain'))

    # 配置 Gmail SMTP 服务器
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # 登录到 Gmail SMTP 服务器
    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
    smtp_obj.starttls()
    smtp_obj.login(sender_email, 'ljj030322@@')

    # 发送邮件
    smtp_obj.sendmail(sender_email, receiver_email, message.as_string())
    smtp_obj.quit()

    print('邮件发送成功！')


def send_request():
    url = 'http://www.google.com'
    response = requests.get(url)
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    send_request()