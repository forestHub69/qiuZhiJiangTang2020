'''
# 分支，if
print('---------分支，if-------------')
line=60
score=float(input('please input your score:'))
# print('please input your score:')
# score=int(input())
if 0<=score<line:
    print('failed')
elif line<=score<100:
    print('passed')
elif score==100:
    print('excellent')
    pass
else:
    print('wrong score')
    pass #空语句

print('down')

# 演练，猜拳小游戏
print('-------石头剪刀布---------')
import random
person=int(input('choose form\nstone(0);scissors(1);cloth(2)\n'))
computer=random.randint(0,2) #随机数
print('{}'.format(computer))
if person==computer:
    print('A tie.')
    pass
elif person==computer+1 or person==computer-2:
    print('You Lose!')
    pass
else:
    print('You Win!')
    pass
print('Game is over.')


# if-else嵌套
print('----------if-else嵌套----------')
credit=float(input('please input your credit:'))
if credit>150:
    averageGrade=float(input('please input your average grade:'))
    if averageGrade>85:
        print('Well done')
        pass
    else:
        print('Sorry that your grade is not good enough.')
        pass
    pass
else:
    print('please gain more credits.')
    pass
print("that's it.")

# 循环，while；for
print('--------Loop---------')
endRound=1
winTimes=0
loseTimes=0
while endRound<=5:
    person = int(input('choose form\nstone(0);scissors(1);cloth(2)\n'))
    computer = random.randint(0, 2)
    print('{}'.format(computer))
    if person==computer:
        print('A tie at round %d.'%endRound)
        pass
    elif person==computer+1 or person==computer-2:
        print('You Lose at round %d!'%endRound)
        loseTimes+=1
        pass
    else:
        print('You Win at round %d!'%endRound)
        winTimes+=1
        pass
    endRound+=1 #注意这句话的缩进位置！！！！！！！
    pass
if loseTimes>winTimes:
    print('you lose!!!')
    pass
elif loseTimes==winTimes:
    print('a tie!!!')
    pass
else:
    print('you win!!!')
    pass
print('Game is over.')
'''

'''
#思考1：写一个猜拳程序，猜n局，考虑所有提前获胜的情况！！！
print('---------思考1------------')
import random
endTimes=float(input('how many times do you want:'))
endRound=1.0
winTimes=0.0
loseTimes=0.0
evenTimes=0.0
print(type(evenTimes))
while endRound<=endTimes:
    person = int(input('choose form\nstone(0);scissors(1);cloth(2)\n'))
    computer = random.randint(0, 2)
    print('{}'.format(computer))
    if person==computer:
        print('A tie at round %d.'%endRound)
        evenTimes+=1
        pass
    elif person==computer+1 or person==computer-2:
        print('You Lose at round %d!'%endRound)
        loseTimes+=1
        pass
    else:
        print('You Win at round %d!'%endRound)
        winTimes+=1
        pass
    endRound+=1 #注意这句话的缩进位置！！！！！！！
    if endRound<=endTimes:
        if winTimes > (endTimes - evenTimes) / 2:
            print('you win already!!!')
            break
        elif loseTimes > (endTimes - evenTimes) / 2:
            print('you lose already!!!')
            break
        else:
            pass
        pass
    # 判断必胜或者必负，以提前结束
if loseTimes>winTimes:
    print('you lose!!!')
    pass
elif loseTimes==winTimes:
    print('a tie!!!')
    pass
else:
    print('you win!!!')
    pass
print('Game is over.')
'''


'''
#思考2：打印一个九九乘法表。
print('-----------思考2------------')
# 法一
x,y=1,1
while x<=9:
    while y<=9:
        print("%d*%d=%d\t" % (x, y, x * y), end='') #Python的print默认以\n结尾，会自动提行，加end=‘’以避免
        y = y + 1
        pass
    x=x+1
    y=x
    # list=[]
    # for i in range(2*x):
    #     list.append('\t')
    #     pass
    # b=''
    # for i in range(len(list)):
    #     b=b+list[i]
    # print(b)
    # 这一段有待研究
    pass
# 法二
row=1
while row<=9:
    col=1
    while col<=row:
        print('%d*%d=%2d\t'%(row,col,row*col),end='')
        col+=1
        pass
    print()
    row+=1
    pass
'''


'''
# 思考3：打印直角位于四角的四个直角三角形；打印直角位于上下左右的四个直角三角形。
# 等腰三角形
print('-----------思考3----------')
row=1
endRow=7
while row<=endRow:
    j=1
    while j<=endRow-row:
        print(' ',end='')
        j+=1
        pass
    k=1
    while k<=2*row-1:
        print('*',end='')
        k+=1
        pass
    print()
    row+=1
    pass
'''

'''
# for 循环,,for 临时变量 in 容器：
print('\n---------for---------')
# range 函数,可以生成一个数据集合列表，，range(起始,结束,步长) 步长不能为0
list=range(1,100) #左含右不含
for data in list:
    print(data,end=' ')
    pass
print()
# break可退出本层循环 continue跳过本次循环后面的语句，进入下一次循环
#break和continue只能用于循环中
print('\n--------break与continue----------')
sum=0
for item in range(0,50,2):
    if sum>100:
        print('循环结束')
        print('sum=%d'%sum)
        break
        pass
    else:
        print('这句执行几次呢？？')
        pass
    pass
    # break #注意break写到这里的后果
    sum+=item
    pass
for item in range(0,50):
    if item%2==0:
        sum = sum + item
        pass
    else:
        continue
        print('这句会执行吗？？')
    if sum>100:
        print('end')
        print(sum)
        break
        print('这句会执行吗？？')
        pass
    pass
# while 使用：适用于对未知的循环次数
# for 使用：适用于已知次数和对象的遍历
# 作业1：for嵌套打印乘法表
'''

'''
# for---else以及while---else结构
print('\n---------"for/while---else结构"-------------')
account='Ghost'
pwd='123456'
for i in range(3):
    tryAcc=input('请输入用户名:')
    tryPwd=input('请输入密码:')
    if tryPwd==pwd and tryAcc==account:
        print('登录成功')
        break
        pass
    else:
        print('你还有{}次机会'.format(2-i))
        pass
    pass
else: #当前面没有break，或者break没有执行时，else一定会执行，多用于查找（不确定能否找到）
    print('账户已被锁定')
'''

# 作业，见PPT

# from matplotlib import pyplot as plt
# from astropy.io import fits, ascii
# plt.plot(np.sin(np.arange(0,10,0.01)));
# import matplotlib.pyplot


