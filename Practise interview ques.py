#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import datetime as dt





# In[4]:


data = {
 'Date': pd.date_range(start='2023-01-01', periods=180, freq='D'),
 'CompanyX_StockPrice': np.random.randint(50, 150, 180),
 'CompanyY_Sales': np.random.randint(20000, 50000, 180),
 'CompanyZ_StockPrice': np.random.randint(70, 200, 180)
}



# In[5]:


df = pd.DataFrame(data)


# In[6]:


df


# In[8]:


avgX=df["CompanyX_StockPrice"].mean() 


# In[9]:


# Avg stock price for company X over the last 6 months

avgX


# In[10]:


# Month with highest total sales for company Y

df["month"]=df["Date"].dt.month


# In[19]:


monthgrouped=df.groupby("month")["CompanyY_Sales"].sum()


# In[22]:


monthgrouped.sort_values(ascending=False)
#January has highest total sales


# In[23]:


df


# In[45]:


pricemax=df["CompanyZ_StockPrice"].max()
pricemin=df["CompanyZ_StockPrice"].min()
df.loc[df["CompanyZ_StockPrice"]==pricemax]



# In[46]:


df.loc[df["CompanyZ_StockPrice"]==pricemin]


# In[56]:


# percentage change in stock price from the previous day for company X
df.sort_values(by=["Date"])
df["CompanyX_StockPrice"].pct_change()
                               


# In[59]:


firstquarter=df.loc[(df["month"]>=1) &  (df["month"]<=3)]


# In[63]:


#Avg stock price of X & Z company for the first quarter 
qavgX=firstquarter["CompanyX_StockPrice"].mean()
qavgX


# In[64]:


qavgZ=firstquarter["CompanyZ_StockPrice"].mean()


# In[65]:


qavgZ

