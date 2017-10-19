
# coding: utf-8

# In[7]:


word = open('words','r')


# In[8]:


word


# In[9]:


wordlist = word.readlines()


# In[26]:


wordlist[:14]


# In[17]:


len(wordlist)


# In[20]:


'Aaron\n'.strip()


# In[21]:


'Aaron'.lower()


# In[29]:


wordclean = [word.strip().lower() for word in wordlist]


# In[30]:


wordclean[:10]


# In[31]:


wordunique = list(set(wordclean))


# In[32]:


wordunique


# In[33]:


wordunique.sort()


# In[34]:


wordunique


# In[46]:


wordclean = sorted(list(set([word.strip().lower() for word in open('words','r')])))


# In[47]:


wordclean


# In[48]:


sorted ('lives')


# In[49]:


sorted ('lives')==sorted('elvis')


# In[51]:


sorted('emin')


# In[53]:


'&'.join(['e', 'i', 'm', 'n'])


# In[55]:


import collections


# In[1]:


def signature(word):
    return ''.join(sorted(word))

