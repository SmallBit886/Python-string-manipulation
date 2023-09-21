#字符串的驻留机制
a='Python'
b="Python"
c='''Python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(a is b) #Ture
#使用Python交互模式
'''
Microsoft Windows [版本 10.0.22621.2283]
(c) Microsoft Corporation。保留所有权利。
C:\Users\AAA>python
Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> s1=''
>>> s2=''
>>> s1 is s2
True
>>> s1='abc'
>>> s2='abc'
>>> s1==s2
True
>>> s1 is s2
True
>>> s1='abc%'
>>> s2='abc%'
>>> s1==s2
True
>>> s1 is s2
False
>>> id(s1)
1776238243824
>>> id(s2)
1776238243632
>>> a='abc'
>>> b='a'+'bc'
>>> c=''.join(['ab','c'])
>>> a is b
True
>>> a is c
False
>>> a=-5
>>> b=-5
>>> c=-6
>>> d=-6
>>> a is b
True
>>> c is d
False
>>>
'''