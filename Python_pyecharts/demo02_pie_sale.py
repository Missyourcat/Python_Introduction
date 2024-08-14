# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 下午12:08
# @Note     :   仅作学习使用--禁止传播，违者必究✅

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

#
# c = (
#     Pie()
#     .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])  # 添加数据
#     .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
#     .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))  # 表示标签显示形式
#     .render("pie_set_color.html")
# )
data_1 = [['衬衣', 138], ['毛衣', 40], ['领带', 74], ['裤子', 112], ['风衣', 147], ['高跟鞋', 104], ['袜子', 65]]
c = (
    Pie()
    .add("", data_1)  # 添加数据
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-商品销售"),toolbox_opts=opts.ToolboxOpts(is_show=True))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", font_size=20))  # 表示标签显示形式
    .render("pie_set_color.html")
)

