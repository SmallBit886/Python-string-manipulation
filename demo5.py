#字符串的分割
#split()
s='hello world Python'
lst=s.split()               #['hello', 'world', 'Python']
print(lst)
s1='hello|world|Python'
print(s1.split())           #['hello|world|Python']
print(s1.split(sep='|'))    #['hello', 'world', 'Python']
print(s1.split(sep='|',maxsplit=1)) #['hello', 'world|Python']
#rsplit()从右侧开始劈分
print('--------------------------------')
print(s.rsplit())           #['hello', 'world', 'Python']
print(s1.rsplit(sep='|'))   #['hello', 'world', 'Python']
print(s1.rsplit(sep='|',maxsplit=1))#['hello|world', 'Python']



