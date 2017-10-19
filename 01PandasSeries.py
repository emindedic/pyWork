
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


s = pd.Series([0,1,2,4,9,16,25],name='series')


# In[7]:


s


# In[8]:


s.values


# In[9]:


s.index


# In[10]:


s[2:4]


# In[11]:


s[0]


# In[12]:


s[3]


# In[13]:


pop2014 = pd.Series([10,99,3,95.5,92.4,84.8,84.5,78.9,74.3,72.8],
                   index=['Java','C','C++','Python','C#','PHP','JavaScript','Ruby','R','Matlab'])


# In[14]:


pop2014


# In[15]:


pop2014.index


# In[17]:


pop2014.values


# In[20]:


pop2014['C':'R']

