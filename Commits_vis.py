#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

commits = pd.read_csv('commits.csv',header=0)

import matplotlib.pyplot as plt
import seaborn as sns

commits.head()

commits['Date'] = pd.to_datetime(commits['Date'])

commits.dtypes


from matplotlib import colors
from matplotlib.ticker import PercentFormatter


#Plot frequency of commits over the project lifetime
fig,ax = plt.subplots(1,1)
a = np.array(commits['Date'])
ax.hist(a, bins = 12)
ax.set_title("Commits Over Project Life")
#ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('year')
ax.set_ylabel('no. of commits')
plt.show()


# Plot commits in the first year of project
fig,ax = plt.subplots(1,1)
b = commits.iloc[2211:2835, 0]
ax.hist(b, bins = 12)
ax.set_title("Commits Over First Year")
ax.set_xlabel('date')
ax.set_ylabel('no. of commits')
plt.show()


#Plot YTD commits
fig,ax = plt.subplots(1,1)
b = commits.iloc[0:78, 0]
ax.hist(b, bins = 12)
ax.set_title("Commits Over Most Recent Year")
ax.set_xlabel('date')
ax.set_ylabel('no. of commits')
plt.show()

