#!/usr/bin/env python
# coding: utf-8

# 
# # Project: No-show appointments Dataset
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# > This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row.
# 
# >-ScheduledDay’ tells us on what day the patient set up their appointment.
# 
# >-‘Neighborhood’ indicates the location of the hospital.
# 
# >-‘Scholarship’ indicates whether or not the patient is enrolled in Brasilian welfare program Bolsa Família.
# 
# # analysis questions (Data gathering)
# 
# > what is the efective factors of the patient show ?
# 
# > what is the relation between the age and the gender ?
# 
# > is all of the people who receive a text massage attend ?
# 
# 
# 
# # the encoding of the last column: it says ‘No’ if the patient showed up to their appointment, and ‘Yes’ if they did not show up.
# 
# 
# > we will understand what are the factors affecting on the patient descion to attend the examination or not

# In[52]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


get_ipython().run_line_magic('matplotlib', 'inline')


# In[53]:


from pandas.plotting import radviz


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties

# In[3]:


df_noshow =pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df_noshow.head()



# In[4]:


df_noshow.tail()


# In[5]:


df_noshow.info()


# ## There Are No Missing Values in The Data

# In[6]:


df_noshow.describe()


# In[7]:


df_noshow.shape


# In[8]:


df_noshow.dtypes


# ### Data Cleaning (Replace this with more specific notes!)

# # Droping The Unnessery Columns 

# In[9]:


df_noshow.drop(['PatientId','AppointmentID','ScheduledDay',] , axis = 1 , inplace = True)
df_noshow.head()


# # we fond that "No-show" column need to be reanamed 

# In[10]:


df_noshow.rename(columns ={'No-show' : 'No_show'},inplace = True)
df_noshow.head()


# In[11]:


df_noshow.info()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# # General Visualization to the Data  
# 
# 

# In[12]:


df_noshow.hist(figsize= (15,12));


# In[71]:


attend = df_noshow.No_show == 'No'
nonattend = df_noshow.No_show == 'Yes'


# In[44]:


attend.count()


# In[45]:


nonattend


# In[46]:


attend


# ### the relation between the gender and the attendance

# In[68]:


df_noshow.Gender[attend]


# In[67]:


df_noshow.Gender[attend].value_counts().hist(label = 'attend')
df_noshow.Gender[nonattend].value_counts().hist(label = 'nonattend')
plt.legend()
plt.tight_layout()
plt.xlabel('Gender')  
plt.ylabel('patients') 


# In[69]:


df_noshow.groupby('Gender').No_show.value_counts().plot(kind = 'box');
plt.legend()
plt.xlabel('Gender')  
plt.ylabel('patients');


# > we find that the gender does not effect the attendance  

# In[28]:


df_noshow.groupby('Gender').No_show.value_counts()


# In[52]:


plt.figure();


# In[73]:


plt.figure();
df_noshow.Gender[attend].value_counts().plot( )
df_noshow.Gender[nonattend].value_counts().plot( )
plt.legend()
plt.xlabel('Gender')  
plt.ylabel('patients');             


# ### we find that the gender doesn't affect on the relation 

# # the relation between the scholarship and the attendance
# 

# In[55]:


print(df_noshow.Scholarship[attend].value_counts())
print(df_noshow.Scholarship[nonattend].value_counts())


# In[74]:


df_noshow.groupby('Scholarship').No_show.value_counts();


# In[19]:


df_noshow.Scholarship[attend].hist(alpha = 0.5 , label = 'attend' )
df_noshow.Scholarship[nonattend].hist(alpha = 0.5 , label = 'nonattend' )
plt.legend()
plt.xlabel('Scholarship')  
plt.ylabel('patients');     


# > there is no relation between the scolarship and the attendance 
# 

# # the relation between the SMS_received and the attendance

# In[69]:


print(df_noshow.SMS_received[attend].value_counts())
print(df_noshow.SMS_received[nonattend].value_counts())


# In[70]:


df_noshow.groupby('SMS_received').No_show.value_counts().plot();
plt.title("SMS_received factor")
plt.xlabel("pateints")
plt.ylabel("SMS_received")


# In[20]:


plt.figure(figsize=[14.70,8.27])
df_noshow.SMS_received[attend].hist(alpha = 0.5 , label = 'attend' )
df_noshow.SMS_received[nonattend].hist(alpha = 0.5 , label = 'nonattend' )
plt.legend()
plt.xlabel('SMS_received')  
plt.ylabel('patients'); 


# > there is no relation between the SMS_received and the attendace

# # the relation between the Diabetes and the attendance 

# In[72]:


df_noshow.groupby('Diabetes').No_show.value_counts().plot();
plt.title("Diabetes factor")
plt.xlabel("pateints")
plt.ylabel("Diabetes")


# In[21]:


plt.figure(figsize=[14.70,8.27])
df_noshow.Diabetes[attend].hist(alpha = 0.5 , label = 'attend' )
df_noshow.Diabetes[nonattend].hist(alpha = 0.5 , label = 'nonattend' )
plt.xlabel('Diabetes')  
plt.ylabel('patients');


# > there is no relation with the Diabetes

# # the relation between the Handcap and the attendance 

# In[75]:


df_noshow.groupby('Handcap').No_show.value_counts().plot();
plt.title("Handcap factor")
plt.xlabel("pateints")
plt.ylabel("Handcap")


# In[80]:


plt.figure(figsize=[14.70,8.27])
df_noshow.Handcap[attend].hist(alpha = 0.5 , label = 'attend' )
df_noshow.Handcap[nonattend].hist(alpha = 0.5 , label = 'nonattend' )
plt.legend()
plt.xlabel('Handcap')  
plt.ylabel('patients');   


# > there is no relation with the Handcap 

# # the relation between the Age and the attendance 

# In[83]:


df_noshow.groupby('Age').No_show.value_counts().plot();


# In[80]:


plt.figure(figsize=[14.70,8.27])
df_noshow.Age[attend].hist(alpha = 0.5 , label = 'attend' )
df_noshow.Age[nonattend].hist(alpha = 0.5 , label = 'nonattend' )
plt.legend()
plt.xlabel('Ages')  
plt.ylabel('patients');   


# > the range of 0 to 10 yaers old attends more than the other ranges 
# 

# > we see that when the patient becomes older, he attends less than before 

# # the relation between the Neighbourhood and the attendance 

# In[82]:


df_noshow.groupby('Neighbourhood').No_show.value_counts().plot();
plt.title("Neighbourhood factor")
plt.xlabel("pateints")
plt.ylabel("Neighbourhood")
plt.xticks(rotation=45)
plt.yticks(rotation=90);


# In[ ]:


plt.figure(figsize=[14.70,8.27])
df_noshow.Neighbourhood[attend].hist(alpha = 0.5 , label = 'attend' )
df_noshow.Neighbourhood[nonattend].hist(alpha = 0.5 , label = 'nonattend' )
plt.legend()
plt.xlabel('Neighbourhood')  
plt.ylabel('patients');   


# > there is a strong relation between the Neighbourhood and the attendance 

# <a id='conclusions'></a>
# ## Conclusions
# > we find unnessiry columns so we earse the (drop)
# 
# > we find that there are no missing values 
# 
# > we find that the name of " No-show " column need to fix 
# 
# > we make a relation between every factor and the attendance 
# 
# > we made the data frames "attend " and "nonattend" to discribe the statue of the patient with the certien factors
# 
# > **Tip**: Finally, we find that there is no effictive factor for the attendance except the Age and the Neighbourhood . as we see the older people are the less people to attend.
# 
# > **Tip**: As strange result we find that the people who didn't reacive an SMS attended more than the people did .

# ## Limitations
# 
# > we can not find a clear relashion between the gender and the attendance 
# 
# > the columns of the gender and the No_show was boolean 
# 
# > the boolean columns faces a problem to be visualized 

# In[75]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




