#!/usr/bin/env python
# coding: utf-8

# In[3]:


def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
list(r)


# In[4]:


list(map(str,[1,2,3,4,5,6,7,8,9]))


# In[7]:


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


# In[6]:


# reduce把结果继续和序列的下一个元素做累积计算，
from functools import reduce
def add(x,y):
    return x+y
reduce(add,[1,3,5,7,9])


# In[12]:


from functools import reduce
def fn(x,y):
    return x*10+y
reduce(fn,[1,3,5,7,9])


# In[13]:


# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


# In[ ]:




