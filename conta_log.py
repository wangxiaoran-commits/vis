import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

# 加载数据
data= pd.read_excel(r'/Users/wangxiaoran/Desktop/20240528 画图需求.xlsx', sheet_name='conta_proportion')

# 重命名列以便于处理
data_avg_concentration = data[['adulterant_english', 'monitoring_province', 'ProbofAntiForM']]
data_avg_concentration.columns = ['adulterant', 'monitoring_province', 'ProbofAntiForM']

# 取以2为底的log
data_avg_concentration['LOG_ProbofAntiForM'] = np.log(data_avg_concentration['ProbofAntiForM'] + 1) / np.log(2)

# 创建数据透视表
pivot_data_avg_concentration_log = data_avg_concentration.pivot_table(index='monitoring_province', columns='adulterant', values='LOG_ProbofAntiForM', fill_value=0)

# 绘图
plt.figure(figsize=(14, 10))
sns.set(font_scale=1.2)  # 增大字体

cmap = "coolwarm"
# 增加颜色断点数量，并限制到0-1范围
boundaries = np.linspace(0, 1, 100)
norm = mcolors.BoundaryNorm(boundaries, ncolors=256)
#作图
heatmap = sns.heatmap(pivot_data_avg_concentration_log, annot=True, cmap=cmap, fmt=".2f", linewidths=.5, cbar_kws={'label': 'Log2(LOG_ProbofAntiForM)'},annot_kws={"fontsize": 9})

# 调整x轴字体和旋转角度
plt.xticks(rotation=45, ha='right', fontsize=10)  # x轴标签字体小一些
plt.yticks(fontsize=10)  # y轴标签字体小一些

# 设置标题和标签
plt.title('Conta_proportion', fontsize=20, weight='bold', ha='center',pad=20)
plt.xlabel('adulterant', fontsize=15)  # x轴标题大一些
plt.ylabel('monitoring_province', fontsize=15)  # y轴标题大一些

# 设置图例标题字体大小
colorbar = heatmap.collections[0].colorbar
colorbar.ax.tick_params(labelsize=12)  # 调整图例标签字体大小
colorbar.set_label('Log2(LOG_ProbofAntiForM)', fontsize=15)  # 图例标题字体大一些
# 调整布局
plt.tight_layout(pad=2)
plt.show()