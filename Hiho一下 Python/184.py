#!/usr/bin/env python
# coding=utf-8
from operator import *
n,x = [int(i) for i in raw_input().split(' ')]
line = raw_input()
a = [int(j) for j in line.split(' ')]
a = sorted(a)
sum = sum(a)
for i in range(1 << n):
    ret = 0
    for j in range(len(a)):
        if (i>>j)&1 == True:
           ret += a[j]
    if ret >= x and sum >ret:
        sum = ret
if sum < x:sum = -1
print sum


    

