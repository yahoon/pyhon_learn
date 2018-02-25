#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 需求：
#  用户登录，最多三次机会

# 实现 一
n = 1
while n <= 3:
  name = input('>>> ')
  if name == 'root':
    print("welcome login", name)
    break
  else:
    print("wrong, please try again")
    n += 1


# 实现 二
'''
login = False
n = 1
while login != True and n <= 3:
  user = input("please input your user name: ")
  if user == "root":
    login = True
    print("login OK")
    break
  else:
    print("login fail time(s):", n)
  n = n + 1

if n == 4 and login == False:
  print("Error: 3 failures at max")
  exit 
'''
