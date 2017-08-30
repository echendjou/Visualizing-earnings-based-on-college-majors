
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
recent_grads = pd.read_csv("recent-grads.csv")
print(recent_grads.iloc[:1])
print(recent_grads.head())
print(recent_grads.tail())
recent_grads = recent_grads.dropna()


# In[ ]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter')


# In[ ]:


recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')


# In[ ]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# In[ ]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')


# In[ ]:


recent_grads.plot(x='Men', y='Median', kind='scatter')


# In[ ]:


recent_grads.plot(x='Women', y='Median', kind='scatter')


# In[ ]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,12))
for r in range(1,5):
    ax = fig.add_subplot(4,1,r)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)


# In[ ]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,12))
for r in range(4,8):
    ax = fig.add_subplot(4,1,r-3)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)


# In[ ]:


from pandas.tools.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(6,6))


# In[ ]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# In[ ]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)

