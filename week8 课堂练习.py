#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
url = 'http://ip138.com/ips138.asp?ip='
try:
    r = requests.get(url+'192.168.255.2')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('爬取失败')


# In[3]:


from pyquery import PyQuery as pq

import requests
url = 'http://www.blcu.edu.cn'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')


# In[4]:


type(r)


# In[5]:


html_text = r.text


# In[6]:


doc = pq(html_text)


# In[7]:


doc('head').text()


# In[8]:


doc('body').text()


# In[10]:


lis = doc('.zcontent li')

for li in lis:
    print(pq(li).find('a').text())


# In[ ]:




