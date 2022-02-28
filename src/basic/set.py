#!/usr/bin/env python
# -*- coding: utf-8 -*-

fruits = {'apple', 'banana', 'orange'}
animals = set()
animals.add('goat')
animals.add(('horse', 'panda'))
animals.update(['tiger', 'deer'])
animals.update({'birds': 'crow'})
animals.update({'mustang', 'fox'})
animals.remove('tiger')
animals.discard('dragon')  # 若删除的元素不存在，也不报错
animals.pop()  # 随机删除一个元素
brands = {'apple', 'blackberry', 'fox', 'mustang'}
print('animals set: ', animals)

print('\n交集(fruits & brands)')
print('Brands named after fruit: ', fruits & brands)
print(fruits.intersection(brands))  # 可计算多个集合的交集
fruits_set = fruits.copy()
fruits_set.intersection_update(brands)  # 计算交集，覆盖原来的元素，相当于set &= set1 & ...
print(fruits_set)

print('\n并集(fruits | brands)')
print(fruits | brands)
print(fruits.union(brands))

print('\n差集(brands - fruits - animals)')
print(brands - fruits - animals)
print(brands.difference(fruits, animals))
brands_set = brands.copy()
brands_set.difference_update(fruits, animals)
print(brands_set)

print('\n对称差集(animals ^ brands)')
print(animals ^ brands)
print(animals.symmetric_difference(brands))
animals_set = animals.copy()
animals_set.symmetric_difference_update(brands)
print(animals_set)

print('\nisdisjoint()=>', fruits.isdisjoint(animals))  # 判断两集合是否不相交
print('issubset()=>', fruits_set.issubset(fruits), fruits_set <= fruits_set)
print('issuperset()=>', fruits.issuperset(fruits_set), fruits >= fruits_set)

print('\n类型转换')  # 由可迭代的对象转化为集合
print(set('hello'))
print(set([1, 2, 3]))
print(set((1, 2, 3)))
print(set({'k1': '1', 'k2': 'v2'}))
