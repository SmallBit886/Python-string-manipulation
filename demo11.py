#字符串的编码转换
'''编码：将字符串转换成二进制数据（bytes）'''
'''解码：将bytes类型转换成字符串类型'''
s='天涯共此时'
#编码
print(s.encode(encoding='GBK')) #b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1',一个中文占两个字节:[b表示二进制]
print(s.encode(encoding='UTF-8'))#b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'，一个中文占3个字节
#解码
#byte代表的就是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK')   #编码
#print(byte.decode(encoding='UTF-8'))    #解码（UnicodeDecodeError）
print(byte.decode(encoding='GBK'))  #天涯共此时