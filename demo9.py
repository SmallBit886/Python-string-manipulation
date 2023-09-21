#字符串的切片操作
'''字符串是不可变类型；不具有增，删，改等操作'''
'''切片操作将产生新的对象'''
s='hello,python'
s1=s[:5]    #由于没有指定起始位置，所以从0开始
s2=s[6:]    #由于没有指定结束位置，所以切到字符串的最后元素
s3='!'
newstr=s1+s3+s2
print(s)    #hello,python
print(s1)   #hello
print(s2)   #python
print(newstr)   #hello!python

print('--------------------------')
print(id(s))         #2571458983664
print(id(s1))        #2571462125232
print(id(s2))        #2571462125296
print(id(s3))        #2571462124976
print(id(newstr))    #2571462145200

print('----------切片[start,end,step---------------]')
print(s[1:5:1]) #ello
print(s[::2])   #h l o p t o
print(s[::-1])  #nohtyp,olleh
print(s[-6::1]) #python