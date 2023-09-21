#字符串判断的相关方法
'''判断字符串是不是合法的标识符[字母，数字，下划线]'''
s='hello,python'
print('1.',s.isidentifier())        #False
print('2.','hello'.isidentifier())  #True
print('3.','张三_'.isidentifier())    #True
print('4.','张三_123'.isidentifier()) #True
'''是否全部由空白字符组成'''
print('5.','\t'.isspace())  #True 是空白字符（回车，换行，水平制表符）
'''是否全部由字母组成'''
print('6.','abcdef'.isalpha())  #True
print('7.','张三'.isalpha())  #True
print('8.','张三1'.isalpha()) #False
'''是否全部由十进制数组成'''
print('9.','123'.isdecimal())   #True
print('10.','123四'.isdecimal())#False
print('11.','Ⅰ Ⅱ Ⅲ'.isdecimal())#False
'''是否全部由数字组成'''
print('12.','123'.isnumeric())#True
print('13.','123四'.isnumeric())#True
print('14.','ⅠⅡⅢ'.isnumeric())#True
'''是否全部由字母和数字组成'''
print('16.','张三123'.isalnum())#True
print('17.','a123'.isalnum())#True
print('18.','abc!'.isalnum())#False
