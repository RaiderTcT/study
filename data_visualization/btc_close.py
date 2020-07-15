# import requests
#
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)
# with open('btc_close_2017_request.json', 'w') as f:
#     f.write(req.text)
# file_requests = req.json

import json
import pygal
import math
from itertools import groupby


def draw_line(x_data, y_data, title, y_name):
    # 日期和收盘价列表打包成[（时间1，价格1）, （时间1，价格2）....(时间2,价格1)]的列表,排序后按日期分组
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda a: a[0]):
        # 取收盘价[]
        y_list = [v for a, v in y]
        # [[1月，价格],[2月,价格],...]
        xy_map.append([x, sum(y_list)/len(y_list)])
    # [[x1,y1],[x2, y2]...]->[x1,y1] [x2, y2]...[xn,yn]->(x1,x2...xn)(y1,y2,...yn)->[x1,x2,...xn] [y1,y2,...yn]
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_name, y_mean)
#    line_chart.render_to_file(title+".svg")
    return line_chart


filename = "btc_close_2017_request.json"
dates, months, weeks, weekdays, closes = [], [], [], [], []
with open(filename) as f:
    btc_data = json.load(f)
for btc_dict in btc_data:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    dates.append(date)
    weeks.append(week)
    months.append(month)
    weekdays.append(weekday)
    closes.append(close)

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价格(￥)'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
line_chart.title = '半对数变化'
close_log = [math.log10(x) for x in closes]
line_chart.add(' log', close_log)
# line_chart.add('收盘价', closes)
line_chart.render_to_file('收盘价格.svg')

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价格(￥)'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
line_chart.add('收盘价', closes)

line_chart.render_to_file('收盘.svg')


month_date = dates.index('2017-12-01')
print(months)
line_chart_month = draw_line(months[:month_date], closes[:month_date], '月收盘价格', '月均收盘价')


idx_week = dates.index('2017-12-11')
weeks_new = [v.zfill(2) for v in weeks]

line_chart_week = draw_line(weeks_new[1:idx_week], closes[1:idx_week], '各周收盘价', '周收盘价')

idx_weekday = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(day)+1 for day in weekdays]
print(weekdays_int)
line_chart_wd = draw_line(weekdays_int[1:idx_weekday], closes[1:idx_weekday], '星期收盘均值', '收盘价')
line_chart_wd.x_labels = ['周1', '周2', '周3', '周4', '周5', '周6', '周日']
line_chart_wd.render_to_file("星期收盘均值.svg")

with open('收盘价Dashboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard<meta charset ="utf-8"></title></head><body>')
    for svg in ['收盘价格.svg', '收盘.svg', '月收盘价格.svg', '各周收盘价.svg', '星期收盘均值.svg']:
        html_file.write('<object type = "image/svg+xml" data = "{0}" height = 500></object>\n'.format(svg))
    html_file.write('</body></html>')
