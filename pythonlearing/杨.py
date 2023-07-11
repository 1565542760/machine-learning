import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
x1_axis_data = [1, 2, 3, 4, 5,6,7,8,9,10,11,12]
y1_axis_data = [265.4,271.5,284.6,291.3,254.8,275.9,281.7,268.6,264.1,273.2,270.8,260.5]
x2_axis_data = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]
y2_axis_data = [235.9,215.4,215.8,224.7,228.3,231.1,253.0,221.7,218.8,233.8,230.9,240.7,256.9,260.7,224.4]
# plot中参数的含义分别是横轴值，纵轴值，线的形状，颜色，透明度,线的宽度和标签
plt.plot(x1_axis_data, y1_axis_data, 'ro-', color='#4169E1', alpha=0.8, linewidth=1, label='正常人')
plt.plot(x2_axis_data, y2_axis_data, 'ro-', color='#000000', alpha=0.8, linewidth=1, label='病毒性肝炎患者')
# 显示标签，如果不加这句，即使在plot中加了label='一些数字'的参数，最终还是不会显示标签
plt.legend(loc="upper right")
plt.xlabel('人')
plt.ylabel('铁蛋白的含量(mg/dl)')
plt.show()
