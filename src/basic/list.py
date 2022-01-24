#!/usr/bin/env python
# -*- coding: utf-8 -*-


lst1 = [11, 22, 33, 44]
lst2 = ['ok', 'hi', 'Candy', 'Zoo']

lst1.append(99)
lst1.extend(lst2)
lst1.remove(11)
print("lst1.pop(-2)==>", lst1.pop(-2))
lst1.reverse()
print("lst1==>", lst1)

lst2.insert(2, 'OK')
print("\ncount('ok')==>", lst2.count('ok'))
lst2.sort()
print("lst2==>", lst2)
print("index('hi')==>", lst2.index('hi'))
del lst2[-2]
print("lst2==>", lst2)
# sorted(lst1)    # 不同数据类型无法排序

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)
print('-' * 20)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

print('-' * 20)
nums = [5, 10, 3, 20, 35]
nums.sort(key=lambda n: (0, n) if n % 2 else (1, n))    # 奇数往前排
print(nums)
