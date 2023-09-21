#字符串的查询操作
s='hello,hello'
print(s.index('lo'))
print(s.find('lo'))
#
print(s.rindex('lo'))
print(s.rfind('lo'))
#
print(s.index('k')) #ValueError: substring not found
print(s.find('k'))  #-1