#!/usr/bin/env python
# coding: utf-8

# In[1]:


d = {'a': 1, 'b': 2, 'c': 3}


# In[3]:


for key in d:
    print(key)


# In[4]:


for ch in 'ABC':
    print(ch)


# In[8]:


from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代


# In[9]:


isinstance([1,2,3], Iterable) # list是否可迭代


# In[10]:


isinstance(123, Iterable) # 整数是否可迭代


# In[11]:


for i, value in enumerate(['A','B','C']):
    print(i, value)


# In[12]:


for x,y in[(1,1),(2,4),(3,9)]:
    print(x,y)


# In[13]:


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple

from collections import Iterable

def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    if isinstance(L,Iterable) == True:
        min = L[0]
        max = L[0]
    for x in L:
        if x > max:
            max = x
        if x < min:
            min = x
    return (min,max)


# In[14]:


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


# In[ ]:




