# 序列：在Python中就是一组按顺序排列的值（数据集合）
# Python中的三种内置序列类型：字符串、列表、元组
# 优点：支持索引和切片
# 特征：第一个正索引为0，指向左端；为负数，指向右端。

# 切片：【高级特性】可以根据下标来获取序列对象的任意部分数据
# 语法：[start:end:step] step默认为1
# 下标会越界，但切片不会，如越界不会报错而是不返回数据


# 字符串常用函数
# capitalize() 首字母大写
# isalnum() 判断是否是字母和数字
# islower() 判断是否是小写
# swapcase() 大写和小写互换
# title() 每个单词首字母变大写
# endswith() 是否x结束
# startswith() 是否x开始
# isalpha() 判断是否是字母
# join() 循环取出所有值用xx去连接
# istrip()/rstrip()/strip() 移除左/右/两侧空白
# replace(old,new,count=None) 用new替换count个new，无count全换
# find() 检测x是否在字符串中
# isdigit() 判断是否是数字
# lower()/uper() 大小写转换
# split() 切割字符串
# count() 统计出现的次数

'''
print('-------字符串操作举例---------')
test='python'
print(type(test))
print('the first char for "%s" is %s'%(test,test[0]))
for item in test:
    print(item,end=' ')
    pass
print()

print('\n----------字符串函数举例---------')
name='liam chou'
print('name:%s \nand\nname in cap:%s'%(name,name.capitalize()))
a='    hello     '
b=a.strip()
c=a.rstrip()
print('{}\n{}\n{}'.format(a,b,c))

print('\n--------d=a赋值的问题------')
d=a #实质是引用
print(a,b)
print(id(a),id(d)) #内存地址相同 #问题：为什么每次运行内存都不同？？
a=10 #或更改为：d=10
print(a,d) #问题：为什么不论更改a还是d都不影响另一个
e=5
f=5
print(id(e),id(f)) #问题：为什么e和f的地址相同
# 似乎是由于Python的底层是指针？？？

print('\n----------find&index-----------')
dataStr='I Love Python.'
print(dataStr.find('P')) #可以查找到P的位置
print(dataStr.find('o')) #默认找到第一个后停止，怎么查找所有？？
print(dataStr.find('Z')) #没有返回-1
print(dataStr.find('o',0,2)) #指定查找范围
print(dataStr.index('o')) #index也可以，区别？？
#print(dataStr.index('Z')) #index没找到会报错
print(dataStr.startswith('I')) #一个判断，返回bool
print(dataStr.endswith('on.')) #不限定于起止的一位，可以是一串

print('\n---------slice->[m:n:p]-----------')
strMsg='hello world'
hello=strMsg[0:4] #注意，不包含最后一位，hello->hell
print(strMsg,hello)
print(strMsg[1:])
print(strMsg[:11])
# 有趣的事情来了
print('\n---hello world----')
print(strMsg[-0:])
print(strMsg[-1:])
print(strMsg[-5:])
print(strMsg[-13:])
print(strMsg[:100])
print(strMsg[:-1])
print(strMsg[-1:-6]) #这里没有输出，而不是倒序打印，因为起点比终点落后
print(strMsg[-6:-1])
print(strMsg[1:-1])
# 总结：正则从左往右数，0开头；负则从右往左数，1开头；[m:n]中的m和n只规定起止，不规定打印顺序；含左不含右
#倒序输出 [::-1]
print(strMsg[-1:-6:-1])
print(strMsg[-6:-1:-1]) #与上面相反，这里倒序要求[m:n]中m指定的位置落后于n，否则无输出
print(strMsg[6:1:-2]) #[m:n:p]中p的符号决定方向，值决定间隔
'''

print('\n--------列表---------')

# list:一种有序的数据集合
# 1.增删改查//2.数据可变，地址不变//3.用[]表示，数据间用逗号分割，数据可以是任何类型。

# 常用命令：
# append 追加//count 统计//extend 扩展//index 索引号//insert 插入//pop 删除最后一个//remove 移除第一个//reverse 反转//sort 排序
strA='world'
li=[1,2,3,'hello',strA]
print(type(li),type(strA))
print(len(li),len(strA))




