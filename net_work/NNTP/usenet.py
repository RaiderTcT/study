# NNTP: 网络新闻传输协议
import socket
import nntplib

HOST = 'news.gmane.org'
GRNM = 'gmane.comp.python.committers'
USER = ''
PASS = ''


def main():
    with nntplib.NNTP(HOST) as n:
        """
        - resp: server response if successful
        - count: number of articles
        - first: first article number
        - last: last article number
        - name: the group name
        """
        print(n.getwelcome())
        resp, count, first, last, name = n.group(GRNM)
        print(f'Group {name} has {count} articles, range from {first} to {last}')
        rng = f'{first}-{last}'
        """Process an XHDR command (optional server extension).  Arguments:
        - hdr: the header type (e.g. 'subject')
        - str: an article nr, a message id, or a range nr1-nr2
        - file: Filename string or file object to store the resu
        lt in
        Returns:
        - resp: server response if successful
        - list: list of (id, text) strings
        text is the text of the requested header for that article.
        """
        # 获取了从 first 到 last 的 from，subject， date字段信息
        # 返回 （响应，lsit）
        # list： [(序号1， 内容1)，。。。 ]
        rsp, frm = n.xhdr('from', rng)
        rsp, sub = n.xhdr('subject', rng)
        rsp, date = n.xhdr('date', rng)
        print(f'*** Find last article {last}: \nFrom: {frm[-1][1]}\nSubject: {sub[-1][1]}\nDate: {date[-1][1]}')
        rsp, (num, nid, data) = n.body(last)
        displayFirst20lines(data)


def displayFirst20lines(data):
    print('***First 20 lines of this article***')
    lines = (line.rstrip() for line in data)
    count = 0
    for line in lines:
        if line:
            count += 1
            if count > 20:
                break
            print(line)


if __name__ == "__main__":
    main()
