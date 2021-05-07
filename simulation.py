import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
import viz
np.random.seed(1234)


# ## Exercises

# 1.) How likely is it that you roll doubles when rolling two dice?

# In[139]:


6/36


# In[141]:


n_trials = nrows = 10_000
n_dice = ncols = 2
rolls = np.random.choice([1,2,3,4,5,6], n_trials * n_dice).reshape(nrows, ncols)


# In[144]:


doubles = pd.DataFrame(rolls).apply(lambda row: row[0] == row[1], axis=1).mean()


# In[145]:


doubles


# 2.) If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# In[151]:


3/256


# In[154]:


5/256


# In[152]:


2*2*2*2*2*2*2*2


# In[172]:


p_heads = 1
p_tails = 0
flips = ncols = 8
coin_flip = nrows = 10_000


# In[173]:


coin_outcomes = [0,1]


# In[174]:


heads_flipped = np.random.choice(coin_outcomes, flips * coin_flip).reshape(nrows,ncols)


# In[180]:


total_heads = heads_flipped.sum(axis=1)
total_heads


# In[179]:


three_heads = (total_heads == 3).mean()
three_heads


# In[181]:


more_than_three = (total_heads > 3).mean()
more_than_three


# 3.) There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?
# 

# In[ ]:


#1:3 ds for web
#random, trials is 2


# In[36]:


(1/4) * (1/4)


# In[41]:


web = 3
ds = 1
billboards = ncols = 2
cdtrials = nrows = 10_000
billoutcomes = [3,1]
p_web = 0.75
ds = 1-p_web


# In[196]:



bill_data = np.random.choice(billoutcomes, nrows*ncols, p =[p_web, ds]).reshape(nrows,ncols)
bill_data


# In[197]:


bboard_sum = bill_data.sum(axis=1)


# In[198]:


data_billboard = (bboard_sum == 2).mean()
data_billboard


# madeline method

# In[42]:


bill_data_using_random = np.random.random((n_rows,n_cols))


# In[43]:


(bill_data_using_random < ds).mean()


# 4.) Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

# In[44]:


n_trials = n_rows = 1000000
n_days = n_cols = 5


# In[49]:


pop_data = np.random.normal(3, 1.5, n_trials * n_days).reshape(n_rows,n_cols)


# In[50]:


sum_pop =pop_data.sum(axis=1)
sum_pop


# In[51]:


pop_avail = (sum_pop < 17).mean()
pop_avail


# In[ ]:





# 5.) Compare Heights
# 
# Men have an average height of 178 cm and standard deviation of 8cm.
# 
# Women have a mean of 170, sd = 6cm.
# 
# If a man and woman are chosen at random, P(woman taller than man)?
# 
# 

# In[222]:


mw_trials = n_rows = 10000
mw_days = n_cols = 2


# In[238]:


men_data = np.random.normal(178, 8, mw_trials * mw_days).reshape(n_rows,n_cols)
men_data


# In[237]:


women_data = np.random.normal(170, 6, mw_trials * mw_days).reshape(n_rows,n_cols)
women_data


# In[ ]:





# In[244]:


heights_diff = np.subtract(men_data, women_data)
heights_diff


# In[246]:


taller_women = (heights_diff < 0).mean()
taller_women


# 6.) When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails.
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?150? 450?

# In[256]:


student_down = n_rows = 10_000
n_students = n_cols = 50
pdfail = (1/250)
pdpass = 1 - pdfail
pr_outcome = [0,1]


# In[257]:


fifty_test = np.random.choice(pr_outcome, n_rows*n_cols, p =[pdfail, pdpass]).reshape(n_rows,n_cols)
fifty_test


# In[259]:


fifty_total = fifty_test.sum(axis=1)
fifty_total


# In[262]:


fifty_fail = (fifty_total <50).mean()
fifty_fail


# In[264]:


fifty_pass = 1-fifty_fail
fifty_pass


# In[265]:


student_down = n_rows = 10_000
n100_students = n_cols = 100
pdfail = (1/250)
pdpass = 1 - pdfail
pr_outcome = [0,1]


# In[266]:


hundred_test = np.random.choice(pr_outcome, n_rows*n_cols, p =[pdfail, pdpass]).reshape(n_rows,n_cols)
hundred_test


# In[270]:


hundred_total = hundred_test.sum(axis=1)
hundred_total


# In[272]:


hundred_fail = (hundred_total <100).mean()
hundred_fail 


# In[273]:


hundred_pass = 1-hundred_fail
hundred_pass


# In[56]:


student_down = n_rows = 10_000
n150_students = n_cols = 150
pdfail = (1/250)
pdpass = 1 - pdfail
pr_outcome = [0,1]


# In[57]:


onefiftytest = np.random.choice(pr_outcome, n_rows*n_cols, p =[pdfail, pdpass]).reshape(n_rows,n_cols)


# In[64]:


1-((onefiftytest.sum(axis=1))<150).mean()


# In[60]:


student_down = n_rows = 10_000
n450_students = n_cols = 450
pdfail = (1/250)
pdpass = 1 - pdfail
pr_outcome = [0,1]


# In[61]:


fourfiftytest = np.random.choice(pr_outcome, n_rows*n_cols, p =[pdfail, pdpass]).reshape(n_rows,n_cols)


# In[63]:


1- ((fourfiftytest.sum(axis=1))<450).mean()


# 7.) There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?
# 
# How likely is it that a food truck will show up sometime this week?

# In[ ]:


# could utilize np.random.random for several problems


# In[287]:


f_trials = n_rows = 10_000
weekday = n_cols =3
p_there = .70
p_not = 1-p_there
ft_outcomes =[0,1]


# In[292]:


truck_test = np.random.choice(ft_outcomes, n_rows*n_cols, p =[p_not, p_there]).reshape(n_rows,n_cols)
truck_test


# In[ ]:





# In[293]:


truck_count = truck_test.sum(axis=1)
truck_count


# In[294]:


truck_not_three =(truck_count == 0).mean()
truck_not_three


# In[295]:


f_trials = n_rows = 10_000
weekday = n_cols =4
p_there = .70
p_not = 1-p_there
ft_outcomes =[0,1]


# In[298]:


truck_test4 = np.random.choice(ft_outcomes, n_rows*n_cols, p =[p_not, p_there]).reshape(n_rows,n_cols)
truck_test4


# In[300]:


truck_count4 = truck_test4.sum(axis=1)
truck_count4


# In[301]:


truck4 = (truck_count4 > 0).mean()


# In[302]:


truck4


# 8.) If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?

# In[6]:


bdays = np.arange(1,366)


# In[7]:


bd_trials = n_rows = 10_000
people_room = n_cols =23


bday_test = np.random.choice(bdays, n_rows*n_cols).reshape(n_rows,n_cols)


# In[11]:


bday_data = pd.DataFrame(bday_test)
bday_data


# In[13]:


bday_test_match_23 = bday_data.nunique(axis=1)
bday_test_match_23


# In[14]:


bday_match_23_total = (bday_test_match_23 < 23).mean()


# In[15]:


bday_match_23_total


# In[23]:


#20 people
people_room_20 = n_cols =20
bd_trials = n_rows = 10_000

twenty_test = np.random.choice(bdays, n_rows*n_cols).reshape(n_rows,n_cols)


# In[24]:


twenty_data = pd.DataFrame(twenty_test)
twenty_data


# In[25]:


twenty_unique = twenty_data.nunique(axis=1)
twenty_unique


# In[27]:


twenty_count = (twenty_unique < 20).mean()
twenty_count


# In[28]:


#40 people
people_room_40 = n_cols =40
bd_trials = n_rows = 10_000

forty_test = np.random.choice(bdays, n_rows*n_cols).reshape(n_rows,n_cols)


# In[31]:


forty_data = pd.DataFrame(forty_test)
forty_data


# In[33]:


forty_unique = forty_data.nunique(axis=1)
forty_unique


# In[35]:


forty_count = (forty_unique < 40).mean()
forty_count

