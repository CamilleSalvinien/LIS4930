#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np 
import pandas as pd


# In[6]:


covidPath = "C:/Users/camil/OneDrive/Bureau/COVID19_03242020_ByCounty.xlsx"
covid = pd.read_excel(covidPath)


# In[7]:


covid.head()


# In[8]:


covid.describe()

