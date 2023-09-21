#
#字符串的大小写转换操作的方法
s='hello,python'
a=s.upper()     #会产生一个新的字符串对象
print(a,id(a))
print(s,id(s))

b=s.lower()     #会产生一个新的字符串对象
print(b,id(b))
print(s,id(s))

print(b==s) #内容相等
print(b is s)   #地址不相等

s1='hello，heHe'
print(s1.swapcase())    #大写转小写，小写转大写

print(s1.title())   #每个英文单词的第一个字符转换为大写，剩余部分转换为小写