#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

# ### Coin toss interview question
# 
# - how do you insure a fair toss when either you dont know that coin is fair /ubnfair or assuming the coin is unfair?
# 
# - Just toss the coin twice!!

# p(T)= 1/4
# p(H)=3/4
# 
# 
# P(H,H) = 3/4 * 3/4
# 
# P(H,T) = 3/4 * 1/4
# 
# P(T,H) = 1/4 * 3/4
# 
# P(T,T) = 1/4 * 1/4

# ### 1.)A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.
# 
# 

# In[4]:


λ = 2 #cars at noon


# In[7]:


x = np.arange(0,12)
y = stats.poisson(λ).pmf(x)

plt.bar(x,y)
plt.title('Poisson dist with $lambda = 2$')
plt.xlabel('Number of cars')
plt.ylabel('P(X)');


# a.) What is the probability that no cars drive up in the noon hour?

# In[8]:


stats.poisson(λ).pmf(0)


# b.) What is the probability that 3 or more cars come through the drive through?

# In[6]:


stats.poisson(λ).sf(2)


# c.) How likely is it that the drive through gets at least 1 car? means one or more

# In[9]:


stats.poisson(λ).sf(0).round(2)


# In[ ]:





# ### 2.)Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:
# 

# In[ ]:





# - a.) What grade point average is required to be in the top 5% of the graduating class?

# In[11]:


#top 15 %
mean = 3
stddev = .3
stats.norm(mean,stddev).isf(.05).round(2)


# - b.) What GPA constitutes the bottom 15% of the class? # can use ppf

# In[27]:


mean = 3
stddev = .3
stats.norm(mean,stddev).isf(.85)


# In[13]:


stats.norm(mean,stddev).ppf(.15)


# - c.)An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

# In[21]:


mean = 3
stddev = .3
stats.norm(mean,stddev).isf(.70)


# In[ ]:





# In[31]:


stats.norm(mean,stddev).isf(.80)


# In[15]:


stats.norm(mean,stddev).ppf([0.2,0.3])


# In[33]:


# They would qualify! 


# - d.) If I have a GPA of 3.5, what percentile am I in?

# In[39]:


#They are in 95 percentile
stats.norm(mean,stddev).isf(.05)


# In[16]:


stats.norm(mean,stddev).cdf(3.5)


# In[17]:


(np.random.normal(3,0.3,100_000) < 3.5).mean()


# ### 3.)A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs. 
# 

# - a.)How likely is it that this many people or more click through?

# In[19]:


#binomal
ct = 97
n_trials = 4326
p = .02

clicks = stats.binom(n_trials, p)
clicks.sf(96)


# In[20]:


#using simulation
clicks = np.random.choice([0,1], (100_000, 4326), p = [0.98, 0.02])
clicks


# In[21]:


(clicks.sum(axis =1) >96).mean()


# In[23]:


# using poisson

λ = n_trials * p

stats.poisson(λ).sf(96)


# ### 4.)You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.
# 

# - a.) What is the probability that at least one of your first 60 answers is correct?

# In[29]:


#binom
h_trials = 60
pt =0.01
chance = stats.binom(h_trials,pt).sf(0)
chance


# In[31]:


#by simulation
((np.random.choice([0,1], (100_000, 60), p =[0.99, 0.01])).sum(axis=1) >0).mean()


# ### 5.)The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. 
# 

# - a.) How likely is it that the break area gets cleaned up each day? 

# In[33]:


number_of_students = (.90 * (3*22))
p = 0.03


# In[35]:


number_of_students = round(number_of_students)
number_of_students 


# In[37]:


cd_trials = stats.binom(number_of_students, p).sf(0)
cd_trials


# In[42]:


x = np.arange(0,10)
y = stats.binom(number_of_students, p).pmf(x)

plt.bar(x,y)
plt.xlabel('Number of time are is cleaned per day')


# - b.) How likely is it that it goes two days without getting cleaned up? All week?

# In[46]:


never_cleaned = 1-cd_trials
never_cleaned


# In[49]:


# two_days

cd_trials_2_days = stats.binom(number_of_students * 2, p).pmf(0)
cd_trials_2_days


# In[50]:


#all week
cd_trials_5_days = stats.binom(number_of_students * 5, p).pmf(0)
cd_trials_5_days


# ### 6.)You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

# In[ ]:





# In[54]:


line_stdev = 3
line_mean = 15 #number of people on average in line
lunch_break = 60 #min for lunch
order_time_person = 2 #min
time_cook = 10 #min
eat_time = 15


#max amount of time without being late. 60- 15 eat - 10 food prep
time_to_get_order = lunch_break - time_cook - eat_time
time_to_get_order


# In[52]:


#convert mean and std from ppl to min
mean_line = (15*2) #mins
std_line = (3*2)


# In[55]:


stats.norm(mean_line, std_line).cdf(time_to_get_order)


# In[56]:


mean = 15
std_dev = 3

stats.norm(mean,std_dev).cdf(17.5)


# In[57]:


(np.random.normal(30,6,100_000) < 35).mean()


# ### 7.)Connect to the employees database and find the average salary of current employees, along with the standard deviation. For the following questions, calculate the answer based on modeling the employees salaries with a normal distribution defined by the calculated mean and standard deviation then compare this answer to the actual values present in the salaries dataset.
# 
# 

# In[6]:


from env import host, user, password

def get_db_url(user, host, password, db):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[7]:


url = f'mysql+pymysql://{user}:{password}@{host}/employees'


# In[11]:


salaries_db = pd.read_sql("SELECT * FROM salaries WHERE to_date = '9999-01-01'", url)


# In[12]:


salaries_db


# In[29]:


salary_mean = salaries_db.salary.mean()
salary_mean


# In[30]:


salary_std = salaries_db.salary.std()
salary_std


# - a.)What percent of employees earn less than 60,000?

# In[20]:


salaries_mean = salaries_db.describe()
salaries_mean = 72012.235857
salaries_std = 17309.995380


# In[21]:


sixitybelow =stats.norm(salaries_mean,salaries_std).cdf(60_000)


# - b.)What percent of employees earn more than 95,000?

# In[22]:


ninetyfive = stats.norm(salaries_mean,salaries_std).sf(94999)


# - c.)What percent of employees earn between 65,000 and 80,000?

# In[23]:


sixity_five = stats.norm(salaries_mean,salaries_std).cdf(65000)
sixity_five


# In[24]:


eighty = stats.norm(salaries_mean,salaries_std).sf(79999)
eighty


# In[25]:


1-sixity_five - eighty


between_six_eig = np.diff(stats.norm(salaries_mean,salaries_std).cdf([65000, 80000]))
between_six_eig

# - d.)What do the top 5% of employees make?

# In[27]:


stats.norm(salaries_mean,salaries_std).isf(.05)

