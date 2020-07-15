from poplib import POP3_SSL

user = '2276777056@qq.com'
# 使用授权码第三方登录
pass_ = 'kcpklenqgqxjebfh'
# 连接到POP3服务器
p = POP3_SSL('pop.qq.com', 995)
p.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(p.getwelcome().decode('utf-8'))
# 身份验证
p.user(user)
p.pass_(pass_)
# stat()返回邮件数量和占用空间:
print('Messages count: %s. Size: %s' % p.stat())

# 返回 (response, ['mesg_num octets', ...], octets)
resp, mails, octets = p.list()
print(mails)

index = len(mails)
# 检索邮件
# (response, ['line', ...], octets)
resp, lines, octets = p.retr(index)

for eachline in lines:
    print(eachline)

p.quit()