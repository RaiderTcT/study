from smtplib import SMTP
from email.message import EmailMessage
from mimetypes import guess_type
import os

# SMTP协议默认端口是25
#  smtp = SMTP('smtp.exmail.qq.com', 25)
with SMTP('smtp.exmail.qq.com', 25) as smtp:
    # 为服务器通信设置调试级别
    # 1 获取与服务器交互的所有信息
    # 2 将信息带上时间戳
    smtp.set_debuglevel(2)
    smtp.login('jianliang.wu@holley.cn', 'Holley0719')
    smtp.sendmail('jianliang.wu@holley.cn', ['2276777056@qq.com', '991861319@qq.com'],
                  '1234567时光一去不复返'.encode('utf-8'))
    # 邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA
    # 而是包含在发给MTA的文本中的
# smtp.quit()

EMAIL_CONTENT = ''
EMAIL_SETTING = {}


def send_report(file):
    msg = EmailMessage()
    msg['from'] = EMAIL_SETTING['username']
    msg['to'] = EMAIL_SETTING['receiver']
    msg['cc'] = EMAIL_SETTING['cc']
    msg['subject'] = 'xxxx'
    msg.set_boundary(EMAIL_CONTENT, 'html', 'utf-8')
    ctype, encoding = guess_type(file)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/')
    with open(file, 'rb') as f:
        msg.add_attachement(
            f.read(),
            maintype=maintype,
            subtype=subtype,
            filename=os.path.basename(file)
        )
    with SMTP('') as smtp_client:
        import smtplib
        try:
            smtp_client.login(
                EMAIL_SETTING['username'], EMAIL_SETTING['password'])
            smtp_client.send_message(
                EMAIL_SETTING['sender'],
                EMAIL_SETTING['receiver']+EMAIL_SETTING['cc'],
                msg.as_string())
        except smtplib.SMTPAuthenticationError:
            print('用户账号或密码出错')