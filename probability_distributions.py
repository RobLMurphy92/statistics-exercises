#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


# Assumptions:
# 
# Two potential outcome per trial
# 
# Probability of success is same across all trials
# 
# Each trial is independent
# 
# fixed number of observations

# ### 1.)A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.
# 
# 

# In[3]:


λ = 2 #cars at noon


# a.) What is the probability that no cars drive up in the noon hour?

# In[12]:


stats.poisson(λ).pmf(12)


# b.) What is the probability that 3 or more cars come through the drive through?

# In[6]:


stats.poisson(λ).sf(2)


# c.) How likely is it that the drive through gets at least 1 car? means one or more

# In[14]:


stats.poisson(λ).sf(0)


# ### 2.)Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:
# 

# - a.) What grade point average is required to be in the top 5% of the graduating class?

# In[16]:


#top 15 %
mean = 3
stddev = .3
stats.norm(mean,stddev).isf(.05)


# - b.) What GPA constitutes the bottom 15% of the class?

# In[27]:


mean = 3
stddev = .3
stats.norm(mean,stddev).isf(.85)


# - c.)An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

# In[21]:


mean = 3
stddev = .3
stats.norm(mean,stddev).isf(.70)


# In[31]:


stats.norm(mean,stddev).isf(.80)


# In[33]:


# They would qualify! 


# - d.) If I have a GPA of 3.5, what percentile am I in?

# In[39]:


#They are in 95 percentile
stats.norm(mean,stddev).isf(.05)


# ### 3.)A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs. 
# 

# - a.)How likely is it that this many people or more click through?

# In[43]:


#trials 
ct = 97
n_trials = 4326
p = .02

clicks = stats.binom(n_trials, p)
clicks


# In[45]:


likely =clicks.sf(ct-1)
likely


# ### 4.)You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.
# 

# - a.) What is the probability that at least one of your first 60 answers is correct?

# In[47]:


h_trials = 100
p =0.01
chance = stats.binom(h_trials,p).cdf(60)
chance


# ### 5.)The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. 
# 

# - a.) How likely is it that the break area gets cleaned up each day? 

# In[70]:


number_of_students = (.90 * (3*22))
p = 0.03


# In[71]:


number_of_students


# In[72]:


cd_trials = stats.binom(number_of_students, p)
cd_trials


# In[76]:


likely_cleaned = cd_trials.sf(0)
likely_cleaned


# In[84]:


1- cd_trials.pmf(0)


# - b.) How likely is it that it goes two days without getting cleaned up? All week?

# In[78]:


never_cleaned = 1-likely_cleaned
never_cleaned


# In[83]:


cd_trials.pmf(0)


# In[87]:


((cd_trials.pmf(0))**2).round(3)


# In[91]:


((cd_trials.pmf(0))**7).round(6) #.000003


# ### 6.)You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

# In[ ]:





# In[116]:


line_stdev = 3
line_mean = 15 #number of people on average in line
lunch_break = 60 #min for lunch
order_time_person = 2 #min
time_cook = 10 #min
eat_time = 15



time_to_get_order = lunch_break - time_cook - order_time_person - eat_time
time_to_get_order


# In[113]:


mean_line = (15*2)
std_line = (3*2)


# In[114]:


stats.norm(mean_line, std_line).cdf(time_eat)


# ### 7.)Connect to the employees database and find the average salary of current employees, along with the standard deviation. For the following questions, calculate the answer based on modeling the employees salaries with a normal distribution defined by the calculated mean and standard deviation then compare this answer to the actual values present in the salaries dataset.
# 
# 

# In[119]:


from env import host, user, password


def get_db_url(user, host, password, db):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
url = get_db_url('employees')

salaries_dr = pd.read_sql("SELECT * from salaries where to_date = '9999-01-01'", url)


# - a.)What percent of employees earn less than 60,000?

# In[ ]:





# - b.)What percent of employees earn more than 95,000?

# In[ ]:





# - c.)What percent of employees earn between 65,000 and 80,000?

# In[ ]:





# - d.)What do the top 5% of employees make?

# In[ ]: