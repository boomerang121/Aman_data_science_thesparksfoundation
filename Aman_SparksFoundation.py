#!/usr/bin/env python
# coding: utf-8

# ### Sparks Foundation Internship Data science
# 
# # Aman Choudhary
# 
# #Exploratory Data Analysis - Retail
#  
# Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# 
# As a business manager, try to find out the weak areas where you can work to make more profit
# 
# What all business problems you can derive by exploring the data?
# 
# I used Python
# 
# Dataset: https://bit.ly/3i4rbWl

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:



df = pd.read_csv("store_sparks.csv")
df.head()


# In[3]:


df.shape


# In[4]:


df.size


# In[5]:


df.describe()


# In[6]:


fig,axes = plt.subplots(1,1,figsize=(20,10))
sns.heatmap(df.corr())
plt.show()


# In[7]:


sns.countplot(df["Category"])


# In[8]:


sns.pairplot(data = df)


# In[9]:


fig,axes = plt.subplots(1,1,figsize=(20,10))
sns.countplot(df["Quantity"],hue = df["Region"])
plt.show()


# In[11]:


get_ipython().system(' pip install pandas==0.25')


# In[12]:


get_ipython().system(' pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip')


# In[ ]:


import pandas as pd
from pandas_profiling import ProfileReport


# In[15]:


df=pd.read_csv('store_sparks.csv')
 


# In[16]:


profile = ProfileReport(df, title="Pandas Profiling Report")
profile


# In[ ]:




