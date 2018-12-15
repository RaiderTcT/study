from xml.parsers.expat import ParserCreate
import requests


class Weather(object):
    def __init__(self, city=None, forecast=None):
        self.city = city
        self.forecast = []

    def __str__(self):
        return self.city

    def __repr__(self):
        return self.forecast


class MySaxHandler(object):
    def __init__(self, xml_raw):
        self.weather = Weather()
        self.parser = ParserCreate()
        self.parser.StartElementHandler = self.start_element
        self.parser.EndElementHandler = self.end_element
        self.parser.CharacterDataHandler = self.char_data
        self.parser.Parse(xml_raw)
        del(xml_raw)
    # 遇到XML开始标签时调用，name是标签的名字，attrs是标签

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.weather.city = attrs['city']
        if name == 'yweather:forecast':
            l = {'dates': attrs['date'],
                 'high': attrs['high'], 'low': attrs['low']}
            self.weather.forecast.append(l)
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    # 遇到XML结束标签时调用，name是标签的名字

    def end_element(self, name):
        pass
        # print('sax:end_element: %s' % name)
    # This will be called for normal character data,
    # CDATA marked content, and ignorable whitespace

    def char_data(self, text):
        pass
        # print('sax:char_data: %s' % text)


class DefaultSaxHandler(object):
    # 遇到XML开始标签时调用，name是标签的名字，attrs是标签
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    # 遇到XML结束标签时调用，name是标签的名字

    def end_element(self, name):
        print('sax:end_element: %s' % name)
    # This will be called for normal character data,
    # CDATA marked content, and ignorable whitespace

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

if __name__ == "__main__":
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)

    URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.\
    forecast%20where%20woeid%20%3D%202151330&format=xml'
#  
    r = requests.get(URL, timeout=8)
    print(r.content)
    my_parser = MySaxHandler(r.content.decode('utf-8'))
    print(my_parser.weather)
    for forecast in my_parser.weather.forecast:
        print(forecast)
