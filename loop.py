#!/usr/bin/env python3

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

