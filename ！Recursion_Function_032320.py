#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 递归函数


# In[2]:


def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)


# In[3]:


fact(1)


# In[4]:


fact(5)
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120


# In[5]:


fact(1000)


# In[6]:


## 尾递归

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# In[7]:


fact_iter(5, 1)


# In[8]:


fact_iter(4, 5)


# In[9]:


fact_iter(3, 20)


# In[10]:


fact_iter(2, 60)


# In[11]:


fact_iter(1, 120)


# In[ ]:




