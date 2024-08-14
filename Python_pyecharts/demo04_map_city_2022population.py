# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 下午1:42
# @Note     :   仅作学习使用--禁止传播，违者必究✅

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

# c = (
#     Map()
#     .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
#     .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
#     .render("map_base.html")
# )
"""准备数据"""
with open('数据/分省年度数据.csv', 'r', encoding='gbk') as f:
    data_lines = f.readlines()
for _ in range(4):
    data_lines.pop(0)
# print(data_lines)
map_data_list = []
for data_line in data_lines:
    data_line_list = data_line.split(',')
    try:
        map_data_list.append([data_line_list[0], data_line_list[1]])
    except Exception as e:
        continue
print(map_data_list)

"""创建Map对象"""
map = Map()
"""添加数据被配置"""
map.add('2024年各省市的人口分布情况', map_data_list, 'china')
# 全局设置
map.set_global_opts(
    title_opts=opts.TitleOpts(title='2024年各省的人口分布情况'),
    # 视觉效果配置项
    visualmap_opts=opts.VisualMapOpts(
        min_=100,
        max_=15000,
        pos_left='10%',
        pos_bottom='30%'
    )
)
# 系列配置-标签字体大小
map.set_series_opts(label_opts=opts.LabelOpts(font_size=8))
"""生成文件"""
map.render('2024各省市人口分布情况.html')
