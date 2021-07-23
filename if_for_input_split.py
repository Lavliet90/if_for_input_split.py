#!/usr/bin/env python
# coding: utf-8

# In[5]:


k=0
u=0
a=[int(i) for i in input().split()]
b=int(input())
for z in a:
    k+=1
    if z==b:
        u+=1
        print(k)
if u==0:
    print("Отсутствует")


# In[ ]:




