#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Read in csv from fetched data
issues = pd.read_csv('issues.csv',header=0)


# In[3]:


issues.head()


# In[4]:


issues.dtypes


# In[7]:


#convert object type for dates to datetime for two date columns
issues['Closed at'] = pd.to_datetime(issues['Closed at'])
issues['Created at'] = pd.to_datetime(issues['Created at'])


# In[8]:


issues.dtypes


# In[9]:


#convert all object type to strings, integers, or boolean types
issues_converted = issues.convert_dtypes()


# In[11]:


issues_converted.dtypes


# In[12]:


#Slice of top 5 tuples
issues_converted.head()


# In[13]:


from pandas.api.types import CategoricalDtype


# In[14]:


#convert State attribute to categorical
issues_converted.State = issues_converted.State.astype('category')


# In[15]:


#convert State category to numeric ((0= closed, 1= open)
issues_converted.State = issues_converted.State.cat.codes


# In[16]:


issues_converted.head()


# In[17]:


#Frequency of Closed (0) vs Open (1) State of issues
issues_converted['State'].value_counts().plot(kind='bar')
plt.title('Closed vs Open Issues')
plt.xlabel('State')
plt.ylabel('Count')
plt.show()


# In[18]:


#Strip plot of # comments vs closed or open state of issue
sns.stripplot(data=issues_converted, x='State', y = '# of Comments')
plt.title('# of Comments vs. State')
plt.show()


# In[19]:


#Correlation Heatmap for the numeric attributes
plt.figure(figsize=(16,10))
sns.heatmap(issues_converted.corr(), annot=True)
plt.show()


# In[21]:


fig,ax = plt.subplots(1,1)
a = np.array(issues_converted['Created at'])
ax.hist(a, bins = 12) #[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
ax.set_title("Issues Over Project Lifetime")
#ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('year')
ax.set_ylabel('no. of issues')
plt.show()


# In[22]:


#Plotting counts of issue State (closed (0) or open (1)) against project lifetime
issues_converted.hist(column='Created at', by='State', bins=12, sharey=True)
# plt.title('Issues By State over Project Lifetime')
plt.show()


# In[23]
#Plotting counts of State (closed (0) or open (1)) against # of Labels
issues_converted.hist(column='# of Labels', by='State', sharey=True, sharex=True)
plt.show()


