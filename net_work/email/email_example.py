from smtplib import SMTP_SSL
from poplib import POP3_SSL
from imaplib import IMAP4_SSL
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from secret_qq import *
from email.encoders import encode_base64 as base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from io import BytesIO
# MIME: mail interchange message extension
# 邮件互换消息扩展


def make_mpa_msg():
    # 可以组合html和Plain
    email = MIMEMultipart('alternative')
    text = MIMEText('你好', 'plain', 'utf-8')
    html = MIMEText('<html><body><h1>你好哈</h1></body></html>', 'html', 'utf-8')
    # 添加要发送的数据
    email.attach(text)
    email.attach(html)
    return email


def make_img_msg(file):
    with open(file, 'rb') as f:
        data = f.read()
    email = MIMEImage(data)
    # 添加Content-Dispositio头
    email.add_header('Content-Disposition', 'attachment',
                     filename='%s' % file)
    return email


# 发送附件
def make_file_msg(file):
    with open(file, 'rb') as f:
        data = f.read()
    email = MIMEBase('image', 'jpg')
    email.add_header('Content-Disposition', 'attachment', filename='test.png')
    email.add_header('Content-ID', '<0>')
    email.add_header('X-Attachment-Id', '0')
    # 设置要发送的消息
    email.set_payload(data)
    # base64编码，可打印字符串
    base64(email)
    return email


def send_msg(from_, pass_, to, msg, host, port):
    with SMTP_SSL(host, port) as s:
        s.set_debuglevel(1)
        s.login(from_, pass_)
        s.sendmail(from_, to, msg)


To = 'jianliangwu1171@gmail.com'


def mail_parser():
    with IMAP4_SSL('imap.qq.com', 993) as s:
        s.login(MAILBOX, PASSWD)
        # 选择邮箱， 返回邮件数、
        s.select('INBOX', True)
        tpe, msgnums = s.search(None, 'SINCE 25-Aug-2018', 'BEFORE 27-Aug-2018')
        print(msgnums)
        msg_list = [bytes(i) for i in msgnums[0].split()]
        print(msg_list)
        for msg in msg_list:
            rsp, data = s.fetch(msg, '(RFC822)')
            msg = Parser().parsestr(data[0][1].decode('utf-8'))
            print_info(msg)
        s.close()


def decode_str(s):
    # 返回（decode_string, charset）
    # Decode a message header value without converting the character se
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    # subject 解码 
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                # print(type(charset), charset)
                content = content.decode(charset.split(';')[0])
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


if __name__ == "__main__":
    # print('Send multipart alternative msg')
    # msg = make_mpa_msg()
    # msg['From'] = secret_qq.MAILBOX
    # msg['To'] = 'jianliangwu1171@gmail.com'
    # msg['Subject'] = 'multipart alternative test'
    # send_msg(secrect_qq.MAILBOX, secrect_qq.PASSWD, ['jianliangwu1171@gmail.com'], msg.as_string(),
    #          'smtp.qq.com', 465)
    # print('Send image msg')
    # msg = make_img_msg('timg.jpg')
    # msg['From'] = secret_qq.MAILBOX
    # msg['To'] = 'jianliangwu1171@gmail.com'
    # msg['Subject'] = 'image test'
    # send_msg(secrect_qq.MAILBOX, secrect_qq.PASSWD, ['jianliangwu1171@gmail.com'], msg.as_string(),
    #          'smtp.qq.com', 465)

    # print('Attached files test')
    # msg = make_file_msg('nan.jpg')
    # msg['From'] = secret_qq.MAILBOX
    # msg['To'] = To
    # msg['Subject'] = 'send attached files test'
    # send_msg(secrect_qq.MAILBOX, secrect_qq.PASSWD, To, msg.as_string(), 'smtp.qq.com', 465)
    print('Get message from gmail')
    mail_parser()
