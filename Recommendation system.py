#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)
df.head()


# In[4]:


movie_titles = pd.read_csv("Movie_Id_Titles.txt")
movie_titles.head()


# In[5]:


df = pd.merge(df,movie_titles,on='item_id')
df.head()


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


df.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[8]:


df.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[9]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()


# In[12]:


moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()


# In[14]:


ratings['num of ratings']=pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()


# In[15]:


moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()


# In[16]:


ratings.sort_values('num of ratings',ascending=False).head(10)


# In[17]:


ratings.head()


# In[18]:


starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
starwars_user_ratings.head()


# In[19]:


similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)


# In[20]:


corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()


# In[21]:


corr_starwars.sort_values('Correlation',ascending=False).head(10)


# In[22]:


corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()


# In[23]:


corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[24]:


corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[ ]:




