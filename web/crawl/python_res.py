import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code", r.status_code)

response_dict = r.json()
print("Total repositories：", response_dict['total_count'])

repo_dicts = response_dict['items']
print('Repositories Return:', len(repo_dicts))

repo_dict1 = repo_dicts[0]
print('\nKey:', len(repo_dict1))
# for key in sorted(repo_dict1.keys()):
#     print(key)
# print('\nSelected information about each repositories ')
# for repo_dict in repo_dicts:
#     print("\nName:", repo_dict['name'])  # 项目名称
#     print("Owner:", repo_dict['owner']['login'])  # 所有者
#     print("Starts:", repo_dict['stargazers_count'])  # 星级
#     print("Repositories:", repo_dict['html_url'])  # url
#     print('Description:', repo_dict['description'])  # 描述

name, plot_dicts = [], []
for repo_dict in repo_dicts:
    name.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
# 可视化处理
my_style = LS('#FF00FF', base_style=LCS)
# 斜45度，
my_config = pygal.Config()
my_config.x_label_rotation = 45  # 45°倾斜
my_config.show_legend = False  # 移除图例
my_config.show_y_guides = False  # 不显示的水平线
my_config.title_font_size = 24  # 字号
my_config.label_font_size = 15
my_config.label_major_font_size = 18
my_config.truncate_label = 15   # 项目名称缩短显示15
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects in Github'
chart.x_labels = name
chart.add('', plot_dicts)
chart.render_to_file('python_repositories.svg')
