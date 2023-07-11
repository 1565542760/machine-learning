'''#二、完成第一章（13页）习题3
print("*"*15,"\nHello word\n","*"*15)
#三、创建一个python文件，编程解决下面问题，求三个整数的平均数，并写出运行结果
a,b,c=eval(input("请输入三个数字："))
sum=a+b+c
avel=sum/3
print("这三个数的平均数为%f"%avel)
#四、请编写程序，去查看python中关键字列表，并判断‘not’以及‘float’是否为关键字
import keyword
print(keyword.kwlist)
print(keyword.iskeyword('not'))
print(keyword.iskeyword('flaot'))
#五、编写运行温度转换程序
F=eval(input("请输入华氏摄氏度"))
C=(F-32)/18
print("该华氏摄氏度对应的摄氏度为%f"%C)
C=eval(input("请输入摄氏度"))
F=C*1.8+32
print("该摄氏度对应的华氏摄氏度为%f"%F)'''
'''heights=[]#列表
while True:
    height=eval(input())
    if height<=0:
        break
    heights.append(height)#插入列表之后
max_height=max(heights)
min_height=min(heights)
ave_height=sum(heights)/len(heights)
print(max_height)
print(min_height)
print(ave_height)'''
'''for a in range(2,10,2):#for循环与c语言类似，range（）函数定义了循环的次数，而for后跟的a则为输出项,比c语言简单但没c语言灵活
    print(a)'''
'''
sum,i=0,1
while i<=200:
    sum+=i
    i+=1
print(sum)'''
'''
sum=0
while True:
    num=eval(input("请输入数字"))
    if num<=0:
        break
    sum=sum+num
print(sum)'''
'''count=int(input())
while count<5:
    print(count,"is less than 5")
    count+=1
else:
    print(count,"is not less than 5")'''
'''sum=0
for a in range(1,201):
    sum+=a
print(sum)'''
'''for a in range(1000,10000):
    qsum=a//100
    hsum=a%100
    if a==(qsum+hsum)**2:
        print(a)'''
'''j=0
for i in range(1,101,1):
    if i%7==0 or i%11==0:
        if i%7==0 and i%11==0:
            i+=1
        else:
            j+=1
            if j<=10:
                print(" ",i,end='')
            else:
                j=0
                print("\n",i,sep='',end='')'''
'''m=eval(input("请输入一个数字"))
flag=1
for i in range (2,m):
    if m%i==0:
        flag=0
if flag==1:
    print(m,"为素数")
else:
    print(m,"不为素数")'''
'''for i in range(1,10):
    for j in range(1,i+1):
        print("\t",j,"*",i,"=",i*j,end='')
    print()'''
'''for i in range(1,10):
    for j in range(i,i+1):
        print(" "*(10-i),"*"*j*2,end='')
    print()'''
'''n=eval(input("请输入行数"))
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end='')
    for j in range(1,2*i):
        print("*",end='')
    print()'''
'''1、
n=eval(input("请输入行数"))
for i in range(0,n+1):
    for k in range(0,i):
        print(" ",end='')
    for j in range(1,2*n-2*i):
        print("*",end='')
    print()
'''
#2、
'''n=eval(input("请输入行数"))
j=2*n+1
for i in range(j, 0, -2):
    print(" "*((n-i)//2),'*' * i)'''
'''for i in range(1,n+1):
    for j in range(i):
        print(" ",end='')
    for k in range(1,2*n-2*i+2):#2*总行数-2*第几行+1
        print("*",end='')
    print()'''
'''n=eval(input("请输入行数"))
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(1,2*n-2*i+2):
        print("*",end="")
    print()'''
'''n=eval(input("请输入行数"))
for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for k in range(1,2*n-2*i+2):
        print("*",end="")
    print()'''
'''for k in range(21):
    for j in range(51):
        for i in range(51):
            if k+j+i==50 and 5*k+2*j+i==100:
                print(i,k,j)'''
'''a=[]
a.append(1)
a.append(2)
a=a+[3]
print(a)'''
'''
#创建列表
a_list=[11,12,13,14,15,16,17,18]
#切片
print(a_list[:7])
print(a_list[::2])
print(a_list[::-2])
#添加
a_list=a_list+[19]
a_list.insert(18,20)
a_list.append(21)
a_list.extend([22])
print(a_list)
#检索
print(a_list.index(13,0,4))
print(a_list.count(17))
print(7 in a_list)
print(a_list)
#删除
del a_list[0]
print(a_list)
a_list.remove(18)
print(a_list)
print(a_list.pop(3))
print(a_list)
b_list=[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
#常用函数
print(len(b_list))
print(max(a_list))
print(min(b_list))
print(sum(a_list))
print(sorted(b_list,reverse=True))
b_list.sort(reverse=True)
print(b_list)
a_list.reverse()
print(a_list)
'''
# m=1000
# for a in range(2,m+1):
#     s=0
#     L1=[]
#     for i in range(1,a):
#         if a%i==0:
#             s+=i
#             L1.append(i)
#             if s==a:
#                 print("%d its factors are:"%a,L1)
'''
ls = []
for i in range(1,1001):
    for j in range(1,i):
        if i % j == 0:
            ls.append(j)
    if sum(ls) == i:
        print("{}是完数，其因子包括{}".format(i,ls))
    ls.clear()
'''
# while(1):
#     {
#         print("I love you")
#     }
# 创建字典
# a={'1':"ppx",'2':'ppt'}
# b=dict()
# keys=['a','b','c']
# values = [1, 2, 3]
# c= dict(zip(keys, values))
# d= dict(a=1, b=2, c=3, d='a')
# e = dict.fromkeys(['a', 'b', 'c'], [1,2,3])
# #读取字典元素
# print(a['1'])
# print(b.get('a'))#类似于if，else
# #增删改查都是先读取后操作
# # 添加
# b["d"]= 4
# b.update({'d': 4, 'e': 5})
# print(d)
# # 修改
# b["a"]=0.1
# b.update(zip(['f','g','h'],[6,7,8]))
# #删除
# del a['1']#删除对应键值的元素
# d.pop("a")#删除指定元素
# d.popitem()#随机删除元素
# e.clear()#清空元素
# del e#删除该字典
# #遍历
# a.keys()#以列表方式返回所有键
# a.values()#以列表方式返回所有值
# a.items()#以列表形式返回元素（键：值，）
#
#
# #创建集合
# f={1,2,3,4,5,6,7}
# g=set(range(6))
# h=frozenset(range(9,15,1))#冻结集合,与集合的关系类似于元组和列表
# for i in f:
#     print(i,end='')
# print(1 in f)
# #添加
# f.add(8)
# f.update(h)#无重复
# #删除
# f.remove(10)#不存在元素报错
# f.discard(11)#不存在元素不报错
# f.pop(12)
# f.clear()

# #需求，不使用len来统计字符串的长度
# str1="itheima"
# str2="itcast"
# str3="python"
# def my_len(data):
#     count=0
#     for i in data:
#         count+=1
#     print(f"字符串{data}长度是{count}")
# my_len(str1)
# my_len(str2)
# my_len(str3)

# def mtemp (x):
#     if 36<x<37.5:
#         print("please")
#     else:
#         print("gun")
# mtemp( eval(input("please input your tempurter")))

#global可以让函数内的局部变量变成全局变量


#要求：程序启动后要求输入客户姓名，查询余额、存款、取款后都会返回主菜单，存款取款后都会显示一下当前余额，客户选择退出或者输出错误程序退出
# money=50000
# name=input("请输入姓名：")
# def query(show_header):
#     if show_header:
#         print("---------查询余额---------")
#     print(f"{name},您好，您的剩余余额为：{money}元")
# def saving(num):
#     global money
#     money+=num
#     print("---------存款---------")
#     print(f"{name},您好，您存款{num}元成功")
#     query(False)

#一、
# s1=ord(input("请输入一个大写字母"))
# s2=chr(s1+32)
# print("该字符小写为%s"%s2)
#二、
# year,month,day=eval(input("请输入你的出生年月日"))
# print("%04d/%02d/%02d"%(year,month,day))
#三、
# x,y,z=eval(input("请输入长方体的长宽高"))
# Volume=x*y*z
# print("长方体的体积为%06.3f"%Volume)
#四、
# import math
# a,b,c=eval(input("请输入三角形三边长度"))
# if (a+b<=c or a+c<=b or b+c<=a):
#     print("你个傻逼，这他妈不是三角形")
# else:
#     p = (a + b + c) / 2
#     S = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print("三角形的面积为%f" % S)

#五、（1）
# n=eval(input("请输入一个五位自然数"))
# ten_thousand=n//10000
# thousand=(n%10000)//1000
# hundred=(n%1000)//100
# ten=(n%100)//10
# one_seat=n%10
# fifth_num=one_seat*10000
# forth_num=ten*1000
# third_num=hundred*100
# second_num=thousand*10
# new_num=ten_thousand+second_num+third_num+forth_num+fifth_num
# if new_num==n:
#     print("这个数字是回文数")
# else:
#     print("这个数字不是回文数")

#（2）
# n=eval(input("请输入一个五位自然数"))
# size=None
# i ,p= 1,0
# # while size!=0:
# #     size=n//(10*i)
# #     i*=10
# #     p+=1
# p=len(str(n))
# a_list=[]
# for j in range(p):
#     k=n//(10**(j))%10
#     a_list.append(k)
# b_list=list(reversed(a_list))
# # print(a_list,b_list)
# if b_list==a_list:
#     print("这个数字是回文数")
# else:
#     print("这个数字不是回文数")

#(3)

# n=eval(input("请输入一个五位自然数"))
# length=len(str(n))
# a_list=[]
# for i in range(length):
#     a_list.append(str(n)[length-1-i])
# b_list=list(reversed(a_list))
# if b_list==a_list:
#     print("这个数字是回文数")
# else:
#     print("这个数字不是回文数")

# n=input("请输入一个五位自然数")
# length=len(n)
# a_list=[]
# for i in range(length):
#     a_list.append(n[length-1-i])
#     # print(a_list)
# if list(n)==a_list:
#     print("这个数字是回文数")
# else:
#     print("这个数字不是回文数")

# n=input("请输入一个五位自然数")
# x=n[::-1]
#     # print(a_list)
# if n==x:
#     print("这个数字是回文数")
# else:
#     print("这个数字不是回文数")

# import he
# a_list=[1,2,3,8,10,16,17]
# print(he.func_sum(a_list))

# import random
# a_list=[]
# for i in range(10):
#     print(int(100*random.random()))
#
# import random
# for i in range(10):
#     print(random.randrange(1,101,2))
#
# import random
# print(random.choice(['good', 'hello', 'is', 'hi', 'boy']))   # 从list列表中随机取
#
# import random
# print(random.choice('学习python'))   # 从字符串中随机取一个字符

# import he
# r1=2
# r2=1
# h=1
# print(he.dunc_v(r1,r2,h))

# num1,num2,num3,num4=eval(input("请输入四个整数"))
# if num1>num2:
#     num1,num2=num2,num1
# if num1>num3:
#     num1,num3=num3,num1
# if num2>num3:
#     num2,num3=num3,num2
# if num1>num4:
#     num1,num4=num4,num1
# if num2>num4:
#     num2,num4=num4,num2
# if num3>num4:
#     num3,num4=num4,num3
# print(num1,num2,num3,num4)

# x=eval(input("请输入变量x的值"))
# if x<-4:
#     y=x+9
# elif x>=4:
#     y=2*x-15
# else:
#     y=x**2+2*x+1
# print(y)

# r_id ,t=eval(input("请输入员工工号及工作时长"))
# y=t*80
# if t<60:
#     y=y-700
# elif y>120:
#     t1=t-120
#     y=80*120+t1*80*1.15
# print(y)

# r_id ,t=eval(input("请输入员工工号及工作时长"))
# y=120*80+(t-120)*80*1.15
# if t<120:
#     y=t*80
#     if t<60:
#         y=t*80-700
# print(y)

# import math
# a,b,c=eval(input("请输入一元二次方程系数"))
# dai_ao_ta=b**2-4*a*c
# if dai_ao_ta<0:
#     print("方程无解")
# elif a==0:
#     x1=x2=-c/b
#     print(x1)
# else:
#     x1=(-b+math.sqrt(dai_ao_ta))/(2*a)
#     x2=(-b-math.sqrt(dai_ao_ta))/(2*a)
#     print(x1,x2)

# x,y,z=eval(input("请输入三个数"))
# t=x**2+y**2+z**2
# if t>1000:
#     t1=t//1000
#     t2=str(t1)
#     t3=t2[:]
#     for i in range(len(t3)):
#         print(t3[i])
# else:
#     i=x+y+z
#     print(i)

# data=open("D://常用//python//pythonlearing//rrr.txt","r")
# # data_new=data.read(4)
# # print(data_new)
# print("---------------")
# while(True):
#     file = data.readline()
#     if not file:
#         break
#     print(file,end="")
# print("\n---------------")
# l=len(data.readline())
# for i in range(l):
#     print(data.readline())
# print("---------------")
# for j in data.readlines():
#     print(j)
# data.close()

# data=open("D://常用//python//pythonlearing//rrr.txt","a")
# data.write("abc")
# data.close()

# file=open("D://常用//python//pythonlearing//rrr.txt","r")
# file_2=open("D://常用//python//pythonlearing//ddd.txt","w")
# # while(True):
# #     data = file.readline()
# #     if not file:
# #         break
# #     print(data,end="")
# #     file_2.writelines(list(data))
# data=file.readlines()
# file_2.writelines(data)
# file.close
# file_2.close()

# l=0
# for i in range(1,201):
#     if i%11==0:
#         l += 1
#         print("第",l,"个数为",i)
# print("个数为",l)

# n=eval(input("请输入1的阶层加到n的阶层的n为多少"))
# sum=0
# for i in range(1,n+1):
#     num = 1
#     for j in range(1,i+1):
#         num=num*j
#     sum+=num
# print("和为",sum)

# n=eval(input("请输入1的阶层加到n的阶层的n为多少"))
# sum=0
# i=1
# while i<=n:
#     num = 1
#     j=1
#     while j<=i:
#         num=num*j
#         # print("dd",num)
#         j+=1
#     sum+=num
#     # print("he",sum)
#     i+=1
# print("和为",sum)

# for i in range(1,7):
#     print(" "*(6-i),"*"*(2*i-1))
# for j in range(1,8):
#     print(" "*j,"*"*(10-((2*j)-1)))

# x,y=eval(input("请输入两个大于1的数，要求第一个数大于第二个数"))
# if x<=0 or y<=0:
#     print("请按要求输入")
# elif x>y:
#     print("请按要求输入")
# elif x==y:
#     print("请按要求输入")
# elif x==1 or y==1:
#     print("请按要求输入")
# else:
#     for i in range(x,y+1):
#         flag=1
#         for j in range (2,i):
#             if i%j==0:
#                 flag=0
#         if flag==1:
#             print(i,"为素数")

# import math
# for i in range(1000,10000):
#     qian=i//1000
#     bai=i%1000//100
#     shi=i%100//10
#     ge=i%10
#     if qian==bai:
#         if shi==ge:
#             j=math.sqrt(i)
#             if j.is_integer():
#                 print(i)

# for x in range(10):
#     for y in range(13):
#         z=72-8*x-6*y
#         if x>=0 and y>=0 and z>=0 and x+y+z==36:
#             print(x,y,z)

# string1=open("string1.txt")
# string2=open("string2.txt")
# string3=open("string3.txt","w")
# s1=string1.readlines()
# s2=string2.readlines()
# s=s1+s2
# string3.writelines(s)
# string1.close()
# string2.close()
# string3.close()

# from random import *
# fb=input("请输入文件名")
# fb_1=open(fb,"w")
# for i in range (1,11):
#     number=str(randint(1,101))
#     fb_1.write(" ")
#     fb_1.write(number)
# fb_1.close()

# fb=open("string3.txt")
# p=fb.tell()
# print(p)
# fb.read(4)
# p=fb.tell()
# print(p)
# fb.seek(0.0)
# p=fb.tell()
# print(p)
#
# s1=input()
# s2=s1.lower()
# fb=open("string3.txt","w")
# fb.writelines(s2)
# fb.close()
#
# fb2=open("string1.txt")
# fb2.readline()
# a=fb2.tell()
# print(a)
# b=fb2.seek(0,2)
# print(b)
# fb2.close()
#
# s="Python Program"
# fb=open("string1.txt","w")
# fb.writelines(s)
# c=fb.seek(0,2)
# print(c)
# fb.close()

# import random
# num=random.randint(1,10)
#
# while True:
#     try:
#         n=int(input("输入一个整数"))
#     except:
#         print("输入错误，重新输入")
#         continue
#     if n>num:
#         print(".....")
#     elif n<num:
#         print("_____")
#     else:
#         print("11111")
#         break

# while True:
#     try:
#         a=int(input("输入一个数字"))
#         b=int(input("请输入一个数字"))
#         c=int(input("请输入一个数字"))
#         if b==0:
#             print("你个傻逼")
#             break
#     except:
#         print("输入错误，重新输入")
#     else:
#         d=a/b+c
#         print(d)
#     finally:
#         print("程序执行结束")
#         break

# def v(a,b,c) :
#     if a<=0 or b<=0 or c<=0:
#         ex=Exception("不符合")
#         raise ex
#     else:
#         v=a*b*c
#         return v
# try:
#     a,b,c=eval(input("..."))
#     d=v(a,b,c)
#     print(d)
# except Exception as result:
#   print(result)


# def pass_word(p):
#     if len(p) >=8:
#         word = ""
#         D_word=""
#         num=""
#         k_word=""
#         for i in p:
#             if i>='a' and i<='z':
#                 word=word+i
#             elif i>='A' and i<='Z':
#                 D_word=D_word+i
#             elif i>='0' and i<='9':
#                 num=num+i
#             else:
#                 k_word=k_word+i
#         if (len(word)>0 or len(D_word)>0) and len(num)>0 and len(k_word)>0:
#             return p
#         else:
#             et = Exception("密码规则不符合要求")
#             raise et
#     else:
#         ex=Exception("密码长度不符合要求")
#         raise ex
# try:
#     p=input("...")
#     d=pass_word(p)
#     print(d)
# except Exception as result:
#   print(result)

# import random
# num=random.randint(1,10)
# flage=0
# d=eval(input("输入限制次数"))
# while True:
#     try:
#         n=int(input("输入一个整数"))
#         flage+=1
#     except:
#         print("输入错误，重新输入")
#         continue
#     if flage>d:
#         ex=Exception("次数超出限制")
#         raise ex
#     else:
#         if n>num:
#             print(".....")
#         elif n<num:
#             print("_____")
#         else:
#             print("11111")
#             break

# num=eval(input("请输入三位整数"))
# if num<100 or num>999:
#     print("请按规定重新输入")
# else:
#     num=int(num)
#     a=num//100
#     b=num%100//10
#     c=num%10
#     v=a*b*c
#     print("百位：",a,"十位：",b,"个位：",c,"各位之积",v,sep=";",end="#")

# while True:
#     num=eval(input("请输入三位整数"))
#     if num>=100 and num<=999:
#         num=int(num)
#         a=num//100
#         b=num%100//10
#         c=num%10
#         v=a*b*c
#         print("百位：",a,"十位：",b,"个位：",c,"各位之积",v,sep=";",end="#")
#         break
#     else:
#         print("请按规定重新输入")


# elem=[]
# size=eval(input("请输入要输入的元素个数\n"))
# for i in range(0,size):
#     print("要输入第%d个元素"%(i+1))
#     num=eval(input("请输入要输入的元素"))
#     elem.append(num)
# print("元素全部添加完成")
# print(elem)
# q1,h1=eval(input("请分别输入要升序排列的前元素索引号与后元素索引号\n"))
# q1=q1-1
# elem_q=sorted(elem[q1:h1],reverse=False)
# print(elem_q)
# q2,h2=eval(input("请分别输入要降序序排列的前元素索引号与后元素索引号\n"))
# q2=q2-1
# elem_h=sorted(elem[q2:h2],reverse=True)
# print(elem_h)


# elem=[]
# size=eval(input("请输入要输入的元素个数\n"))
# for i in range(0,size):
#     print("要输入第%d个元素"%(i+1))
#     num=eval(input("请输入要输入的元素"))
#     elem.append(num)
# print("元素全部添加完成")
# elem.sort()
# a=b=c=d=e=0
# for i in elem:
#     if i>90:
#         a+=1
#     elif i>80:
#         b+=1
#     elif i>70:
#         c+=1
#     elif i>60:
#         d+=1
#     else:
#         e+=1
# print(a,b,c,d,e)

# idc=[]
# elem=[]
# size=eval(input("请输入要输入的元素个数\n"))
# for i in range(0,size):
#     print("要输入第%d个学生序号及成绩\n"%(i+1))
#     idcd=eval(input("请输入该学生id\n"))
#     num=eval(input("请输入该学生成绩\n"))
#     idc.append(idcd)
#     elem.append(num)
# print("元素全部添加完成\n")
# print(idc)
# print(elem)
# m_score=max(elem)
# p=elem.index(m_score)
# print(p)
# a=idc[p]
# b=elem[p]
# print("学生序号为",a,"分数为",b)

# s=input("请输入一串字符串")
# c=input("请输入要删除的字符串元素")
# d=c.lower()
# e=c.upper()
# new_s = s.replace(d, "")
# new_s = new_s.replace(e, "")
# print(new_s)


# s=input("请输入一串字符串")
# s1=s[::-1]
# print(s1)

# 一、编程：所谓完数是指一个数正好是它的所有约数之和。例如 6 就是一个完数，
# 因为 6 的因子有 1,2,3，并且 6=1+2+3.
# （1） 编写一个函数，求 10000 以内的所有的完数，然后按照如下的格式的
# 输出 10000 以内的所有完数是[a,b,c,….]。列表
# def wanshu():
#     t = eval(input("请输入判断范围"))
#     t += 1
#     a_list = []
#     for num in range(1, t):
#         sum=0
#         for i in range(1,num):#设置循环判断
#             if num%i==0:
#                 sum+=i
#         if sum==num:
#             if num != None:
#                 a_list.append(num)
#     print(a_list)
# wanshu()
# （2） 如何改造这个函数，让它能同时求 10 以内、100 以内、1000 以内、
# 10000 以内所有的完数。
# def wanshu_gaijin():
#     t = eval(input("请输入判断范围"))
#     b_list=[]
#     j=0
#     k=0
#     while True:
#         if t//(10**j)!=0:
#             k+=1
#             j+=1
#         else:
#             break
#     for i in range(1,k):
#         a_list = []
#         l=10**i
#         for num in range(1, l):
#             sum=0
#             for i in range(1,num):#设置循环判断
#                 if num%i==0:
#                     sum+=i
#             if sum==num:
#                 if num != None:
#                     a_list.append(num)
#         print(a_list)
#         del a_list
# wanshu_gaijin()

# 二、编程： 如果有两个数，每一个数的所有约数（除它本身之外）的和正好等
# 于对方，则称这两个数为互满数。求出 10000 以内所有的互满数，并按照下
# 面的格式显示输出
# 如 220 的互满数数为 284。
# def humanshu(num):
#     t1=0
#     for i in range(1,num):
#         if num%i==0:
#             t1+=i
#     return t1
# l=eval(input("请输入范围数字"))
# for num1 in range(1,l):
#     num2=humanshu(num1)
#     t2=humanshu(num2)
#     if t2==num1 and num2<l and num2>num1:
#         print(num1,"的互满数数为",num2)

# 三、编程：使用递归函数解决下面的问题：一个人赶着鸭子去每个村庄卖，每经
# 过一个村子卖去所赶鸭子的一半又一只。这样他经过七个村子后还剩下两只
# 鸭子，问他出发的时候共赶了多少只鸭子，经过每个村子的卖出多少只鸭
# 子？
# def duck(n):
#     if n==8:
#         return 2
#     else:
#         return (duck(n+1)+1)*2
# n=duck(1)
# for i in range(1,8):
#     d1=duck(i)
#     d2=duck(i+1)
#     d=d1-d2
#     print("经过第",i,"个村子卖出",d,"个鸭子")
# print("总共赶了",n,"个鸭子")

# 四、使用递归函数解决下面的问题：
# 角谷定理。输入一个自然数，若为偶数，则把它除以 2，若为奇数，则把它乘
# 以 3 加 1。经过有限次运算后，总可以得到自然数的值为 1，求经过多少次可以
# 得到自然数为 1
# def jiaogu(num):
#     if num==1:
#         return 0
#     else:
#         if num%2==0:
#             return 1+jiaogu(num/2)
#         else:
#             return 1+jiaogu(num*3+1)
# num=eval(input("输入一个自然数"))
# t=jiaogu(num)
# print("经过",t,"经过多少次可以得到自然数为 1")

# count=0
# def jiaogu(num):
#     if num==1:
#         return count
#     else:
#         if num%2==0:
#             return 1+jiaogu(num/2)
#         else:
#             return 1+jiaogu(num*3+1)
# num=eval(input("输入一个自然数"))
# t=jiaogu(num)
# print("经过",t,"经过多少次可以得到自然数为 1")


# 一、编程：从键盘上输入一行字符，然后将其中的大写字母全部转换成小写字母，
# 然后输出到一个磁盘文件中保存。
# s=input("请输入传字符")
# n_file=open("D://常用//python//pythonlearing//rrr.txt","w")
# n_file.writelines(s.lower())
# n_file.close()
# 二、编程用 readline 方法完成文件的复制，复制成功后修改源文件的文件名为每
# 个同学的名字的拼音的简写，并求取源文件的文件长度。
# import os
# n_file=open("D://常用//python//pythonlearing//rrr.txt","r")
# a_file=open("D://常用//python//pythonlearing//gaokai.txt","w")
# a=[]
# while True:
#     s=n_file.readline()
#     if not s:
#         break
#     a.append(s)
# b=a[0]
# print(len(b))
# a_file.writelines(b)
# n_file.close()
# a_file.close()
# os.rename("D://常用//python//pythonlearing//gaokai.txt","D://常用//python//pythonlearing//ooo.txt")
# 三、编写程序：创建一个文件，在文件中写入下面的几行话：承诺书；我是 21
# 级信管的学生***（自己的名字）；我保证每天打卡；如果没有按时打卡，我
# 同意接受惩罚；读取文件的内容并输出；然后把文件中的“我保证每天打卡”
# 改为“我一定在中午 12 点前完成打卡”。
# new_file=open("D:/常用/python/string1.txt","wt+")
# new_file.writelines("承诺书；我是 21级信管的学生是一个小蛋高；我保证每天打卡；如果没有按时打卡，我同意接受惩罚")
# new_file.seek(0)
# while True:
#     s=new_file.readline()
#     if not s:
#         break
#     print(s)
# new_file.seek(0)
# while True:
#     s=new_file.readline()
#     if not s:
#         break
#     s=s.replace("我保证每天打卡","我一定在中午 12 点前完成打卡")
#     print(s)
# new_file.close()
# 四、编写程序：定义用户输入密码函数，要求密码长度不小于 8，而且必须包
# 含字母和数字以及特殊字符。且输入密码的次数不超过 3 次。
# def pass_word(p):
#     if len(p) >=8:
#         word = ""
#         D_word=""
#         num=""
#         k_word=""
#         for i in p:
#             if i>='a' and i<='z':
#                 word=word+i
#             elif i>='A' and i<='Z':
#                 D_word=D_word+i
#             elif i>='0' and i<='9':
#                 num=num+i
#             else:
#                 k_word=k_word+i
#         if (len(word)>0 or len(D_word)>0) and len(num)>0 and len(k_word)>0:
#             return p
#         else:
#             et = Exception("密码规则不符合要求")
#             raise et
#     else:
#         ex=Exception("密码长度不符合要求")
#         raise ex
# count=0
# while True:
#     try:
#         p=input("请设置密码")
#         d=pass_word(p)
#         print(d)
#         break
#     except Exception as result:
#       print(result)
#     finally:
#         count+=1
#     if count>=3:
#         print("超出设置次数")
#         break


# from sklearn.datasets import load_iris
# from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
# import jieba
# import pandas as pd
#
# def cut_word(text):
#     '''
#     进行中文分词
#     :param text:
#     :return:
#     '''
#     text=" ".join(list(jieba.cut(text)))
#     return text
#
# def text_chinese_count_demo2():
#     '''
#     中文文本特征抽取：CountVecotrizer
#     :return:
#     '''
#     #将中文文本进行分词
#     data=pd.read_csv("文献.txt")#用分词工具
#     data_new=[]
#     b_list=[]
#     for sent in data:
#         data_new.append(cut_word(sent))
#     print("分词呈现",data_new)
#     #1、实例化一个转换器类
#     transfer = CountVectorizer()#stop_words=[]
#     #2、调用fit_transform
#     data_final=transfer.fit_transform(data_new)
#     print("词频:\n",data_final.toarray())
#     data_2=data_final.toarray()
#     data_3=data_2[0]
#     data_4=data_3[::1]
#     for i in data_4:
#         if i!=" ":
#             b_list.append(i)
#     Max_Position=0
#     Max_Posit_list=[]
#     Min_Position=0
#     Min_Posit_list=[]
#     for j in b_list:
#         if j==max(b_list):
#             Max_Posit_list.append(Max_Position)
#         Max_Position+=1
#     for k in b_list:
#         if k==min(b_list):
#             Min_Posit_list.append(Min_Position)
#         Min_Position+=1
#     data_5=transfer.get_feature_names_out()
#     Max_fecture_name=[]
#     for l in Max_Posit_list:
#         Max_fecture_name.append(data_5[l])
#     Min_fecture_name=[]
#     for m in Min_Posit_list:
#         Min_fecture_name.append(data_5[m])
#     print("最大词频为：", max(b_list),"最大词频对应的词语：", Max_fecture_name,"最小词频：",min(b_list),"最小词频对应的词语",Min_fecture_name)
#     print("特征名:\n", transfer.get_feature_names_out())
#     return None
#
# def tfidf_demo():
#     '''
#     用TF-IDF的方法进行文本特征抽取（重要程度）
#     :return:
#     '''
#     data = pd.read_csv("文献.txt")  # 用分词工具
#     data_new = []
#     b_list=[]
#     for sent in data:
#         data_new.append(cut_word(sent))
#     print(data_new)
#     # 1、实例化一个转换器类
#     transfer = TfidfVectorizer()
#     # 2、调用fit_transform
#     data_final = transfer.fit_transform(data_new)
#     print("词的重要程度(基于TF_IDF方法):\n", data_final.toarray())
#     data_2 = data_final.toarray()
#     data_3 = data_2[0]
#     data_4 = data_3[::1]
#     for i in data_4:
#         if i != " ":
#             b_list.append(i)
#     Max_Position = 0
#     Max_Posit_list = []
#     Min_Position = 0
#     Min_Posit_list = []
#     for j in b_list:
#         if j == max(b_list):
#             Max_Posit_list.append(Max_Position)
#         Max_Position += 1
#     for k in b_list:
#         if k == min(b_list):
#             Min_Posit_list.append(Min_Position)
#         Min_Position += 1
#     data_5 = transfer.get_feature_names_out()
#     Max_fecture_name = []
#     for l in Max_Posit_list:
#         Max_fecture_name.append(data_5[l])
#     Min_fecture_name = []
#     for m in Min_Posit_list:
#         Min_fecture_name.append(data_5[m])
#     print("重要度最大为：", max(b_list), "最大对应的词语：", Max_fecture_name, "重要度最小为：", min(b_list),
#           "最小对应的词语", Min_fecture_name)
#     print("特征名:\n", transfer.get_feature_names_out())
#     return None
# text_chinese_count_demo2()
# tfidf_demo()