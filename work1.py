
# coding: utf-8

# In[2]:


capitals = {'USA': 'Washington', 'France':'Paris', 'Italy':'Rome'}


# In[3]:


print (capitals)


# In[4]:


capitals['Italy']


# In[5]:


'Paris' in capitals


# In[6]:


morecapitas = {'Germany':'Berlin','UK':'London'}


# In[9]:


capitals.update(morecapitas)


# In[10]:


capitals


# In[11]:


del capitals('USA')


# In[12]:


del capitals['USA']


# In[13]:


capitals


# In[15]:


for key in capitals:
    print (key,capitals[key])


# In[16]:


for key in capitals.keys():
    print (key)


# In[18]:


for value in capitals.values():
    print (value)


# In[20]:


for key,values in capitals.items():
    print key,value

