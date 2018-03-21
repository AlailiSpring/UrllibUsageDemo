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
*    匹配0次、1次或者多粗前面的原子
？   匹配0次或1次前面的原子
+    匹配1次或者多次前面的原子
{n}   前面的原子恰好出现n次
{n,m} 前面的原子至少出现n次，至多出现m次
'''
pattern3=".python.."
string3="sasasaspython234sa"
result3=re.search(pattern3,string3)
print(result3)

