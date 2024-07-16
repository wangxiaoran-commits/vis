import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import pandas as pd
import holoviews as hv
from holoviews import opts
from bokeh.io import output_notebook

# 加载数据
# import pandas as pd
# import plotly.graph_objects as go
# import numpy as np
# import networkx as nx
#
# file_path = '/Users/wangxiaoran/Desktop/副本20240625 画图需求.xlsx'
# data_chord = pd.read_excel(file_path, sheet_name='HI-current-withoutunknown')
#
# # Ensure correct columns are used
# data_chord.columns = ['MonitoringProvince', 'HIforMfromP', 'ProductionProvince']
#
# # List of unique provinces (both Monitoring and Production)
# provinces = list(set(data_chord['MonitoringProvince']).union(set(data_chord['ProductionProvince'])))
#
# # Create a mapping from province to index
# province_to_index = {province: i for i, province in enumerate(provinces)}
#
# # Create the adjacency matrix
# matrix = np.zeros((len(provinces), len(provinces)))
#
# # Populate the matrix with HIforMfromP values
# for _, row in data_chord.iterrows():
#     source = province_to_index[row['ProductionProvince']]
#     target = province_to_index[row['MonitoringProvince']]
#     matrix[source, target] = row['HIforMfromP']
#
# # Create a NetworkX graph from the matrix
# G = nx.from_numpy_array(matrix)
#
# # Get positions for the nodes in circular layout
# pos = nx.circular_layout(G)
# #
# # # Create a Plotly figure
# # fig = go.Figure()
# #
# # # Add edges
# # for i, j in G.edges():
# #     fig.add_trace(go.Scatter(
# #         x=[pos[i][0], pos[j][0], None],
# #         y=[pos[i][1], pos[j][1], None],
#         mode='lines',
#         line=dict(width=matrix[i, j]*10, color='blue'),
#         opacity=0.5
#     ))
#
# # Add nodes
# for node in G.nodes():
#     fig.add_trace(go.Scatter(
#         x=[pos[node][0]],
#         y=[pos[node][1]],
#         mode='markers+text',
#         text=[provinces[node]],
#         marker=dict(size=10, color='red'),
#         textposition='bottom center'
#     ))
#
# # Customize layout
# fig.update_layout(
#     title="Chord Diagram of Production and Monitoring Provinces",
#     showlegend=False,
#     xaxis=dict(showgrid=False, zeroline=False),
#     yaxis=dict(showgrid=False, zeroline=False)
# )
#
# # Show the plot
# fig.show()
# show
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # Load the Excel file
# file_path = '/Users/wangxiaoran/Desktop/副本20240625 画图需求.xlsx'
# data2 = pd.read_excel(file_path, sheet_name=1)
#
# # Renaming columns for easier handling
# data2.columns = ['MonitoringProvince', 'HIforMfromP', 'ProductionProvince']
#
# # Creating the pivot table to prepare the data for plotting
# pivot_data2 = data2.pivot_table(index='MonitoringProvince', columns='ProductionProvince', values='HIforMfromP', fill_value=0)
#
# # Calculate the total Hazard Index for each Monitoring Province for sorting
# pivot_data2['TotalHI'] = pivot_data2.sum(axis=1)
#
# # Sort the pivot table by the Total Hazard Index
# pivot_data2 = pivot_data2.sort_values('TotalHI', ascending=False)
#
# # Drop the TotalHI column after sorting
# pivot_data2 = pivot_data2.drop(columns=['TotalHI'])
#
# # Reset the index to use in Seaborn
# pivot_data2 = pivot_data2.reset_index()
#
# # Melt the dataframe for use in Seaborn
# melted_data = pivot_data2.melt(id_vars='MonitoringProvince', var_name='ProductionProvince', value_name='HIforMfromP')
#
# # Plotting the stacked bar plot
# plt.figure(figsize=(16, 12))
# sns.set_palette("Paired")
#
# # Create a horizontal barplot
# barplot = sns.barplot(data=melted_data, y='MonitoringProvince', x='HIforMfromP', hue='ProductionProvince', dodge=False)
#
# # Customizing the plot
# plt.title('The probability of contaminated aquatic products associated with antibiotics in each consumption region, along with the respective contribution proportions from various production regions.',fontsize=10)
# plt.xlabel('Hazard Index')
# plt.ylabel('Consumption region')
#
# # Remove the barplot frame
# barplot.spines['top'].set_visible(False)
# barplot.spines['right'].set_visible(False)
# barplot.spines['left'].set_visible(False)
# barplot.spines['bottom'].set_visible(False)
#
# # Remove the legend frame
# legend = plt.legend(title='Production Province', bbox_to_anchor=(1.05, 1), loc='upper left')
# legend.get_frame().set_linewidth(0.0)
#
# # Show the plot
# plt.tight_layout()
# plt.show()




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

# 加载数据
data3 = pd.read_excel('//Users//wangxiaoran//Desktop//画图.xlsx', sheet_name='average_concentration')

# 重命名列以便于处理
data_avg_concentration = data3[['monitoring_province_y', 'adulterant_english_x', 'average_concentration(ug/kg)_log']]
data_avg_concentration.columns = ['MonitoringProvince', 'Adulterant', 'AverageConcentration']

# 取以2为底的log
data_avg_concentration['LogAverageConcentration'] = np.log(data_avg_concentration['AverageConcentration'] + 1) / np.log(1.1)

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
colorbar.set_label('Log1.2(Average Concentration (ug/kg))', fontsize=15)  # 图例标题字体大一些
# 调整布局
plt.tight_layout(pad=2)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 加载数据
# df = pd.read_excel('/Users/wangxiaoran/Desktop/工作簿1.xlsx')
#
# # 打印列名以确认它们
# print(df.columns)
#
# # 创建透视表并计算总的 hazard index 值
# pivot_df = df.pivot_table(index='Monitoring_province_y', columns='ProductionProvince_x', values='HIforMfromP', aggfunc='sum')
#
# # 添加一列用于总的 hazard index 值的排序
# pivot_df['Total_HI'] = pivot_df.sum(axis=1)
#
# # 按总的 hazard index 值排序
# pivot_df = pivot_df.sort_values('Total_HI', ascending=False)
#
# # 绘制堆叠柱状图
# fig, ax = plt.subplots(figsize=(14, 10))
# bar_width = 0.9  # 设置柱子的宽度
# bar_spacing = 0.9 # 设置柱子之间的间隔
#
# # 绘制堆叠柱状图
# pivot_df.drop(columns='Total_HI').plot(kind='barh', stacked=True, ax=ax, width=bar_width)
# # 设置标题和轴标签
# plt.title('The probability of contaminated aquatic products associated with antibiotics in each consumption region\n along with the respective contribution proportions from various production regions.', fontsize=16,pad=20)
# ax.set_xlabel('Hazard Index', fontsize=14,labelpad=15)
# ax.set_ylabel('Consumption region', fontsize=14,labelpad=15)
#
#
# # 设置x轴和y轴标签的字体大小
# ax.tick_params(axis='x', labelsize=10)
# ax.tick_params(axis='y', labelsize=10)
#
# # 在每个柱子旁边标注总的 hazard index 值
# for i in range(len(pivot_df)):
#     ax.text(pivot_df['Total_HI'].iloc[i], i, f'{pivot_df["Total_HI"].iloc[i]:.5f}', va='center')
#
# # 去掉柱状图的外框线
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
#
# # 调整图例
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False, fontsize=8, ncol=1, columnspacing=0.5, handletextpad=0.5)
# #调整图表位置
# plt.subplots_adjust(top=0.9, bottom=0.15)
# # 显示图表
# plt.show()
