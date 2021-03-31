import numpy as np
import matplotlib.pyplot as plt
import math

# 散点图and气泡图

# n=1024
# X=np.random.normal(0,1,n)
# Y=np.random.normal(0,1,n)
# T=np.arctan2(Y,X) #颜色
#
# plt.scatter(X,Y,s=75,c=T,alpha=0.5)
#
# plt.xlim((-1.5,1.5))
# plt.ylim((-1.5,1.5))
# plt.xticks(())
# plt.yticks(())

# plt.show()



# 条形图and柱状图

# n=12
# X=np.arange(n)
# Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
# Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
#
# plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
# plt.bar(X,-Y2,facecolor='lightgreen',edgecolor='gray')
#
# for x,y in zip(X,Y1):
#     plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')
#     #ha=horizontal alignment 对齐方式
#     pass
# for x,y in zip(X,Y2):
#     plt.text(x+0.05,-y-0.05,'-%.2f'%y,ha='center',va='top')
#
# plt.xlim(-.5,n)
# plt.xticks(())
# plt.ylim(-1.25,1.25)
# plt.yticks(())
#
# plt.show()


# 等高线

def f(x,y):
    # the height function
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
# t=np.ndarray() ?????






