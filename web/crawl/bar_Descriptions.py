import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS("#5F9EA0", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Project'
chart.x_labels = ['http', 'django', 'flask']

polt_dict = [
    {'value': 1777, 'label': 'Descriptions of http'},  # 值，描述
    {'value': 2222, 'label': 'Descriptions of django'},
    {'value': 1888, 'label': 'Descriptions of flask'}
]
chart.add(" ", polt_dict)
chart.render_to_file('Python Project.svg')
