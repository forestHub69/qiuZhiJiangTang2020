# 注释
# 单行#balabalabala
# 多行'''balabalabala'''
# 快捷注释，Ctrl+/


# 数据类型
print('----------数据类型-----------')
a=10
b=str(a)
c=len(b)
d=type(c)
e=() #元组类型
f=[] #列表类型
g={} #字典类型
h=True #布尔类型
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(a,b,c,d,e,f,g,h)
print('\n')

# 算数运算符
print('----------------算数运算--------------')
x,y=7,3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y) #7^3，，C中使用math.h中的pow(x,y)函数
print(x//y) #取整数部分
print(x%y)  #求余数
print()

 # 比较运算符,结果是bool
 #  == >= <= > < !=
print('------------比较运算------------')
print(x>y)
print()

# 逻辑运算符
# and or not   & | !  注意区别
print('---------------逻辑运算-------------')
print(x>y and x>y+1)
print(x>y & x>y+1)
print((x>y) & (x>y+1))
print(x>y or x>y+1)
print(x>y | x>y+1)
print((x>y) | (x>y+1))
#print(!x) 不能这么写
print(x)
print(not x)
print(x>y)
print(not x>y)
# 优先级: () ---> not ---> and ---> or
print( not 4>3 or 5>4)
print( not(4>3 or 5>4))
print(3>2 and 4>3 or 5>4 and 5>6)
print(3>2 and not 4>3 or 5>4 and 5>6)
print('\n')

# 赋值运算符,类似于C
# =  +=  -=  /=  *=  **=  //=  %=
print('----------------赋值运算---------------')
print('略\n')

# 输出
# 字符串格式化,使用%作占位符，后跟变量类型
# 常用符号 %c字符；%s，str()字符串；%ior%d有符号十进制整数；%u无符号十进制整数；%o八进制整数；%x十六进制整数；%eor%E索引；
# %f浮点数；%gor%G，%f和%eor%E的简写
# 也可使用.format()函数
print('--------------输出-------------------')
name_='李华'
class_='一班'
age_=18
print('我的名字是%s,来自%s,今年%d岁。'%(name_,class_,age_))
print('%s'%name_)
print('%d'%age_)# 只输出一个不用加括号
# C复习，注意区别：
# include <stdio.h>
# int main()
#
# {
#
# char name[] = "李华";
# char *p="一班";
# int age=18;
# printf("我的名字是%s，来自%s,今年%d岁。",name,p,age);
# return 0;
#
# }
print()
# 方法二  .format()
print('方法二：')
print('我叫：{},来自：{}\n'.format(name_,class_))

# 输入
# input函数，默认为str类型
print('---------------输入----------------')
name=input('please input your name:')
age=input('please tell me your age:')
studentnum=int(input('and you student number:'))
print('My name is {}.'.format(name))
print('%s,%s'%(age,type(age)))
print('%d,%s'%(studentnum,type(studentnum)))

