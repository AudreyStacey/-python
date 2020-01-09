#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 元组可变参数示例
def printinfo( arg1, *vartuple ):
   #"打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)


# In[6]:


printinfo(2, 3,4,5,6,7)


# In[7]:


# 字典可变参数示例
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)


# In[8]:


printinfo(1, a=2,b=3)


# In[10]:


#  传不可变对象实例
def ChangeInt( a ):
    a = 10
b = 2
ChangeInt(b)
print( b )


# In[11]:


# 传可变对象实例
# 可写函数说明
def changeme( mylist ):
   #"修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return


# In[14]:


mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)


# In[15]:


#Lambda示例
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))


# In[21]:


#Lambda示例
multiply= lambda x,y: x*y
squre= lambda x:x*x
print(multiply(2,3))
print(squre(4))


# In[23]:


def multiply_and_square(x,y):
    return (x*y,x*x,y*y)


# In[25]:


ret = multiply_and_square(1,2)


# In[27]:


ret


# In[29]:


ret1, ret2,ret3=multiply_and_square(1,2)


# In[31]:


ret1


# In[33]:


ret2


# In[36]:


import copy


# In[37]:


import sys


# In[39]:


print(sys.path)


# In[41]:


dir(copy)


# In[43]:


import numpy as np


# In[45]:


np.array


# In[47]:


import math


# In[48]:


math.pi


# math.sin

# In[49]:


math.sin


# In[51]:


from random import randint


# In[53]:


import json.decoder


# In[54]:


from json import decoder


# In[55]:


dir(decoder)


# In[57]:


import json


# In[58]:


dir(json)


# In[60]:


json.encoder


# In[61]:


json.loads


# In[63]:


import os


# In[65]:


dir(os)


# In[66]:


print(os.getcwd())


# In[67]:


import sound


# In[68]:


import sound.effects.echo


# In[69]:


from sound.effects import echo


# In[2]:


import geometry


# In[50]:


import geometry


# In[55]:



import geometry.area.rectangle


# In[56]:


rectangle_area()
rectangle_area(3,4)


# In[58]:


from geometry.area.circle import circle_area
circle_area(3)

from geometry.area.rectangle import rectangle_area
rectangle_area(3,2)

from geometry.area.square import square_area
square_area(5)

from geometry.area.triangles import triangles_area
triangles_area(3,4)

print("\n")

from geometry.surface_area.cube import cube_sur
cube_sur(3)

from geometry.surface_area.cuboid import cuboid_sur
cuboid_sur(3,4,5)

from geometry.surface_area.cylinder import cylinder_sur
cylinder_sur(3,5)

from geometry.surface_area.sphere import sphere_sur
sphere_sur(3)

print("\n")

from geometry.volume.cube import cube_vol
cube_vol(3)

from geometry.volume.cuboid import cuboid_vol
cuboid_vol(3,6,8)

from geometry.volume.cylinder import cylinder_vol
cylinder_vol(3,10)

from geometry.volume.sphere import sphere_vol
sphere_vol(7)


# In[ ]:




