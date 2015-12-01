#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename:test.py

import random
import math

#随机生成用户30次答案，前三次分别是1，1，0
user_answer = [1, 1, 0]
for n in range(27):
    n = random.randint(0,1)
    user_answer.append(n)
    n = n + 1
print (user_answer)

#生成b的数组，前三位是0，0.5,0.75，后27位是0
b_para = [0, 0.5, 0.75]
for n in range(27):
    n = random.randint(0,0)
    b_para.append(n)
    n = n + 1

item_num = 3
count_num = 3

#牛顿迭代法
def nb(x):
    l1 = 0
    l2 = 0
    l3 = 0
    i = 0
    while i < count_num:
        z = math.exp(x - b_para[i])
        if user_answer[i] == 1:
            l1 = l1 + 1/(1 + z)
        else:
            l1 = l1 - z/(z + 1)
        l2 = l2 - z/((z + 1)**2)
        i = i + 1
        l3 = l1 / l2
    #print ('l3=',l3)
    return l3


#极大似然法
def mle(np):
    #计算1的求和
    sum1 = 0
    i = 0
    while i < count_num:
        sum1 = sum1 + user_answer[i]
        i = i + 1
        #print ('sum1=',sum1)
    x = math.log(sum1 / (count_num - sum1))
    #print ('x(math.log)=',x)
    y = 100
    while i <= 100:
        y = x - nb(x)
        if (abs(y - x) >= 10**(-5)):
            x = y
        else:
            break
        i = i + 1
    #print ('x=',x)
    return x

#选下一题的难度
while item_num < 30:
    b_para[item_num]=mle(1)
    print ('----b_para=',b_para[item_num])
    print ('user_answer=',user_answer[item_num])
    print('item_num',item_num)
    item_num = item_num + 1
    count_num = count_num + 1


