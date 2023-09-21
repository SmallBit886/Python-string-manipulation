#字符串的比较操作

print('apple'>'app')    #Ture
print('apple'>'banana') #False
print(ord('a'),ord('b'))    #97 98
print(ord('马')) #39532

print(chr(97),chr(98))  #a b
print(chr(39532))   #马
'''==与is的区别
   ==比较的是value
   is比较的是id
'''
a=b='python'
c='python'
print(a==b)  #Ture
print(a==c)  #Ture

print(a is b)    #Ture
print(a is c)    #Ture
print(id(a))    #2313367341360
print(id(b))    #2313367341360
print(id(c))    #2313367341360
