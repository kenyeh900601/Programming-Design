# -*- coding: utf-8 -*-
"""week45

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cMQaa_35sfdobI2uHZuoRnCx_wr_i58R
"""

a=int(input("第一次期中考成績"))
b=int(input("第二次期中考成績"))
c=int(input("期末考成績"))
print(a+b+c)
print((a+b+c)/3)

d=int(input("請輸入幾尺"))
print(d,"尺")
e=int(input("請輸入幾吋"))
print(e,"吋")
f=(d*12+e)*2.54
print("轉換成",f,"公分")

a=1
a

a="Python"
a

a=123
b=123.456
c="Python"
d=False

a=1
print(a, id(a))
b="Python"
print(b, id(b))

x=1
y=2
print(id(x), id(y))

z=1
print(id(x), id(z))

import sys
x=18
sys.getsizeof(x)

print(False)
print(True)
print(False+3)
print(True+3)
print(False==0)
print(True==1)

print(False, type(False))
print(True+1, type(True+1))

print(bool(1))
print(bool(0))
print(bool(()))

a = 100
b = 100.001

print(type(100))
print(type(100.001))

print(int(100))
print(float(100.001))

print(0.1+0.1+0.1)

s1 = '春眠不覺曉,處處聞啼鳥。'
print(s1)
s2 = "夜來風雨聲,花落知多少。"
print(s2)
s3 = '作者"孟浩然" 詩名"春曉"'
print(s3)
s4 = "作者'孟浩然' 詩名'春曉'"
print(s4)
s5 = ''' 春眠不覺曉,處處聞啼鳥。
夜來風雨聲,花落知多少。
作者"孟浩然" 詩名"春曉"
'''
print(s5)

a = 123
b = 123.456
print(a)
print("b=", b)
print(a, b, end = '.')

print("Bigflower Francis")
print("Bigflower \n Francis")
print("Bigflower \t Francis")

s = input()
s

s = input("Enter Your Name:")
s

s = input ("Enter Your Name:")
print("Hi,", s)

s = input ("Enter Your Number:")
print(s+100)

s = int(input("Enter Your Number:"))
print(100 + s)

s = float(input("Enter Your Number:"))
print(100 + s)

s = eval(input("Enter Your Number:"))
print(100 + s)
s = eval(input("Enter Your Number:"))
print(100 + s)

a = 1 + 2

print (5<2)
print (5<=2)
print (5>2)
print(5>=2)
print(5!=2)
print(5==2)

X = 70
print((X>60) and (X<80))
print((X>60) or (X<80))
print(not(X>60))

x = 1
y = [1,2,3]
print(x in y)
print( x not in y)
x = [1,2,3]
y = [1,2,3]
print(id(x), id(y))
print(x is y)
print(x is not y)

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 // 2)
print(5 % 2)
print(5 ** 2)

a = 5
a = a + 2
print(a)
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)
a//=2
print(a)
a%=2
print(a)
a**=2
print(a)

s1 ="123"
s2 = "456"
s3 = s1+s2
print(s3)
s4 = s1*2
print(s4)

s5 = '春眠不覺曉,處處聞啼鳥。\n\
夜來風雨聲,花落知多少。\n\
\t作者"孟浩然" 詩名"春曉"'
print(s5)

s = '123456789'
print(s[0])
print(s[1])
print(s[-1])
print(s[-2])

s = '0123456789'

print('s=', s)
print('s[0]=', s[0])
print('s[1]=', s[1])
print('s[-1]=', s[-1])
print('s[-2]=', s[-2])

print('s=', s, 's[:]=', s[:])
print('s=', s, 's[5:]=', s[5:])
print('s=', s, 's[-2:]=', s[-2:])
print('s=', s, 's[:5]=', s[:5])
print('s=', s, 's[:-2]=', s[:-2])
print('s=', s, 's[7:9]=', s[7:9])
print('s=', s, 's[-4:-1]=', s[-4:-1])
print('s=', s, 's[5:-2]=', s[5:-2])
print('s=', s, 's[2:10:2]=', s[2:10:2])
print('s=', s, 's[::-1]=', s[::-1])
print('s=', s, 's[-1::-1]=', s[-1::-1])

a = -2
print(abs(a))
print(abs(-10))
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))
print(pow(2,3))
print(round(5.8))
print(round(3.14159,2))

s = '春眠不覺曉,處處聞啼鳥,夜來風雨聲,花落知多少。'
print(len(s))
s1='春眠不覺曉,處處聞啼鳥,夜來風雨聲,花落知多少。'
list1=s1.split(',')
print(list1)
list1 = ['春眠不覺曉','處處聞啼鳥','夜來風雨聲','花落知多少。']
s2=','.join(list1)
print(s2)

s1='春眠不覺曉,處處聞啼鳥,夜來風雨聲,花落知多少。'
s3=s1.replace('春','冬')
print(s3)
s1='春眠不覺曉,處處聞啼鳥,夜來風雨聲,花落知多少。'
print(s1.find('花落'))
print(s1.count('處'))
s1='An apple a day.'
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())
print(s1.upper())
print(s1.lower())

s1='春眠不覺曉,處處聞啼鳥,夜來風雨聲,花落知多少。'
print(s1.startswith('春眠'))
print(s1.endswith('多少。'))
s1='春眠不覺曉'
print(s1.center(10))
print(s1.rjust(10))
print(s1.ljust(10))
s1='123'
print(s1.zfill(5))
s1=' Hello,Mary. '
print(s1.strip())
print(s1.lstrip(' H'))
print(s1.rstrip(' .'))