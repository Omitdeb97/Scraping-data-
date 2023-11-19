#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries 
from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"


# In[4]:


# getting reuest from url website
web = requests.get(url)


# In[6]:


# Reading html using beautifulSoup and request url.
soup = BeautifulSoup(web.text, 'html')


# In[7]:


print(soup)


# In[ ]:





# In[ ]:





# In[12]:


# Finding all the table
soup.find_all("table")


# In[ ]:





# In[35]:


# If we use .find_all then all the text data come out as list so we can indexing it and can find the require table information. 
table = soup.find_all('table')[1]


# In[ ]:





# In[ ]:





# In[36]:


# Finding the table heading using table variable which was selecteing indexing. 
title = table.find_all('th')


# In[37]:


print(title)


# In[ ]:





# In[47]:


# Doing list compriansion 

world_list_title = [heading.text.strip() for heading in title]
print(world_list_title)


# In[ ]:





# In[ ]:


# Using pandas laibrary to structure data 


# In[50]:


import pandas as pd
dt = pd.DataFrame(columns= world_list_title)


# In[51]:


dt


# In[ ]:





# In[52]:


column = table.find_all('tr')


# In[53]:


column


# In[ ]:





# In[56]:


for row in column[1:]:
    row_data = row.find_all('td')
    invidudal_data = [data.text.strip() for data in row_data]
   # print(invidudal_data)
    
    length = len(dt)
    dt.loc[length] = invidudal_data
    
    


# In[57]:


dt


# In[ ]:





# In[59]:


# Exporting this data into csv file
dt.to_csv(r'C:\Users\amitd\OneDrive\Documents\Data analysing\python tutorial\scraping website\companies.csv', index=False)


# In[ ]:





# In[ ]:




