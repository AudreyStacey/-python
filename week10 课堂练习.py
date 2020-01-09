#!/usr/bin/env python
# coding: utf-8

# In[12]:


from selenium import webdriver
from pyquery import PyQuery as pq


# In[13]:


dr = webdriver.Chrome()


# In[15]:


dr.get("http://www.baidu.com")


# In[16]:


dr.find_elements_by_id('kw')


# In[17]:


dr.find_element_by_id('kw').send_keys('北京语言大学')


# In[18]:


dr.find_element_by_id('su').click()


# In[19]:


dr.find_element_by_id('content_left')


# In[20]:


s = dr.page_source


# In[21]:


print(s)


# In[22]:


doc = pq(s)


# In[23]:


lst = doc('#content_left .c-container h3 a em')


# In[24]:


print(lst)


# In[25]:


len(lst)


# In[26]:


lis = doc('#content_left .c-container h3 a').items()#.items会是一个生成器
print(type(lis))
for li in lis:
    print(li)
    


# In[27]:


dr.find_element_by_id('page')


# In[28]:


f = dr.page_source


# In[29]:


doc2 = pq(f)


# In[30]:


lst2 = doc2('#page a')


# In[31]:


print(lst2)


# In[32]:


lis2 = doc('#page a').items()#.items会是一个生成器
print(type(lis2))
for li in lis2:
    print(li)


# In[ ]:




