
1. always use '.py' as suffix, or 'import' operation will fail

2. the first line:
#!/usr/bin/env python

3. the 2nd line to specify utf-8 code
#! -*- coding: utf-8 -*-
this is only needed in python 2.x and must be 2nd line, but it's not needed in python3.'

4. coding
ascii
unicode
utf-8



5. in python cmdline
>> dir()
>> help(input)

6. comment
# single line
"""
xx
xxx
xxx
"""
7. condition:
## if, else
if 1 == 1:
  print("hello")
else:
  print("world")
... 
hello

## if, elif, else
if 1 == 1:
   print("hello")
 elif 2 == 2:
   print("wolrd")
... 
hello

## pass
if 1 == 1:
  pass
else:
  print("world")

8. basic data type
## string
  'a'
  "a"
  '''a'''
  """a"""

string +/* operation
>>> n1 = 'a'
>>> n2 = 'b'
>>> n3 = n1 + n2
>>> n3
'ab'
>>> n3 * 2
'abab'

## number
  +, -, *, /, %, **, //
% 余数
// 商数
** 次方

>>> number = input("please input a number: ")
please input a number: 32
>>> inta = int(number)
>>> if inta % 2 == 0:
...   print(number + " is even")
... else:
...   print(number + " is odd")
... 
32 is even

9. loop
>>> count = 0
>>> while count < 10:
...   print(count)
...   count = count + 1
... 
0
1
2
3
4
5
6
7
8
9



OTHER:
1. print in 3.5
>>> print("ab" + "cd")
abcd
>>> print("ab", "cd")
ab cd

# be default, print will use ' ' as delimeter

2. time module
import time
print(time.time())

