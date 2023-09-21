#字符串内容对齐操作的方法
s='hello,python'
print(s.center(20,'*')) #居中对齐

print(s.ljust(20,'*'))  #左对齐

print(s.rjust(20,'*'))  #右对齐

print(s.zfill(20))  #右对齐（用0进行填充）

print(s.zfill(10))  #小于原字符串；返回原字符串

print('-1980'.zfill(8)) #-0001980
print('+1980'.zfill(8)) #+0001980