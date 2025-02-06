import pandas as pd
import numpy as np
from pyecharts.charts import Map
from pyecharts import options as opts

# 数据
data = {
    'Monitoring_province': ['Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong', 'Guangxi', 'Guizhou',
                            'Hainan', 'Hebei', 'Heilongjiang', 'Henan', 'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu',
                            'Jiangxi', 'Jilin', 'Liaoning', 'Ningxia', 'Qinghai', 'Shaanxi', 'Shandong', 'Shanghai',
                            'Shanxi', 'Sichuan', 'Tianjin', 'Xinjiang', 'Yunnan', 'Zhejiang'],
    'HI-improve': [0.234909078, 0.088363414, -0.0024677, -1.32718E-05, 1.61559E-06, 0.240590773, 0.002150823,
                   -0.00030688, -0.068470662, -0.020679594, 0.055557462, 0.033880438, -0.00561682, 2.24358E-08,
                   -4.21451E-05, 0.128740684, 0.128740684, 0.00488313, -0.000918038, 0.000168892, 0.001000218,
                   -6.16307E-07, 0.271631734, 0.032445814, 0.005212625, 0.233899162, -0.163017937, 1.30159E-05,
                   0.492160834, 0.078406098]
}

df = pd.DataFrame(data)

# 对每个数加上2，然后取以2为底的对数，再乘以10
df['Processed_HI-improve'] = np.log2(df['HI-improve'] + 2) * 100000000

# 英文省份名称到中文的映射
province_map = {
    'Anhui': '安徽省', 'Beijing': '北京市', 'Chongqing': '重庆市', 'Fujian': '福建省', 'Gansu': '甘肃省',
    'Guangdong': '广东省', 'Guangxi': '广西壮族自治区', 'Guizhou': '贵州省', 'Hainan': '海南省', 'Hebei': '河北省',
    'Heilongjiang': '黑龙江省', 'Henan': '河南省', 'Hubei': '湖北省', 'Hunan': '湖南省',
    'Inner Mongolia': '内蒙古自治区',
    'Jiangsu': '江苏省', 'Jiangxi': '江西省', 'Jilin': '吉林省', 'Liaoning': '辽宁省', 'Ningxia': '宁夏回族自治区',
    'Qinghai': '青海省', 'Shaanxi': '陕西省', 'Shandong': '山东省', 'Shanghai': '上海市', 'Shanxi': '山西省',
    'Sichuan': '四川省', 'Tianjin': '天津市', 'Xinjiang': '新疆维吾尔自治区', 'Yunnan': '云南省', 'Zhejiang': '浙江省',
    'Tibet': '西藏自治区', 'Hong Kong': '香港特别行政区', 'Macau': '澳门特别行政区', 'Taiwan': '台湾省'
}

# 将英文省份名称转换为中文
df['Monitoring_province'] = df['Monitoring_province'].map(province_map)

# 分别获取大于10和小于等于10的值
greater_than_10 = df[df['Processed_HI-improve'] > 100000000][['Monitoring_province', 'Processed_HI-improve']]
less_or_equal_10 = df[df['Processed_HI-improve'] <= 100000000][['Monitoring_province', 'Processed_HI-improve']]

# 将数据转换为 pyecharts 可以使用的格式
data_pair_greater = [list(z) for z in
                     zip(greater_than_10['Monitoring_province'], greater_than_10['Processed_HI-improve'])]
data_pair_less = [list(z) for z in
                  zip(less_or_equal_10['Monitoring_province'], less_or_equal_10['Processed_HI-improve'])]


def china_map(data_pair_greater, data_pair_less):
    map_chart = Map(init_opts=opts.InitOpts(theme='white', width='1280px', height='720px'))

    # 添加大于10的部分
    map_chart.add(
        series_name="HI-improve (Greater than 10)",
        data_pair=data_pair_greater,
        maptype="china",
        label_opts=opts.LabelOpts(is_show=True, position='inside'),
        is_map_symbol_show=False
    )

    # 添加小于等于10的部分
    map_chart.add(
        series_name="HI-improve (Less or equal 10)",
        data_pair=data_pair_less,
        maptype="china",
        label_opts=opts.LabelOpts(is_show=True, position='inside'),
        is_map_symbol_show=False
    )

    # 设置全局配置
    map_chart.set_global_opts(
        title_opts=opts.TitleOpts(
            title="HI-Improve Heat Map Of The Provinces",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(font_size=28, font_family="Microsoft YaHei")
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} : {c}"),
        visualmap_opts=[
            opts.VisualMapOpts(
                is_piecewise=False,
                min_=less_or_equal_10['Processed_HI-improve'].min(),
                max_=100000000,
                range_color=["#FFFFFF", "#0000FF"],  # 白色到蓝色
                pos_left='left',
                pos_top='middle',
                textstyle_opts=opts.TextStyleOpts(font_size=12, font_family="Microsoft YaHei")
            ),
            opts.VisualMapOpts(
                is_piecewise=False,
                min_=100000000.1,
                max_=greater_than_10['Processed_HI-improve'].max(),
                range_color=["#FFFFFF", "#FF0000"],  # 白色到红色
                pos_right='10%',
                pos_top='middle',
                textstyle_opts=opts.TextStyleOpts(font_size=12, font_family="Microsoft YaHei")
            )
        ]
    )

    map_chart.render('HI_improve_map_with_gradient.html')


if __name__ == '__main__':
    china_map(data_pair_greater, data_pair_less)