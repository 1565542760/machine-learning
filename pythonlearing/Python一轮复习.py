#求三个数平均值
# a,b,c=eval(input("请输入三个数"))
# l=(a+b+c)/3
# print(l)
# 创建一个五个数构成的列表,并进行升序排序
# a_list=[2,5,6,9,8]
# a_list.sort()
# print(a_list)
#创建一个可以求圆形,三角形,长方形的面积的函数
# def s(a,b,c,r):
#     import math
#     s_yuan=math.pi*r**2
#     p=(a+b+c)/2
#     s_sanjiao=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     s_chang=a*b
#     print(s_yuan,s_sanjiao,s_chang)
# 判断关键词
# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword('s'))
# print(keyword.iskeyword('True'))
# id type value三种重要类型
# x=1
# print(id(x),type(x),x)
# 二进制,八进制,十进制,十六进制
# print(0b10001,0o21,17,0x11)
#转义字符
# print("a\nbb\tccc\bdd\nddd\reee\f666\\33\'")
# x=16/4-2**5*8/4%5//2
# print(x)
# print(0xA+0xB)
# print(~1)#~x==-(x+1)
# print(1^0)
# print(eval('2+4/5'))
# s='a\nb\tc'
# print(len(s))
# print(1 and 5==0)
# print(5+4j > 2-3j)
# a=2
# k=3
# print(a<k and a%2==0)
# print(2**31-1)
# x,y,z=eval(input("请输入三个数"))
# if x>y:
#     x,y=y,x
# if x>z:
#     x,z=z,x
# if y>z:
#     y,z=z,y
# print(x,y,z)
# x=0
# y=True
# print(x>y and 'A'<'B')
# j=0
# for i in range(26,-4,-2):
#     j+=1
#     print(j)
# n=1
# e=0
# while True:
#     for i in range(1,n+1):
#         n*=i
#     e+=1/n
#     if 1 / n < 10 ** -7:
#         break
#     n+=1
# print(e)
