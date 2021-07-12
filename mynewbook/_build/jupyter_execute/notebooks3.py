#!/usr/bin/env python
# coding: utf-8

# # This is yet another page in this great book

# - Pick 5 numbers between 1 and 10.
# - Create a list where 'I love ds' is in each element of the list, and the list has 5 elements.

# In[1]:


import numpy as np

x = np.random.uniform(1,10,5)


# In[2]:


mylist = ['I love ds' for x in range(0,5)]
mylist

