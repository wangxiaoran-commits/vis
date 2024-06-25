import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# data1=pd.read_excel('//Users//wangxiaoran//Desktop//画图.xlsx', sheet_name=0)
# print(data1)

data2=pd.read_excel('//Users//wangxiaoran//Desktop//画图.xlsx', sheet_name=1)
data2.columns = ['MonitoringProvince', 'HIforMfromP', 'ProductionProvince']
# 数据透视表
pivot_data2 = data2.pivot_table(index='MonitoringProvince', columns='ProductionProvince', values='HIforMfromP', fill_value=0)
pivot_data2 = pivot_data2.reset_index()
#将数据转换为长格式，使其适合使用seaborn进行可视化
melted_data = pivot_data2.melt(id_vars='MonitoringProvince', var_name='ProductionProvince', value_name='HIforMfromP')
plt.figure(figsize=(16, 12))
#设置调色板
sns.set_palette("Paired")  # Set the color palette to 'Paired'
# hue='ProductionProvince'：使用生产省份来区分不同的颜色堆叠部分。
# dodge=False：不分开不同生产省份的条形，使其堆叠在一起
sns.barplot(data=melted_data, y='MonitoringProvince', x='HIforMfromP', hue='ProductionProvince', dodge=False)
plt.title('Stacked Bar Plot of Food Safety Values by Monitoring and Production Provinces')
plt.xlabel('Hazard Index')
plt.ylabel('Consumption Regions')
# bbox_to_anchor参数用于控制图例的位置。它定义了图例框相对于指定位置的锚点。参数 (1.05, 1) 表示图例框的右上角（即锚点）将被放置在绘图区域的右上角之外，并且稍微偏右。
# 1.05 表示图例框的锚点在绘图区域的右边缘之外一点，即 x 轴方向的偏移量为 1.05 倍的绘图区域宽度。
# 1 表示图例框的锚点在绘图区域的上边缘，即 y 轴方向的偏移量为 1 倍的绘图区域高度。
#
plt.legend(title='Production Regions', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

