
# coding: utf-8

# In[1]:


squares =[]

for i in range(10):
    squares.append(i**2)


# In[2]:


squares


# In[3]:


squares[i**2 for i in range(30) if i % 3==0] 


# In[5]:


squares2 = [i**2 for i in range(30) if i % 3==0] 


# In[6]:


squares2


# In[9]:


squares_dict = {i: i**2 for i in range(30) if i % 3==0}


# In[10]:


squares_dict


# In[11]:


capitals = {'USA': 'Washington', 'France':'Paris', 'Italy':'Rome'}


# In[12]:


capitals_bycapital = {capitals[key]: key for key in capitals}


# In[13]:


capitals


# In[14]:


capitals_bycapital


# In[17]:


capitals_bystate = {capitals[key]: key for key in capitals}


# In[18]:


capitals_bystate


# In[23]:


niz = [i**2 for i in range (10)]


# In[24]:


niz


# In[25]:


sum(i**2 for i in range (10))

