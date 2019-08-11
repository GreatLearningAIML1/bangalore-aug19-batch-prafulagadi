#!/usr/bin/env python
# coding: utf-8

# ## Lists, Dictionaries and Sets in Python

# ## Part 1
# 
# ### Lists in Python
# 
# Sequences in Python are data structures that hold objects in an ordered array. Now, we will work on Lists, the most common sequence data types in Python.

# In[21]:


#Example 
l1 = ['learning', "Python", 'is fun?', True]
print(l1)


# List can also be created by using list() function. 

# In[22]:


#Example
l2 = list(("learning", "for", "life", True))
print(l2)


# Adding to an existing list
# 
# ### Question 1
# 
# Add 10 to list l1 given above.
# 
# [ **Hint: ** Use **append** ]

# In[13]:


# appending 10 to list l1
l1 = ['learning', "Python", 'is fun?', True,]
l1.append (10)
print (l1)


# Removing from an existing list
# 
# ### Question 2
# 
# Remove 10 from l1.
# 
# [ **Hint:** Use **remove**]

# In[14]:


l1 = ['learning', "Python", 'is fun?', True, 10]
l1.remove (10)
print (l1)


# Joining 2 lists
# 
# ### Question 3
# 
# [ **Hint: ** Use **+** operator or **extend**]

# In[25]:


l1 = ['learning', "Python", 'is fun?', True]
l2 = list(("learning", "for", "life", True))


# In[18]:


# Joining lists l1 and l2
l1 = ['learning', "Python", 'is fun?', True]
l2 = list(("learning", "for", "life", True))
l3 = l1 + l2
print(l3)


# Number List
# 
# ### Question 4
# 
# Find Range and Mean of l3.
# 
# l3 = [2,4,6,8]
# 
# [ **Hint: ** Use **len(),sum(), min(), max()** functions ]
#  
# If you want to use standard functions like mean & range, you have to import them from numpy else you can calculate them the traditional way using formulas

# In[25]:


#Finding Mean and Range of l3
l3 = [2,4,6,8]
print ("Range of l3 = ", [max(l3) - min(l3)])
print ("Mean of l3 = ", [sum(l3)/len(l3)])


# In[ ]:





# Count the occurances of an element in a given list.
# 
# ### Question 5
# Append the given sequence of numbers to l3 (given above) 0,1,3,3,5,5,7,9. Count the occurences of 5 in l3.
# 
# [ **Hint: ** Use ** + operator to add multiple elements in the array and count() function to print the occurences**]

# In[50]:


# Appending numbers and counting occurences of 5 in l3
l3 = [2,4,6,8]
l4 = [0,1,3,3,5,5,7,9]
l5 = l3 + l4
print (l5)
print (l5.count(5))


# Sorting and Reversing a list
# 
# ### Question 6
# sort and print l3 in ascending and descending order sequentially (given above)
# 
# **(Hint: Use .sort() function)**

# In[52]:


# displaying numbers in ascending number
l5.sort()
print(l5)


# In[56]:


# Descending order
l5.sort(reverse=True)
print (l5)


# ### Functions

# **Example:**
# 
# **def** function_name(args)**:**
#     
#     function code goes here

# ### Question 7
# 
# Define a function with name **sum_3** which can take 3 numbers as input, and returns sum of them.

# In[76]:


# Define function sum_3 and return sum of the number
def sum_3(a,b,c):
    sum_3=a + b + c
    return sum_3

a = 3
b = 5
c = 8
print("the sum of 3 numbers is", sum_3(a,b,c))


# ### Lambda Functions

# Anonymous functions or no name functions, which can be considered when you use a function only once.
# 
# **Example:**
# 
# f = lambda x, y : x + y
# 
# f(1,1)
# 
# 2
# 

# ### Question 8
# 
# Write the same above **sum_3** function using lambda.

# In[61]:


sum_3 = lambda a,b,c : a + b + c
print(sum_3(3,5,8))


# In[ ]:





# # Numpy

# We have seen python basic data structures in our last section. They are great but lack specialized features for data analysis. Like, adding roows, columns, operating on 2d matrices aren't readily available. So, we will use *numpy* for such functions.
# 
# 

# In[18]:


import numpy as np


# Numpy operates on *nd* arrays. These are similar to lists but contains homogenous elements but easier to store 2-d data.

# In[19]:


l1 = [1,2,3,4]
nd1 = np.array(l1)
print(nd1)

l2 = [5,6,7,8]
nd2 = np.array([l1,l2])
print(nd2)


# Sum functions on np.array()

# In[20]:


print(nd2.shape)

print(nd2.size)

print(nd2.dtype)


# ### Question 1
# 
# Create an identity 2d-array or matrix (with ones across the diagonal).
# 
# [ **Hint: ** You can also use **np.identity()** function ]

# In[62]:


import numpy as np


# In[70]:


np.identity(2)


# ### Question 2
# 
# Create a 2d-array or matrix of order 3x3 with values = 9,8,7,6,5,4,3,2,1 arranged in the same order.
# 
# Use: **np.matrix()** function
# 
# 

# In[74]:


A = np.matrix([[9,8,7],[6,5,4],[3,2,1]])
print(A)
              


# In[ ]:





# ### Question 3
# 
# Reverse both the rows and columns of the given matrix.
# 
# Hint: You can use the transpose **.T**)

# In[ ]:


# Program to transpose a matrix


# In[75]:


print (A)
A.T


# ### Question 4
# Add + 1 to all the elements in the given matrix.

# In[ ]:





# In[ ]:





# Similarly you can do operations like scalar  substraction, division, multiplication (operating on each element in the matrix)

# ### Question 5
# 
# Find the mean of all elements in the given matrix nd6.
# nd6 = [[  1   4   9 121 144 169]
#  [ 16  25  36 196 225 256]
#  [ 49  64  81 289 324 361]]
#  
#  Use: **.mean()** function
# 

# In[ ]:


# Program to find mean all elements given in matrices


# In[ ]:





# In[ ]:





# ### Question 7
# 
# Find the dot product of two given matrices.
# 
# [**Hint:** Use **np.dot()**]

# In[ ]:





# In[ ]:





# In[ ]:





# # Pandas

# We have seen Numpy in the last section. It is good at performing math operation on 2d-arrays of numbers. But the major drawback is, it cannot deal with heterogenous values. So, Pandas dataframes are helpful in that aspect for storing different data types and referring the values like a dict in python instead of just referring each item with index.
# 
# [Link to Official Documentation](http://pandas.pydata.org/pandas-docs/version/0.23/dsintro.html)

# ## Series

# Pandas series are almost same as nd arrays in numpy, with a additional inferencing ability with custom labels like *keys* in a *dictionary* in python.

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


#Example

series1 = pd.Series(data = [1,2,3], index = ['key1', 'key2', 'key3'])
series1


# ### Question 1
# 
# Convert a given dict to pd series.
# 
# [**Hint:** Use **.Series**]

# In[79]:


import pandas as pd


# In[ ]:





# In[ ]:


# Program to convert given dict to pd series 


# In[80]:


d1 = pd.Series(data = [1,2,3], index = ['a','b','c'])
d1


# You can directly use numpy functions on series.
# ### Question 2
# 
# Find the dot product of both the series create above
# 
# 
# [ **Hint: ** Use **np.dot()** ]

# In[ ]:


import numpy as np


# In[84]:


a1 = np.array([1,2,3])
b1 = np.array([a,b,c])
np.dot(a1,b1)


# In[83]:





# ## Dataframes

# A dataframe is a table with labeled columns which can hold different types of data in each column. 

# In[103]:


# Example
d1 = {'a': [1,2,3], 'b': [3,4,5], 'c':[6,7,8] }
df1 = pd.DataFrame(d1)
df1


# ### Question 3
# 
# Select second row in the above dataframe df1.
# 

# In[ ]:


# Importing Pandas as pd 


# In[ ]:


import pandas as pd


# In[119]:


d1 = {'a': [1,2,3], 'b': [3,4,5], 'c':[6,7,8] }
df1 = pd.DataFrame(d1)
df1


# In[125]:


df1.head(2)


# ### Question 4
# 
# Select column c in second row of df1.
# 
# [ **Hint: ** For using labels use **df.loc[row, column]**. For using numeric indexed use **df.iloc[]**. For using mixture of numeric indexes and labels use **df.ix[row, column]** ]
# 
# 

# In[139]:


df1.loc[[0, 2], :]


# ## Using Dataframes on a dataset

# ##### Using the mtcars dataset.
# 
# For the below set of questions, we will be using the cars data from [Motor Trend Car Road Tests](http://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html)
# 
# The data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973–74 models). 
# 
# 
# Details :
#     
# A data frame with 32 observations on 11 (numeric) variables.
# 
# [, 1] 	mpg 	Miles/(US) gallon
# 
# [, 2] 	cyl 	Number of cylinders
# 
# [, 3] 	disp 	Displacement (cu.in.)
# 
# [, 4] 	hp 	Gross horsepower
# 
# [, 5] 	drat 	Rear axle ratio
# 
# [, 6] 	wt 	Weight (1000 lbs)
# 
# [, 7] 	qsec 	1/4 mile time
# 
# [, 8] 	vs 	Engine (0 = V-shaped, 1 = straight)
# 
# [, 9] 	am 	Transmission (0 = automatic, 1 = manual)
# 
# [,10] 	gear 	Number of forward gears
# 
# [,11] 	carb 	Number of carburetors 

# In[94]:


## Reading a dataset from a csv file using pandas.
mtcars = pd.read_csv('mtcars.csv')
mtcars.index = mtcars['name']


# Following questions are based on analysing a particular dataset using dataframes.

# ### Question 5
# 
# Check the type and dimensions of given dataset - mtcars.
# 
# 
# [ **Hint: ** Use **type()** and **df.shape** ]

# In[ ]:


import numpy as np


# In[ ]:


import pandas as pd


# ### Question 6
# 
# Check the first 10 lines and last 10 lines of the given dataset- mtcars.
# 
# [**Hint:** Use **.head()** and **.tail()**]

# In[ ]:





# ### Question 7
# 
# Print all the column labels in the given dataset - mtcars.
# 
# [ **Hint: ** Use **df.columns** ]

# In[ ]:





# ### Question 8

# Select first 6 rows and 3 columns in mtcars dataframe.
# 
# **Hint: **  
# mtcars.ix[:,:] gives all rows and columns in the dataset.

# In[ ]:





# In[ ]:




