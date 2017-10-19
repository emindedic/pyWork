
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as pp


# In[10]:


a = np.array([1,2,3,4,5])
a


# In[12]:


a.dtype


# In[13]:


a = np.array([1,2,3,4,5],dtype=np.float64)


# In[14]:


a


# In[15]:


a.ndim, a.shape, a.size


# In[17]:


b = np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype=np.float64)


# In[18]:


b


# In[20]:


b.dtype


# In[22]:


np.zeros((3,3),'d')


# In[23]:


np.empty((4,4),'d')


# In[24]:


np.arange(0,10,2)


# In[25]:


np.random.standard_normal((2,6))

