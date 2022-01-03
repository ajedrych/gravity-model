#!/usr/bin/env python
# coding: utf-8

# # LAB 2: VISUALIZING DATA, DESCRIBING DATA WITH STATISTICS, SIMPLE LINEAR MODEL
# 

#  ## 1.1 CREATING GRAPHS WITH MATPLOTLIB

# As we know the Cartesian coordiante plane allows us to visualize the relationship between two sets
# of numbers.

# We'll be using matplotlib package to make graphs with Python. Let's start with a simple graph with
# just three points. To create this graph, we'll first make tow lists of numbers - one storing the values of
# x-coordinates and another for y-coordinates.

# In[17]:


x=[1, 2, 3]
y=[4, 5, 6]


# Firstly we have to import plot() and show() functions from the pylab module, wich is part of the
# matplotlib package.
# 

# In[18]:


from pylab import plot, show


# The first argument to the plot() function is the list of numbers we want to plot on the x-axis, and
# the second argument is the corresponding list of numbers we want to plot on the y-axis. The plot()
# function returns an object. This object contains the information about the graph that we asked 
# Python to create. At this stage you can add more information, such as title, to the graph, or you can
# just display the graph as it is. We have to call the show() function.

# In[19]:


plot(x,y)
show()


# Notice that instead of starting from irigin (0) the x-axis starts from number 1 and the y-axis from
# the number 4, these are the lowest numbers from each of the two lists.

# If you want the graph to mark the points that you supplied for plotting, you can use an additional
# keyword argument while calling plot() function - marker = 'o'. You can choose from several marker
# options, including 'o', '*', 'x', '+'

# In[20]:


plot(x,y, marker ='o')
show()


# Using marker = includes a line connecting the points(this is the default). You can also make a graph
# that marks only the points that you specified, without any line connecting them, by omitting marker=

# In[21]:


plot(x,y, 'o')
show()


# When you use plot() on a single list, those numbers are automically plotted on the y-axis. The
# corresponding values on the x-axis are filled in as the positions of each value in the list.

# In[22]:


plot(x, marker='o')


# Matplotlib keeps track of what plots haven't been displayed yet. So as long as we wait to call
# show() until after we call plot() all the times, the plots will all get displayed on the same graph.

# ## 1.2 COMPARING GRAPHS

# In[23]:


plot(x, marker='o')
plot(y, marker ='o')
show()


# However, we don't have any clue as to which color corresponds to which list. To fix this we can use
# the function legend()

# In[24]:


from pylab import legend


# In[25]:


plot(x, marker='o')
plot(y, marker ='o')
legend(['Lista X','Lista Y'])
show()


# You can also specify a second argument of the function legend() that will specify the position of the
# legend. You can specify a particu;ar positions such as 'lower center', 'center left', 'upper left'. Or you
# can set the position to 'best', and the legend will be positioned so as not to interfere with the graph.

# ## 1.3 READING DATA FROM FILES

# Let's read the user data from a file. We'll see a simple example of how we can read numbers from a
# file and perform mathematical operations on them. In most cased data is stored in the well-known
# CSV format

# A comma-separated value (CSV) file consists of rows and columns with the columns separated from
# each other by commmas. 

# In[26]:


import pandas as pd


# In[27]:


df=pd.read_csv('Salary.csv', sep=',')


# In[28]:


type(df)


# List first 5 records

# In[29]:


df.head(5)


#  List last 5 records

# In[30]:


df.tail()


# Data Frame data types:
# 
# - object - string - The most general dtype. Will be assigned to your column if column has mixed
# types (numbers and strings).
# - int64 - int - Numeric characters. 64 refers to the memory allocated to hold this character.
# - float64 - float - Numeric characters with decimals. If a column contains numbers and NaNs,
# pandas will default to float64, in case your missing value has a decimal.
# - datetime64, timedelta[ns] - Values meant to hold time data.

# In[31]:


df.dtypes


# ## 1.4 SELECTING A COLUMN IN A DATAFRAME

# Method 1: subset the data frame using column name:

# In[32]:


df['Salary']


# Method 2: use the column name as an attribute:

# In[33]:


df.Salary


# There is a number of pandas commands to read other data formats:

# In[34]:


#pd.read_excel('myfile.xlsx',sheet_name='Sheet1', index_col=None, na_values=['NA'])
#pd.read_stata('myfile.dta')
#pd.read_sas('myfile.sas7bdat')


# In[35]:


plot(df['YearsExperience'],df['Salary'],'o')
show()


# ## 1.5 CUSTOMIZING GRAPHS

# We can add a title to our graph using the title() function and add labels for the x-axis and y-axes
# using xlabel() and ylabel()

# In[38]:


from pylab import title, xlabel, ylabel


# In[41]:


plot(df['YearsExperience'],df['Salary'],'o')
title('Relation between salary and years of experience')
xlabel('Years of experience')
ylabel('Salary')
show()


# So far we've allowed the numbers on both axes to be automatically determined by Python based
# on the data supplied to the plot() function. We can adjust the range of the axes the axis() function.

# In[43]:


from pylab import axis


# In[45]:


plot(df['YearsExperience'],df['Salary'],'o')
title('Relation between salary and years of experience')
xlabel('Years of experience')
ylabel('Salary')
axis(ymin=0,xmin=0)
show()


#  Similarly you can use xmin, xmax and ymax.

# If you need to save your graph you can do so using the savefig() function. You can choose among
# several image formats, including PNG, PDF, and SVG. Savefig() function has to be used before show().
# The program saves the graph to an image file in your current directory

# In[48]:


from pylab import savefig


# In[49]:


plot(df['YearsExperience'],df['Salary'],'o')
title('Relation between salary and years of experience')
xlabel('Years of experience')
ylabel('Salary')
axis(ymin=0,xmin=0)
savefig('nazwa_wykresu.jpg')
show()


# In[50]:


from pylab import tight_layout


# In[54]:


plot(df['YearsExperience'],df['Salary'],'o')
title('Relation between salary and years of experience')
xlabel('Years of experience')
ylabel('Salary')
axis(ymin=0,xmin=0)
tight_layout()
savefig('nazwa_wykresu.pdf')
show()


# ## 1.6 DESCRIBING DATA WITH STATISTICS
# 

# We'll use Python to explore statistics so we can study, describe and better understand sets of data.
# A large number of methods collectively compute descriptive statistics and other related operations
# on DataFrame: 
# - count() - number of non-null observations
# - sum() - sum of values
# - mean() - mean of values
# - median() - median of values
# - mode() - mode of values
# - std() - standard deviation of the values
# - min() - minimum value
# - max() - maximum value
# - cumsum() - cumulative sum
# 

# In[57]:


df.sum()


# The describe() function computes a summary of statistics pertaining to the DataFrame columns

# In[58]:


df.median()


# This function gives the mean, std and IQR values. And, function excludes the character columns and
# given summary about numeric columns. 'include' is the argument which is used to pass necessary
# information regarding what columns need to be considered for summarizing. Takes the list of values;
# by default, 'number':
# - object − summarizes String columns
# - number − summarizes Numeric columns
# - all − summarizes all columns together (Should not pass it as a list value)

# In[59]:


df.describe()


#  As you know Covariance and correlation measure of how much two variables change together

# In[60]:


df.cov()


# In[63]:


df.corr(method='spearman')


# ## 1.7 HISTOGRAM
# 
# A standard way to get started exploring a single variable is with the histogram. As we know the
# histogram divides the variable into bins, counts the data points in each bin, and shows the bins on
# the x-axis and the counts on the y-axis.
# 

# In[64]:


from pylab import hist


# In[66]:


hist(df.Salary)


# The binwidth is the most important parameter for a histogram and we should always try out a few
# different values of binwidth to select the best one for our data.

# In[67]:


hist(df.Salary, bins=15, color='steelblue', edgecolor='black')
show()


# In[73]:


hist(df.Salary, bins=15, color='steelblue', edgecolor='black', alpha=0.5)
show()


#  ## 1.8 BOXPLOT

# As we know a box plot is created to display the summary of the set of data values having properties
# like minimum, first quartile, median, third quartile and maximum. In the box plot, a box is created
# from the first quartile to the third quartile, a verticle line is also there which goes through the box at
# the median. Here x-axis denotes the data to be plotted while the y-axis shows the frequency
# distribution. The extreme lines shows the highest and lowest value excluding outliers.

# In[75]:


from pylab import boxplot


# In[76]:


boxplot(df.Salary)


# In[79]:


boxplot(df.Salary, vert=False)
show()


#  ## 1.9 SIMPLE LINEAR REGRESSION

# In[80]:


import statsmodels.api as sm


# In[81]:


y=df['Salary']


# In[82]:


X=df['YearsExperience']


# In[83]:


model_1=sm.OLS(y, X).fit()


# In[84]:


model_1.summary()


# In[93]:


X = sm.add_constant(X)


# In[96]:


model_2 = sm.OLS(y,X).fit()


# In[97]:


model_2.summary()


# In[99]:


prediction = model_2.predict(X)


# In[100]:


prediction.mean()


# In[101]:


df[['Salary']].mean()


# # 2. ADDITIONAL MATERIALS

# ## 2.1 FILTERING

# To subset the data we can apply Boolean indexing. This indexing is commonly known as a filter. For
# example if we want to subset the rows in which the salary value is greater than $30K: 

# In[ ]:





# Any Boolean operator can be used to subset the data:
# - '>' greater;
# - '>=' greater or equal;
# - < less;
# - <= less or equal;
# - == equal;
# - != not equal; 

# ## 2.2 SLICING

# There are a number of ways to subset the Data Frame:
# - one or more columns,
# - one or more rows,
# - a subset of rows and columns.
# 
# Rows and columns can be selected by their position or label.
# 
# When selecting one column, it is possible to use single set of brackets, but the resulting object will
# be a Series (not a DataFrame).

# In[ ]:





# When we need to select more than one column and/or make the output to be a DataFrame, we
# should use double brackets.

# In[ ]:





#  ## 2.3 SELECTING ROWS

# If we need to select a range of rows, we can specify the range using ":" 

# In[ ]:





# Notice that the first row has a position 0, and the last value in the range is omitted. So for 2:5 range
# 3 rows are returned with the positions starting with 2 and ending with 4.

# If we need to select a range of rows and/or columns, using their positions we can use method iloc

# In[ ]:





# ## 2.4 SORTING

# We can sort the data by a value in the column. By default the sorting will occur in ascending order
# and a new data frame is return. 

# In[ ]:





# # 3. SEABORN LIBRARY
# 

# An alternative way for different plots is seaborn library.

# In[ ]:





# A seborn package offers a density plot which is a continuous version of a histogram estimated from
# the data. The most common form of estimation is known as kernel density estimation. In this
# method, a continuous curve (the kernel) is drawn at every individual data point and all of these
# curves are then added together to make a single smooth density estimation. The kernel most often
# used is a Gaussian.

# In[ ]:




