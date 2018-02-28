#!/usr/bin/env python
#! -*- coding: utf-8 -*-

# in this doc, we will learn int type's basic methods

# int('str'), convert to int
num_str = '123'
num = int(num_str) # here num_str cannot be '123a' or 'a123' or '1a23'

print(num)
print(type(num))
print(type(num), num)

print("-----------------")

print(num_str)
print(type(num_str))
print(type(num_str), num_str)

# todo: int(xxx, base=)



print("###########################")

# int.bit_length()
# print the length binary bits
# print: 最少用多少bit位来表示这个数字
# 1 -> 1, 2 -> 2, 3 -> 2, 4 -> 3
a = 5
print(a, a.bit_length())

# Below is an example for failure:
#
#     >>> a = 10
#     >>> a.bit_length()
#     4
#     >>> 10.bit_length()
#       File "<stdin>", line 1
#         10.bit_length()
#                     ^
#     SyntaxError: invalid syntax
#
# here, 10 is a constant, not an instance of int. So 10.bit_length() fails but a.bit_length() works


