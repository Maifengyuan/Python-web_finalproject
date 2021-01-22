from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

ducity = ['上海','东莞','北京','南京','天津','广州','无锡','杭州','武汉','深圳','珠海','苏州','贵阳','重庆','长沙']
dunum = [39, 1, 67, 6, 2, 5, 1, 20, 1, 13, 1, 3, 1, 1, 1]

def mapcity():
    c = (
        Map()
        .add(
            "",
            [list(z) for z in zip(ducity,dunum)],
            "china-cities",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2018dujioashou"),
            visualmap_opts=opts.VisualMapOpts(),
        )
        
       # .render_notebook()
     # .render("2018独角兽企业城市分布数量.html")#生成HTML文件，可在浏览器打开
    )
    return c.render()
