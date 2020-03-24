#!/usr/bin/env python
# coding: utf-8

# In[1]:


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


# In[2]:


[L[0],L[1],L[2]]


# In[4]:


L[0:3]


# In[6]:


L[0:-2]


# In[7]:


L[:3]


# In[8]:


L[:-2]


# In[9]:


L[-2:]


# In[10]:


L = list(range(100))


# In[11]:


L


# In[12]:


L[:10]


# In[13]:


L[-10:]


# In[14]:


L[11:20]


# In[16]:


L[:10:2]


# In[17]:


L[:]


# In[18]:


L[::5]


# In[19]:


(0,1,2,3,4,5)[:3]


# In[20]:


'ABCDEFG'[:3]


# In[21]:


'ABCDEFG'[::3]


# In[22]:


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    while s[:1] ==" ":
        s = s[1:]
    while s[-1:] ==" ":
        s = s[:-1]
    return s


# In[23]:


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


# In[ ]:




