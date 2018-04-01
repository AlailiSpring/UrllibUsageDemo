#正则表达式的使用
import re
pattern="yue"
string="http://yum.iqianyue.com"
result=re.search(pattern,string)
print(result)

'''通用字符作为原子
\w 匹配任意一个字母、数字或下划线
\d 匹配任意一个十进制数
\s 匹配任意一个空白字符
以上的通用字符改为大写，那么都是取反的意思
'''
pattern1="\w\dpython\w"
string1="abcdfe12pythonsa5"
result1=re.search(pattern1,string1)
print(result1)

'''原子表匹配
使用原子表，可以定义一组地位平等的原子
【abc】定义了3个平等原则的元素a b c
[abc]xyz 对应的源字符串是"acdxyz"，那么就可以匹配出acxyz
'''
pattern2="\w\dpython\w[abc]"
result2=re.search(pattern2,string1)
print(result2)

'''元字符
.    匹配除换行符以外的任意字符
^    匹配字符串的开始位置
$    匹配字符串的结束位置
*    匹配0次、1次或者多次前面的原子
？   匹配0次或1次前面的原子
+    匹配1次或者多次前面的原子
{n}   前面的原子恰好出现n次
{n,m} 前面的原子至少出现n次，至多出现m次
'''
pattern3=".python.."
string3="sasasaspython234sa"
result3=re.search(pattern3,string3)
print(result3)

'''
模式选择符
|   匹配任意一个,有可能是匹配到第一个符合条件的就结束、
()  被扩起来的作为一个整体进行匹配
'''
pattern4='python|php'
string4='abcsdpython345php_123'
result4=re.search(pattern4,string)
print(result4)

pattern5='(cd){3}'
pattern6='cd{1,}'
string5='1290cdcdcd_909no'
result5_1=re.search(pattern5,string5)
result5_2=re.search(pattern6,string5)
print(result5_1)
print(result5_2)


'''
模式修正，可以实现匹配结果的调整
I   忽略大小写
M   多行匹配
L   本地化识别匹配
U   根据Unicode字符及解析字符
S   匹配包括换行符，"." 匹配的字符包括换行符，即可以匹配任意字符
'''

pattern7="python"#小写的匹配
pattern8="Python"#大写的匹配
string7="090python_112mm"
result6=re.search(pattern8,string7,re.I)#忽略了大小写
result6_1=re.search(pattern8,string7)
print(result6)
print(result6_1)



'''
贪婪模式 尽可能多的进行匹配
懒惰模式 尽可能少的进行匹配
'''
pattern_greed="p.*y"#贪婪模式写法
pattern_lazy="p.*?y"#懒惰模式写法
string10="abcdefapython_123py"
result_greed=re.search(pattern_greed,string10)
result_lazy=re.search(pattern_lazy,string10)
print(result_greed)
print(result_lazy)


'''
正则表达式涉及到的相应的函数
re.match(pattern,string,flag) match函数匹配的pattern必须是串的开始位置
re.search(pattern,string,flag)  是全文匹配对需要进行匹配的格式的位置没有要求
'''

#例子略

'''
假如我们想要匹配出一个串中所有符合条件的字符，我们可以采用如下的策略进行
1. re.compile()对正则表达式进行预编译
2. findAll()根据正则表达式从源字符串中将匹配结果全部找出
'''
string_findAll='hellomypythonispythonmethodpython123'
pattern_findall=re.compile(".python.")
result_findall=pattern_findall.findall(string_findAll)
print(result_findall)

'''
替换函数
re.sub(pattern,rep,string,max)
下面是参数的说明
pattern 正则表达式
rep 要替换成的字符串
string 源字符串
max 可选项，最多替换的次数，忽略不写，代表根据符合的模式全部替换
'''
string_rep='hellomypythonisa123goodpythonwow'
pattern_rep='.python'
result_rep=re.sub(pattern_rep,'php',string_rep)
result_rep_2=re.sub(pattern_rep,'php',string_rep,1)
print(result_rep)
print(result_rep_2)













