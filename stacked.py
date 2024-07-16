import pandas as pd
import matplotlib.pyplot as plt


import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
df = pd.read_excel(r'/Users/wangxiaoran/Desktop/工作簿1 12.18.04.xlsx')

# 打印列名以确认它们
print(df.columns)

# 创建透视表并计算总的 hazard index 值
pivot_df = df.pivot_table(index='Monitoring_province_y', columns='ProductionProvince_x', values='HIforMfromP', aggfunc='sum')

# 添加一列用于总的 hazard index 值的排序
pivot_df['Total_HI'] = pivot_df.sum(axis=1)

# 按总的 hazard index 值排序
pivot_df = pivot_df.sort_values('Total_HI', ascending=False)

# 绘制堆叠柱状图
fig, ax = plt.subplots(figsize=(14, 10))
bar_width = 0.9  # 设置柱子的宽度
bar_spacing = 0.9 # 设置柱子之间的间隔

# 绘制堆叠柱状图
pivot_df.drop(columns='Total_HI').plot(kind='barh', stacked=True, ax=ax, width=bar_width)
# 设置标题和轴标签
plt.title('The probability of contaminated aquatic products associated with antibiotics in each consumption region\n along with the respective contribution proportions from various production regions.', fontsize=16,pad=20)
ax.set_xlabel('Hazard Index', fontsize=14,labelpad=15)
ax.set_ylabel('Consumption region', fontsize=14,labelpad=15)


# 设置x轴和y轴标签的字体大小
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

# 在每个柱子旁边标注总的 hazard index 值
for i in range(len(pivot_df)):
    ax.text(pivot_df['Total_HI'].iloc[i], i, f'{pivot_df["Total_HI"].iloc[i]:.5f}', va='center')

# 去掉柱状图的外框线
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 调整图例
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False, fontsize=8, ncol=1, columnspacing=0.5, handletextpad=0.5)
#调整图表位置
plt.subplots_adjust(top=0.9, bottom=0.15)
# 显示图表
plt.show()
