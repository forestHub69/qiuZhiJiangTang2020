import numpy as np
import matplotlib.pyplot as plt
import math

# 定义函数
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2
y3=np.sin(x)

# plt.figure(num=1)
# plt.plot(x,y1)

# 申请图
plt.figure(num=3,figsize=(6,6))

# 画图
lOne,=plt.plot(x,y2,label='x^2',linestyle='-.')
lTwo,=plt.plot(x,y1,color='red',linewidth=3.0,label='2x+1')
# lThree,=plt.scatter(x,y3,color='purple',label='-x') #散点图返回值用什么接收？？,加不加逗号有什么区别？？
lThree=plt.scatter(x,y3,color='purple',label='-x') #散点图返回值用什么接收？？

# 图例
# plt.legend(handles=[lOne,],labels=['x*x','what??'],loc='best')
plt.legend(handles=[lOne,lTwo,lThree],loc='best')

# 范围
plt.xlim((-1,2))
plt.ylim((-2,3))

# 坐标轴标注
plt.xlabel('x轴')
plt.ylabel('y轴')

# 这是啥？？似乎是改变了刻度？？和xscale区别？？
newTicks=np.linspace(-1,2,5) #???
print(newTicks)
plt.xticks(newTicks)
plt.yticks([-2,-1.8,-1,1.22,3],
           [r'$\ \alpha$',r'$\ \beta$',r'$\ \gamma$',r'$\ \delta$',r'$\ \epsilon$'])

# 边框颜色；默认坐标轴；边框位置？？
ax=plt.gca() # gca=get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

# 标点
x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)

# 注释，法一
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',
             xytext=(+30,-30),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',
                                         connectionstyle='arc3,rad=.2'))

# 注释，法二
plt.text(-3.7,3,r'$a\ nice\ plot.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})

# 坐标轴标注属性
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='green',edgecolor='None',
                        alpha=0.3))

plt.show()

# end of part one




