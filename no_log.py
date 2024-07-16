import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.colors as mcolors
import holoviews as hv
from holoviews import opts
from bokeh.io import output_notebook
data3 = pd.read_excel('//Users//wangxiaoran//Desktop//画图.xlsx', sheet_name='average_concentration')

# 重命名列以便于处理
data_avg_concentration = data3[['monitoring_province_y', 'adulterant_english_x', 'average_concentration(ug/kg)_log']]
data_avg_concentration.columns = ['MonitoringProvince', 'Adulterant', 'AverageConcentration']

# 取以2为底的log
data_avg_concentration['LogAverageConcentration'] = data_avg_concentration['AverageConcentration']

# 创建数据透视表
pivot_data_avg_concentration_log = data_avg_concentration.pivot_table(index='MonitoringProvince', columns='Adulterant', values='LogAverageConcentration', fill_value=0)

# 绘图
plt.figure(figsize=(14, 10))
sns.set(font_scale=1.2)  # 增大字体

cmap = "coolwarm"
# 增加颜色断点数量，并限制到0-1范围
boundaries = np.linspace(0, 1, 100)
norm = mcolors.BoundaryNorm(boundaries, ncolors=256)
#作图
heatmap = sns.heatmap(pivot_data_avg_concentration_log, annot=True, cmap=cmap, fmt=".2f", linewidths=.5, cbar_kws={'label': 'Log0.5(Average Concentration (ug/kg))'},annot_kws={"fontsize": 9})

# 调整x轴字体和旋转角度
plt.xticks(rotation=45, ha='right', fontsize=10)  # x轴标签字体小一些
plt.yticks(fontsize=10)  # y轴标签字体小一些

# 设置标题和标签
plt.title('The probabilities of contaminated', fontsize=20, weight='bold', ha='center',pad=20)
plt.xlabel('Antibiotic residue', fontsize=15)  # x轴标题大一些
plt.ylabel('Consumption region', fontsize=15)  # y轴标题大一些

# 设置图例标题字体大小
colorbar = heatmap.collections[0].colorbar
colorbar.ax.tick_params(labelsize=12)  # 调整图例标签字体大小
colorbar.set_label('Average Concentration (ug/kg)', fontsize=15)  # 图例标题字体大一些
# 调整布局
plt.tight_layout(pad=2)
plt.show()
