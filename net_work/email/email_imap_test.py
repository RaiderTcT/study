from imaplib import IMAP4_SSL

user = '2276777056@qq.com'
pass_ = 'kcpklenqgqxjebfh'
with IMAP4_SSL('imap.qq.com', 993) as s:
    s.login(user, pass_)
    # 返回邮件数
    rsp, msgs = s.select('INBOX', True)
    print(msgs)
    rsp, data  = s.fetch(msgs[0], '(BODY)')
    print(data[0])
    s.close
# s.logout()