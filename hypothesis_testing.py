#!/usr/bin/env python
# coding: utf-8

# ## Central Limit Theorem

# If you have a population (regardless of distribution) with mean μ and take sufficiently large random samples (usually N > 30) from the population, then the distribution of the sample means will be approximately normally distributed

# In[1]:


import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


roll  = stats.randint(1, 7)


# In[3]:


plt.hist(roll.rvs(100000), bins= [1,2,3,4,5,6,7], align = 'left', width = 0.9)
plt.title('Uniform Population distribution')


# In[4]:


roll.rvs(100000).mean()


# ### Distribution of sample means 
# ![CLT.png](attachment:CLT.png)

# # Comparing Means
# 
# 
# _______________________________________________________________________
# 
# |Goal|$H_{0}$|Data Needed|Parametric Test|Assumptions*||  
# |---|---|---|---|---|---|  
# |Compare observed mean to theoretical one|$\mu_{obs} = \mu_{th}$|array-like of observed values & float of theoretical|One sample t-test: scipy.stats.ttest_1samp|Normally Distributed\*\*||   
# |Compare two observed means (independent samples)|$\mu_{a} = \mu_{b}$|2 array-like samples|Independent t-test (or 2-sample): scipy.stats.ttest_ind|Independent, Normally Distributed\*\*, Equal Variances\*\*\*||   
# |Compare several observed means (independent samples)|$\mu_{a} = \mu_{b} = \mu_{n}$|n array-like samples|ANOVA: scipy.stats.f_oneway|Independent, Normally Distributed\*\*, Equal Variances**||   
# 
# \*If assumptions can't be met, the equivalent non-parametric test can be used.  
# \*\*Normal Distribution assumption can be be met by having a large enough sample (due to Central Limit Theorem), or the data can be scaled using a Gaussian Scalar.   
# \*\*\*The argument in the stats.ttest_ind() method of `equal_var` can be set to `False` to accomodate this assumption.   
# 
# ## One Sample T-Test
# 
# Goal: Compare observed mean to theoretical one. 
# 
# 1. Plot Distributions (i.e. Histograms!)  
# 
# 2. Establish Hypotheses   
# th = population sample
# ||||  
# |-----|-----|---------|  
# |Null Hypothesis|$H_{0}$|$\mu_{obs} = \mu_{th}$|  
# |Alternative Hypothesis (2-tail, significantly different)|$H_{a}$|$\mu_{obs} != \mu_{th}$|  
# |Alternative Hypothesis (1-tail, significantly smaller)|$H_{a}$|$\mu_{obs} < \mu_{th}$|  
# |Alternative Hypothesis (1-tail, significantly larger)|$H_{a}$|$\mu_{obs} > \mu_{th}$|      
# 
# 3. Set Significance Level: $\alpha = .05$
# 
# 4. Verify Assumptions: Normal Distribution, or at least 30 observations and "kinda" normal. The more observations you have, the less "normal" it needs to appear. (CLT)  
# 
# 5. Compute test statistic and probability (t-statistic & p-value) using `scipy.stats.ttest_1samp`. 
# 
# 6. Decide. **For a 2-tailed test, we take the p-value as is. For a 1-tailed test, we evaluate $p/2 < \alpha$ and $t > 0$ (to test if higher), and of a less-than test when $p/2 < \alpha$ and $t < 0$.**

# ![T-test-2.png](attachment:T-test-2.png)
# 
# - t-statistic == 0 means no difference is means (i.e null hypothesis is true)
# - Only when t-statistic is larger enough (positive or negative) we are confident that means are different enough to reject null

# ### Example 1
# 
# I believe customers who churn are charged more (monthly average) than the overall average monthly charges.  
# Is the mean of monthly charges of customers who churn significantly higher than the mean across all customers? 
# 
# We will use a 1-tailed ("significantly higher"), 1-sample (comparing 1 group to the average) t-test.  

# In[183]:


# read the csv file 
df = pd.read_csv("Cust_Churn_Telco.csv")  


# H0 = customers who churn are not charged more than overall averge monthly charges
# Ha = customers who churn are charged more (monthly average) than the overall average monthly charges

# In[184]:


# look at the head
df.head()


# **A. Plot Distribution**

# In[16]:


# plot distribution of monthly charges
churn_sample = df.MonthlyCharges
churn_sample.hist()


# In[185]:


# plot distribution of montly charges for customer who churn
churn_sample = df[df.Churn =='Yes'].MonthlyCharges
churn_sample.hist()


# **B. Set Hypothesis**
# 
# $H_{0}$: Mean of monthly charges of churned customers = Mean of monthly charges of all customers  
# $H_{a}$: Mean of monthly charges of churned customers > Mean of monthly charges of all customers  
# 
# **C. Set Alpha**

# In[21]:


# we decide on 95% cofidence level (alpha = 0.05)
alpha = 0.05


# **D. Verify Assumptions**

# In[20]:


# How big is sample size for churned customers?
# If sample size is significantly > 30, we don't have to worry about normality (CLT!!)
df.Churn.value_counts() # our churn sample is large enough on overall count to meet distributionsd


# Our churn sample is large enough, as is overall count, to meet the assumptions of normal distributions. 

# **E. Compute test statistic and probability (t-statistic & p-value)**
# 
# - scipy.stats.ttest_1samp
# - For a 1-tailed test where our alternative hypothesis is testing for "greater than", we evaluate 𝑝/2 < 𝛼  and  𝑡 > 0. 

# In[186]:


# calculate t and p statistic
churn_sample = df[df.Churn == 'Yes'].MonthlyCharges
overall_mean = df.MonthlyCharges.mean()
t, p = stats.ttest_1samp(churn_sample, overall_mean)

t, p/2, alpha


# **F. Decide**
# 
# Is 1/2 * p < alpha AND t > 0? 
# 
# Is $t > 0$ and $p/2 < \alpha$
# 
# t positive means sample means greater than population mean

# In[58]:


if (p/2 < alpha) & (t > 0):
    print("We reject the null hypothesis")
else:
    print("We fail to reject the null hypothesis")


# ## Example 2
# ### TWO TAILED!!!!!!!!!!!
# 
# **A. Distributions** See above
# 
# **B. Set Hypothesis**
# 
# $H_{0}$: Mean of monthly charges of churned customers = Mean of monthly charges of all customers  
# $H_{a}$: Mean of monthly charges of churned customers != Mean of monthly charges of all customers  
# 
# ## only care about being significanly different!!!
# 
# **C. Set Alpha** See above  
# 
# **D. Assumptions** See above  
# 
# **E. Compute test statistics**

# In[30]:


t,p = stats.ttest_1samp(churn_sample, overall_mean)
t, p, alpha


# **F. Is p-value less than alpha?**

# In[29]:


if p <  alpha:
    print("We reject the null hypothesis")
else: 
    print(" We fail to reject the null hypothesis")


# ## Independent T-Test (a.k.a. Two Sample T-Test)
# 
# Goal: Compare mean of group a to mean of group b. 
# 
# 1. Plot Distributions (i.e. Histograms!)  
# 
# 2. Establish Hypotheses   
# 
# ||||  
# |-----|-----|---------|  
# |Null Hypothesis|$H_{0}$|$\mu_{a} == \mu_{b}$|  
# |Alternative Hypothesis (2-tail, significantly different)|$H_{a}$|$\mu_{a} != \mu_{b}$|  
# |Alternative Hypothesis (1-tail, a is significantly smaller than b)|$H_{a}$|$\mu_{a} < \mu_{b}$|  
# |Alternative Hypothesis (1-tail, a is significantly larger than b)|$H_{a}$|$\mu_{a} < \mu_{b}$|      
# 
# 3. Set Significance Level: $\alpha = .05$ (in other words Confidence level is 0.95)
# 
# ### 4. Verify Assumptions:  
#     - Normal Distribution, or at least 30 observations and "kinda" normal. The more observations you have, the less "normal" it needs to appear. (CLT)  
#     - Independent samples  
#     - Equal Variances (or set method argument to False when not)
# 
# 
# 5. Compute test statistic and probability (t-statistic & p-value) using `stats.ttest_ind`
# 
# 6. Decide. 

# ### Example 1
# 
# I believe customers who churn are charged more (monthly average) than customers who don't churn. 
# Is the mean of monthly charges of customers who churn significantly higher than the mean of those who don't churn? 
# 
# We will use a 1-tailed ("significantly higher"), 2-sample (comparing 2 groups) t-test.  

# In[32]:


# histogram of churned customers
churn_sample = df[df.Churn == 'Yes'].MonthlyCharges
churn_sample.hist()


# In[34]:


# histogram of non-churned customers

no_churn_sample = df[df.Churn == 'No'].MonthlyCharges
no_churn_sample.hist()


# **Set Hypothesis**
# 
# $H_{0}$: Mean of monthly charges of churned customers = Mean of monthly charges of customers who haven't churned  
# $H_{a}$: Mean of monthly charges of churned customers > Mean of monthly charges of customers who haven't churned  
# 
# **Set Alpha**

# In[68]:


alpha = .05


# **Verify Assumptions**
# 
# 1. Independent Samples. YES! no observations in the churn sample exist in the no-churn sample. 
# 
# 2. Normal Distribution, or at least 30 observations and "kinda" normal. The more observations you have, the less "normal" it needs to appear. (CLT).  YES! Plenty of observations
# 
# #### 3. Equal Variances (the scipy methods we will use has an argument to handle when variances aren't equal).

# In[46]:


churn_sample.var(), no_churn_sample.var()


# If no, we will set the argument of equal_var to False. 
# 
# **Compute Test Statistic**

# In[43]:


t,p = stats.ttest_ind(churn_sample, no_churn_sample, equal_var = False) # 1 tailed, subtracts in order we put them..

t, p/2, alpha


# **Decide**

# In[44]:


print("is p/2 < alpha? ", p/2 < alpha)
print("is t > 0? ", t > 0)


# In[45]:


if (p/2 < alpha) & (t > 0):
    print("We reject the null hypothesis")
else:
    print("We fail to reject the null hypothesis")


# ## Example 2
# 
# Are charges of customers who churn *significantly different* than those who do not churn? 
# 
# $H_{0}$: charges of customers who churn equals that of those who don't churn.   
# 
# $H_{a}$: charges of customers who churn is not equal to that of those who don't churn. 
# 
# We can use 2 sample, 2-tailed t-test here

# In[49]:


t, p = stats.ttest_ind(churn_sample, no_churn_sample, equal_var = False)

t,p, alpha


# **Decide**
# 
# Is the p-value less than alpha?

# In[48]:


print("Reject $H_{0}$? ", p < alpha)


# ## Example 3
# 
# Are charges of customers who churn *significantly less* than those who do not churn? 
# 
# $H_{0}$: charges of customers who churn equals that of those who don't churn.   
# 
# $H_{a}$: charges of customers who churn is less than that of those who don't churn. 

# In[53]:


# 1 tailed test, see if t less than 0

t, p = stats.ttest_ind(churn_sample, no_churn_sample, equal_var = False)

t, p, p/2


# **Decide**
# 
# is t < 0? AND is p/2 < alpha?
# 

# In[54]:


print("Is t < 0? ", t<0)

print("is p/2 < alpha? ", p/2<alpha)


# In[55]:


if (p/2 < alpha) & (t < 0):
    print("We reject the null hypothesis")
else:
    print("We fail to reject the null hypothesis")


# ## Summary
# ![T-test-2.png](attachment:T-test-2.png)

# ### MPG Example

# In[56]:


df = sns.load_dataset('mpg')
df.origin.value_counts()


# In[57]:


df.head()
df.info()


# Drop nulls

# In[62]:


df = df.dropna()


# #### Do the vehicle built in USA have higher HP than vehicle from Japan?

# In[63]:


usa_hp = df[df.origin == 'usa'].horsepower
japan_hp = df[df.origin == 'japan'].horsepower


# **Plot Distribution**

# In[64]:


usa_hp.hist()


# In[61]:


japan_hp.hist()


# In[ ]:





# **Hypothesis**
# 
# $H_{0}$: hp is the same for usa and japan origin vehicles
# 
# $H_{a}$: hp is not the for usa and japan origin vehicles
# 
# **Significance Level**
# 
# $\alpha$ is already set to .05 (95% cofidence level)
# 
# **Verify Assumptions**
# 
# - Normal: yes!
# - Independent: yes!
# - Variance: ?

# In[67]:


usa_hp.count(), japan_hp.count() # equal_var will be false!!


# In[65]:


# do two sample have similar variances?
usa_hp.var(), japan_hp.var() # dont have similar variances!!


#  ### Looking at the variances, they are very different, so I will move to a 2-sample, independent t-test comparing usa made cars vs. japan made cars. 

# In[68]:


# use Scipy's independent ttest to find t and p

t, p = stats.ttest_ind(usa_hp, japan_hp, equal_var = False)

t, p, alpha


# **Decide**
# 
# is p-value less than alpha? 

# In[69]:


p < alpha


# Reject null hypothesis. The hp of usa cars vs. japan cars is significantly different. 

# ### Mini Exercise:

# Are the USA origin vehicles heavier than vehicles with European origin?

# In[73]:


usa_weight = df[df.origin == 'usa'].weight
japan_weight = df[df.origin == 'japan'].weight


# #### Decide?
# 
# One sample t-test or 2-sample t-test?   
# One tailed or two tailed?
# 
# 
# 2 sample, one tailed

# In[74]:


usa_weight.count(), japan_weight.count()


# In[75]:


usa_weight.var(), japan_weight.var() # var significantly diff so use 2 tailed


# #### Plot distributions

# In[76]:


usa_weight.hist()


# In[77]:


japan_weight.hist()


# In[ ]:





# **Hypothesis**
# 
# $H_{0}$:average weights of usa cars == average weight of japan cars.
# 
# $H_{a}$: average weights of usa cars > average weight of japan cars
# 
# 
# 
# **Significance Level**
# 
# $\alpha$ = 0.05
# 
# **Verify Assumptions**
# 
# - Normal: count is greater than 30 so can ignore the normal dist.
# - Independent: Yes, looking at weight of japan cars and us cars. These are two different subsets
# - Variance: Vars are significantly different!

# In[78]:


# use stats.ttest to calculate t and p
t, p = stats.ttest_ind(usa_weight, japan_weight, equal_var = False)

t, p, alpha # positive t value means 


# #### Decide

# In[80]:


p/2 < alpha


# ### reject the H null, so Usa Car weight is greater than japan car weight!!!

# In[ ]:





# In[ ]:





# ## Exercises

# #### Ace Realty wants to determine whether the average time it takes to sell homes is different for its two offices. A sample of 40 sales from office #1 revealed a mean of 90 days and a standard deviation of 15 days. A sample of 50 sales from office #2 revealed a mean of 100 days and a standard deviation of 20 days. Use a .05 level of significance.

# ### keyword here is difference, so 2 tail and these are two subsets so independent.
# 
# **Hypothesis**
# 
# $H_{0}$:office 1 average time to sell homes == office 2 average time to sell homes.
# 
# $H_{a}$:office 1 average time to sell homes != office 2 average time to sell homes.
# 
# 
# 
# **Significance Level**
# 
# $\alpha$ = 0.05
# 
# **Verify Assumptions**
# 
# - Normal: count is greater than 30 so can ignore the normal dist.
# - Independent: Yes, looking average time for office one and office 2
# - Variance: Vars are different!
# 
# 

# In[88]:


15 ** 0.5


# In[90]:


20 ** 0.5


# In[92]:


mean1 = 90 
mean2 = 100
std1 = 15
std2 = 20
obs1 = 40
obs2 = 50


# In[ ]:





# In[ ]:


alpha = 0.05


# In[94]:


t,p = stats.ttest_ind_from_stats(mean1, std1, obs1, mean2, std2, obs2, equal_var = False)
t, p, alpha


# In[96]:


print("Reject $H_{0}$? ", p < alpha)


# #### Load the mpg dataset and use it to answer the following questions:

# In[143]:


from pydataset import data


# In[144]:


mpg = data('mpg')


# In[145]:


mpg.info()


# In[86]:


mpg.head(5)


# ### 1.) Is there a difference in fuel-efficiency in cars from 2008 vs 1999?
# 

# In[146]:


mpg['average_mileage'] = (mpg.hwy + mpg.cty)/2
mpg


# In[172]:


mpg


# In[ ]:





# In[148]:


cars_2008_year = mpg[mpg.year == 2008].average_mileage
cars_2008_year.count()


# In[149]:


cars_2008_year.hist()


# In[150]:


cars_1999_year = mpg[mpg.year == 1999].average_mileage
cars_1999_year.count()


# In[151]:


cars_1999_year.hist()


# In[152]:


cars_2008_year.var(), cars_1999_year.var()


# ### keyword here is difference, so 2 tail and these are two subsets so independent.
# 
# **Hypothesis**
# 
# $H_{0}$:fuel-efficency in cars from 2008 == fuel-efficency in cars from 1999.
# 
# $H_{a}$: fuel-efficency in cars from 2008 > fuel-efficency in cars from 1999.
# 
# 
# 
# **Significance Level**
# 
# $\alpha$ = 0.05
# 
# **Verify Assumptions**
# 
# - Normal: count is greater than 30 so can ignore the normal dist.
# - Independent: Yes, fuel-efficency of two different subsets.
# - Variance: Vars are significantly different!

# In[154]:


t, p = stats.ttest_ind(cars_2008_year, cars_1999_year, equal_var = False)

t, p, alpha


# In[156]:


if p > alpha: 
    print("Reject the null hypothesis, they are the same")
    print("We move forward with the alternative hypothesis")
else:
    print("We fail to reject the null hypothesis")


# ### 2.)Are compact cars more fuel-efficient than the average car?
# 

# In[177]:


compact = mpg[mpg['class'] == 'compact'].average_mileage


# In[197]:


total_car = mpg.average_mileage


# In[179]:


compact.count()


# In[180]:


total_car.count()


# In[178]:


compact.var(), total_car.var() #var is significant different!


# In[193]:


total_car_mean = total_car.mean()


# ### keyword here compact fuel-efficency greater than total population, so this is one sample mean vs population.
# 
# **Hypothesis**
# 
# $H_{0}$:fuel-efficency compact == fuel-efficency total population.
# 
# $H_{a}$: fuel-efficency compact > fuel-efficency total population.
# 
# 
# 
# **Significance Level**
# 
# $\alpha$ = 0.05
# 
# **Verify Assumptions**
# 
# - Normal: count is greater than 30 so can ignore the normal dist.
# - Independent: No this is one sample t-test, 1 tailed. Want to see if compact > total.
# - Variance: Vars are significantly different!

# In[ ]:





# In[199]:


t, p = stats.ttest_1samp(compact, total_car.mean())

t, p/2, alpha


# In[200]:


if (p/2 < alpha) & (t > 0):
    print("We reject the null hypothesis")
else:
    print("We fail to reject the null hypothesis")


# ### 3.)Do manual cars get better gas mileage than automatic cars?

# ### keyword here manual greater than automatic, so this is a Independent(two sample) , one tailed(greater or less).
# 
# **Hypothesis**
# 
# $H_{0}$:fuel-efficency manual cars == fuel-efficency auto cars.
# 
# $H_{a}$: fuel-efficency manual cars > fuel-efficency auto cars.
# 
# 
# 
# **Significance Level**
# 
# $\alpha$ = 0.05
# 
# **Verify Assumptions**
# 
# - Normal: count is greater than 30 so can ignore the normal dist.
# - Independent: Yes, manual cars, auto cars, two seperate subsets.
# - Variance: Vars are significantly different!

# In[219]:


auto = mpg[mpg['trans'].str.lower().str.startswith('a')].average_mileage
auto.count()


# In[216]:


auto.hist()


# In[ ]:





# In[220]:


manual = mpg[mpg['trans'].str.lower().str.startswith('m')].average_mileage
manual.count()


# In[218]:


manual.hist()


# In[213]:


auto.var(), manual.var()


# In[214]:


auto_mean = auto.mean()


# In[215]:


manual_mean = manual.mean()


# In[223]:


stats.levene(manual, auto)


# In[226]:


t, p = stats.ttest_ind(manual, auto, equal_var = True)

t, p/2, alpha


# In[227]:


if (p/2 < alpha) & (t > 0):
    print("We reject the null hypothesis")
else:
    print("We fail to reject the null hypothesis")

