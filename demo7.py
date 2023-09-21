#字符串替换 replace()
s='hello,python'
print(s.replace('python','Java'))   #hello,Java
s1='hello,python,python,python'
print(s1.replace('python','Java',2))    #hello,Java,Java,python

#将列表或者元组中的字符串合并成一个字符串 join()
lst=['hello','java','python']
print('|'.join(lst))    #hello|java|python
print(' '.join(lst))    #hello java python

t=('hello','java','python')
print(' '.join(t))  #hello java python

print('*'.join('python'))   #p*y*t*h*o*n