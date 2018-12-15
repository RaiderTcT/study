from smtplib import SMTP

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
