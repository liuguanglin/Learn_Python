# -*- coding: utf-8 -*-


str1 = 'hello,world!'
print('capitalize()==>', str1.capitalize())
print('title()==>', str1.title())
print('upper()==>', (str1.upper()))
print('lower()==>', (str1.lower()))
print('swapcase()==>', (str1.swapcase()))

print('ljust()==>\n', (str1.ljust(20)))
print('rjust()==>\n', (str1.rjust(20)))
print('center()==>\n', (str1.center(20)))
print('zfill()==>', str1.zfill(20))
print('find()==>', (str1.find("lo", 3, 5)))  # 若查找失败，则返回-1
print('rfind()==>', (str1.rfind("l")))
print('count()==>', (str1.count("o")))
print('index()==>', (str1.index("ll", 1, 4)))  # 若查找失败，则出现ValueError异常
print('replace()==>', (str1.replace("o", "O", 2)))
print('partition()==>', str1.partition(','))

print('startswith()==>', (str1.startswith("el", 1, 3)))  # 可匹配元组
print('endswith()==>', (str1.endswith("ll", 1, 4)))  # 左闭右开
print('isalnum()==>', (str1.isalnum()))  # 全为字母或数字
print('isalpha()==>', (str1[:3].isalpha()))
print('isdigital()==>', (str1.isdigit()))
print('islower()==>', (str1.islower()))
print('issupper()==>', (str1.isupper()))
print('istitle()==>', (str1.istitle()))
# print('cmp()==>', (cmp(str1, str1.upper())))
print('-'.join(str1))

str2 = 'I\'m fine,thank you. And you? '
print('strip==>', (str2.strip()))
print('strip(str)==>', (str2.strip('Iu? ')))
print('split()==>', str2.split(" "))

str3 = 'a\tb'
print(list(str3))
print(list(str3.expandtabs()))
