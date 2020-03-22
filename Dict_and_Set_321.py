#!/usr/bin/env python
# coding: utf-8

# In[5]:


names = ['Michael', 'Bob', 'Tracy']
'Bob' in names


# In[6]:


'Brandy' in names


# In[7]:


# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
s


# In[8]:


# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
s


# In[13]:


# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
s


# In[14]:


# 通过remove(key)方法可以删除元素
s.remove(4)
s


# In[15]:


a = ['c', 'b', 'a']
a.sort()
a


# In[ ]:




