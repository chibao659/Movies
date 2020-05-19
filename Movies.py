#!/usr/bin/env python
# coding: utf-8

# In[145]:


import numpy as np
import pandas as pd
from pandas import DataFrame,Series
from scipy import stats
import json

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic(u'matplotlib inline')


# In[150]:


movies_excel = pd.read_excel(r'C:\Users\chi_b\OneDrive\Desktop\Linked Class\CareerFoundry\movie_metadata.xlsx')


# In[151]:


print(movies_excel.columns)


# In[152]:


dframe = movies_excel.drop(['color'],axis=1)


# In[153]:


df = dframe.rename(columns={'Movie Category':'movie_cat'})

df.columns


# # Let's say block busters are ones with gross >= 100,000,000

# In[154]:


#Only Blockbuster Movies
block_b = df.gross >= 100000000 

block_b_movie = df[block_b]

block_b_movie


# In[155]:


block_b_movie.genres[0]


# In[157]:


block_b_movie['genres'].value_counts()


# In[164]:


#All the genres separately

genres_list = block_b_movie.genres.str.split('|',expand=True).stack().unique().tolist()
genres_list


# In[167]:


#Counts for Block Buster Movie Genres
Series({genre: block_b_movie.genres.str.contains(genre).sum() for genre in genres_list})


# In[ ]:




