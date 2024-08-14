# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 下午2:18
# @Note     :   仅作学习使用--禁止传播，违者必究✅
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline

# from pyecharts.faker import Faker
#
# x = Faker.choose()
# tl = Timeline()
# for i in range(2015, 2020):
#     bar = (
#         Bar()
#         .add_xaxis(x)
#         .add_yaxis("商家A", Faker.values())
#         .add_yaxis("商家B", Faker.values())
#         .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
#     )
#     tl.add(bar, "{}年".format(i))
# tl.render("timeline_bar.html")
"""准备数据"""
# 创建多少个Bar
with open('数据/分省年度数据.csv', 'r', encoding='gbk') as f:
    data_lines = f.readlines()
for _ in range(3):
    data_lines.pop(0)
for _ in range(2):
    data_lines.pop(-1)

years = data_lines.pop(0).replace('\n', "").split(',')
years.pop(0)
# print(years)

# 设计数据 把数据放到一个字典对象中
data_dict = {}
# print(data_lines)
for data_line in data_lines:
    data_line_list = data_line.replace("\n", "").split(",")
    # print(data_line_list)
    index = 0
    for year in years:
        index += 1
        try:
            data_dict[year].append([data_line_list[0], float(data_line_list[index])])
        except Exception as e:
            # 如果出现了异常，说明是第一次添加数据
            data_dict[year] = []
            data_dict[year].append([data_line_list[0], float(data_line_list[index])])
print(data_dict)
"""创建Timeline对象"""
timeline = Timeline()
years.reverse()
"""创建个Bar对象 并加入到Timeline对象 进行配置"""
for year in years:
    data_dict[year].sort(key=lambda ele: ele[1], reverse=True)
    rank_12_city_data = data_dict[year][0:12]
    # print(year, rank_12_city_data)

    # 定义bar的x轴
    x_data = []
    # 定义bar的y轴
    y_data = []
    for city in rank_12_city_data:
        x_data.append(city[0])
        y_data.append(city[1])
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("人口(万)", y_data)
    bar.reversal_axis()
    bar.set_global_opts(title_opts=opts.TitleOpts(title=f"{year} 年中国省市人口前12排名情况"))

    timeline.add(bar, str(year))
timeline.add_schema(
    play_interval=500,
    is_auto_play=True
)
"""生成文件"""
timeline.render("demo05_timeline_bar_city_population.html")
