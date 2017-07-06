
# coding: utf-8

# In[1]:


cd tops5_p25_phrasemachine


# In[2]:


import csv
import pandas as pd
import re #regular expression


# In[3]:


df_tag5 = pd.read_csv('PM_top5_p25_tags.csv', header=None, names=list('abcdefgh'))


# In[4]:


df_tag5.head(10)


# In[55]:


cd ../../expanded_audits


# In[56]:


df_enviro = pd.read_csv('environment.csv')


# In[57]:


df_enviro.head(10)


# In[60]:


df_tag5['b'] = df_tag5['b'].str.replace(r'\[\(', '')


# In[61]:


df2_tag5 =  df_tag5.drop(df_tag5.columns[[2, 3, 4, 5, 6, 7]], axis=1)


# In[62]:


df2_tag5.columns = ['url', 'topic_id']


# In[63]:


df2_tag5.head(10)


# In[64]:


df_first_topic = df2_tag5.loc[df2_tag5['topic_id'] == '0']
df_second_topic = df2_tag5.loc[df2_tag5['topic_id'] == '1']
df_third_topic = df2_tag5.loc[df2_tag5['topic_id'] == '2']
df_fourth_topic = df2_tag5.loc[df2_tag5['topic_id'] == '3']
df_fifth_topic = df2_tag5.loc[df2_tag5['topic_id'] == '4']


# In[65]:


df_first_topic.head(10)


# In[66]:


df_first_topic.shape


# In[67]:


df_first = pd.merge(df_first_topic, df_enviro, left_index = True, right_index = True , indicator = True)
df_second = pd.merge(df_second_topic, df_enviro, left_index = True, right_index = True , indicator = True)
df_third = pd.merge(df_third_topic, df_enviro, left_index = True, right_index = True , indicator = True)
df_fourth = pd.merge(df_fourth_topic, df_enviro, left_index = True, right_index = True , indicator = True)
df_fifth = pd.merge(df_fifth_topic, df_enviro, left_index = True, right_index = True , indicator = True)


# In[68]:


df_first.head(10)


# In[69]:


df_first.loc[(df_first['url_x'] != df_first['url_y'])]
df_second.loc[(df_second['url_x'] != df_second['url_y'])]
df_third.loc[(df_third['url_x'] != df_third['url_y'])]
df_fourth.loc[(df_fourth['url_x'] != df_fourth['url_y'])]
df_fifth.loc[(df_fifth['url_x'] != df_fifth['url_y'])]


# In[70]:


df_first =  df_first.drop(df_first.columns[[1, 2, 4]], axis=1)
df_second =  df_second.drop(df_second.columns[[1, 2, 4]], axis=1)
df_third =  df_third.drop(df_third.columns[[1, 2, 4]], axis=1)
df_fourth =  df_fourth.drop(df_fourth.columns[[1, 2, 4]], axis=1)
df_fifth =  df_fifth.drop(df_fifth.columns[[1, 2, 4]], axis=1)


# In[71]:


df_first.columns = ['url', 'text']
df_second.columns = ['url', 'text']
df_third.columns = ['url', 'text']
df_fourth.columns = ['url', 'text']
df_fifth.columns = ['url', 'text']


# In[72]:


df_first.shape


# In[73]:


cd ../enviro_experiments


# In[74]:


df_first.to_csv('first_top_PM.csv', index = False)
df_second.to_csv('second_top_PM.csv', index = False)
df_third.to_csv('third_top_PM.csv', index = False)
df_fourth.to_csv('fourth_top_PM.csv', index = False)
df_fifth.to_csv('fifth_top_PM.csv', index = False)


# In[ ]:




