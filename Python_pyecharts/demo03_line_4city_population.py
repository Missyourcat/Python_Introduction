# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 下午12:33
# @Note     :   仅作学习使用--禁止传播，违者必究✅

import pyecharts.options as opts
from pyecharts.charts import Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=line-simple

目前无法实现的功能:

暂无
"""

# x_data = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# y_data = [820, 932, 901, 934, 1290, 1330, 1320]
#
#
# (
#     Line()
#     .set_global_opts(
#         tooltip_opts=opts.TooltipOpts(is_show=False),
#         xaxis_opts=opts.AxisOpts(type_="category"),
#         yaxis_opts=opts.AxisOpts(
#             type_="value",
#             axistick_opts=opts.AxisTickOpts(is_show=True),
#             splitline_opts=opts.SplitLineOpts(is_show=True),
#         ),
#     )
#     .add_xaxis(xaxis_data=x_data)
#     .add_yaxis(
#         series_name="",
#         y_axis=y_data,
#         symbol="emptyCircle",
#         is_symbol_show=True,
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#     .render("basic_line_chart.html")
# )

# 创建line对象 折线图对象
line = Line()
# 给x轴添加数据

# 代开文件
f = open('数据/分省年度数据.csv', 'r', encoding='GBK')
# for line in f:
#     print(line, end='')
# f.close()

# 读取所有行数据
line_datas = f.readlines()
print(line_datas)
f.close()

# 删除前面三个行（元素）
for _ in range(3):
    line_datas.pop(0)
print(line_datas)

x_data_year = line_datas.pop(0).replace('\n', '').split(',')
x_data_year.pop(0)
x_data_year.reverse()
print(x_data_year)

# 给Y轴添加数据
# 创建四个列表存放4个省
y_data_bj = []
y_data_tj = []
y_data_hb = []
y_data_sx = []
# 遍历line_datas
for line_data in line_datas:
    line_data = line_data.replace('\n', '').split(',')
    if line_data[0] == '北京市':
        line_data.pop(0)
        line_data.reverse()
        y_data_bj = line_data
    elif line_data[0] == '天津市':
        line_data.pop(0)
        line_data.reverse()
        y_data_tj = line_data
    elif line_data[0] == '河北省':
        line_data.pop(0)
        line_data.reverse()
        y_data_hb = line_data
    elif line_data[0] == '山西省':
        line_data.pop(0)
        line_data.reverse()
        y_data_sx = line_data

line.add_xaxis(x_data_year)
line.add_yaxis('北京市历年人口', y_data_bj, label_opts=opts.LabelOpts(is_show=False))
line.add_yaxis('天津市历年人口', y_data_tj, label_opts=opts.LabelOpts(is_show=False))
line.add_yaxis('河北省历年人口', y_data_hb, label_opts=opts.LabelOpts(is_show=False))
line.add_yaxis('山西省历年人口', y_data_sx, label_opts=opts.LabelOpts(is_show=False))

# 设置全局配置项
line.set_global_opts(title_opts=opts.TitleOpts(title="2004-2024人口折线图", pos_left='center',pos_bottom="1%"))
line.render("demo03_line_4city_population.html")
