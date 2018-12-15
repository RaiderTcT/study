from html.parser import HTMLParser
from html.entities import name2codepoint
import requests


class MyHTMLParser(HTMLParser):
    # 处理标记的开始
    # 例如<div id="main">，参数tag指的是div，
    # attrs指的是一个（name,Value)的列表
    # 一个tag <A HREF="https://www.cwi.nl/"> 的处理
    # handle_starttag('a', [('href', 'https://www.cwi.nl/')])
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.nameflag = False
        self.locationflag = False
        self.datetimeflag = False
        self.name = []
        self.location = []
        self.datetime = [] 

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for k, v in attrs:
                if k == 'href' and ('python-events/6' in v) or ('python-events/7' in v) :
                    self.nameflag = True
        if tag == 'time':
            for k, v in attrs:
                if k == 'datetime':
                    self.datetimeflag = True
        if tag == 'span':
            for k, v in attrs:
                if k == 'class' and v == 'event-location':
                    self.locationflag = True

            # my_event = Event()
            # print('<%s>' % tag)
    # 处理结束标记</html>

    def handle_endtag(self, tag):
        if tag == 'a':
            if self.nameflag:
                self.nameflag = False
        if tag == 'time':
            if self.datetimeflag:
                self.datetimeflag = False
        if tag == 'span':
            if self.locationflag:
                self.locationflag = False
        
        # print('</%s>' % tag)
    # 处理 XHTML-style 的空tag <img ... />

    def handle_startendtag(self, tag, attrs):
        pass
        # print('<%s/>' % tag)
    # 处理任意数据，如text nodes and the content of
    # <script>...</script>和<style>...</style>

    def handle_data(self, data):
        if self.nameflag:
            self.name.append(data)
        if self.datetimeflag:
            self.datetime.append(data)
        if self.locationflag:
            self.location.append(data)
        # return data
        # print(data)
    # 处理注释
    #<!--[if IE 9]>IE9-specific content<![endif]-->
    #

    def handle_comment(self, data):
        pass
        #print('<!--', data, '-->')
    #处理 &name

    def handle_entityref(self, name):
        pass
        # print('&%s;' % name)
    # 处理16进制和10进制数字字符 &#NNN，&#xNNN

    def handle_charref(self, name):
        pass

        # print('&#%s;' % name)
if __name__ == "__main__":

    parser = MyHTMLParser()
    parser.feed('''<html>
    <head></head>
    <body>
    <!-- test html parser -->
        <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
    </body></html>''')
    url = 'https://www.python.org/events/python-events/'
    r = requests.get(url, timeout=4)
    my_html = MyHTMLParser()
    my_html.feed(r.content.decode('utf-8'))
    print(my_html.name)
    print(my_html.location)
    print(my_html.datetime)
