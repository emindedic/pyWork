
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


pop2014 = pd.Series([100,99.3,95.5,93.5,92.4,84.8,84.5,78.9,74.3,72.8],
                    index=['Java','C','C++','Python','C#','PHP','JavaScript','Ruby','R','Matlab'])


# In[4]:


pop2015 = pd.Series({'Java': 100,'C': 99.9,'C++': 99.4,'Python': 96.5,'C#': 91.3,
                     'R': 84.8,'PHP': 84.5,'JavaScript': 83.0,'Ruby': 76.2,'Matlab': 72.4})


# In[15]:


twoyears = pd.DataFrame ({'2014':pop2014, '2015':pop2015})


# In[6]:


twoyears


# In[7]:


twoyears.values


# In[8]:


twoyears.iloc[0:4]


# In[9]:


twoyears.loc['C':'Python']


# In[10]:


twoyears ['avg'] = 0.5*(twoyears['2014'] + twoyears['2015'])


# In[11]:


twoyears


# In[23]:


presidents = pd.DataFrame([{'name': 'Barack Obama', 'inauguration': 2009, 'birthyear': 1961},
                           {'name': 'George W.Bush', 'inauguration': 2001, 'birthyear': 1946},
                           {'name': 'Bill Clinton', 'birthyear': 1946, 'inauguration': 1993},
                           {'name': 'George H. Bush', 'inauguration':1989, 'birthyear': 1924}])


# In[24]:


presidents


# In[25]:


presidents_index = presidents.set_index('name')


# In[26]:


presidents_index


# In[27]:


presidents_index.loc['Bill Clinton']


# In[33]:


#Joins
presidents_fathers = pd.DataFrame([{'son': 'Barack Obama', 'father':'Barack Obama, Sr.'},
                    {'son': 'George W.Bush', 'father': 'George H.W.Bush'},
                    {'son': 'George H. Bush', 'father': 'Prescot Buch'}])


# In[34]:


presidents_fathers


# In[35]:


pd.merge(presidents,presidents_fathers, left_on='name',right_on='son')


# In[38]:


#delete some columns
pd.merge(presidents,presidents_fathers, left_on='name',right_on='son').drop('son',axis=1)

