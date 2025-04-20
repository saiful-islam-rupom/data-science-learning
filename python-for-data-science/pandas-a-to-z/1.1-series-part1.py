########## pandas datatype/object - series ############### - in series, there are two things - index,value
import numpy as np           # best practice to import numpy when we use pandas
import pandas as pd

### create series from 'list' ###

# country = ['Bangladesh','Germany', 'Italy','France','Austria'] #for string
# print(pd.Series(country)) # it sets the string as an object datatype

# runs = [23,12,45,66,24,89] # for integer
# print(pd.Series(runs)) 

### create custom index ###

# marks = [67,89,56,77]
# subjects = ['Maths','Physics','Chemistry','Biology']

# print(pd.Series(marks, index=subjects)) # setting custom index

# print(pd.Series(marks,index=subjects,name="Saiful's final result")) #  setting additional information

#### create series from 'dictionary' #####

# final_result = {
#     'Maths':67,
#     'Physics':89,
#     'Chemistry':56,
#     'Biology':77
# }
# print(pd.Series(final_result))   # easy to create custom index from dictionary - directly
# print(pd.Series(final_result, name='My final result'))

########## sereis - attributes ############

### size ### - to find how many items in the series - it count both null and not-null values
# marks = [67,89,56,77]
# subjects = ['Maths','Physics','Chemistry','Biology']
# result = pd.Series(marks,index=subjects,name="Saiful's final result")

# print(result.size) # there are 4 items

### dtype ### - to find the data type of the sereis
# print(result.dtype)

### name ### - to find out the additional information(name)
# print(result.name)

### is_unique ### - to find out all the items are unique or not -one(T/F)
# print(result.is_unique)

### index ### - to find out the index object(indexes)
# print(result.index)

# runs = [23,12,45,66,24,89] 
# runs_ser = pd.Series(runs)
# print(runs_ser.index)

### values ### - to find out the values from series
# print(result.values)

########## creating series from csv file - read_csv ###########- (real life data)
### subs - subscribers per day for 365 days
# print(pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\subs.csv")) # when read csv file, it import data as dataframe by default
# print(type(pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\subs.csv")))

# dfs = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\subs.csv")
# sers = dfs.squeeze()  # .squeeze() - convert into series from dataframe
# print(sers)
# print(type(sers))

### kohli_ipl - 215 matches with runs
# print(pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv")) # reading the raw data
# print(pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")) # setting index_col

# dfk = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")
# serk = dfk.squeeze() # convert into series from dataframe
# print(serk)

### bollywood - about 1500 movies name with their main actor
# print(pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\bollywood.csv"))
# dfb = pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\bollywood.csv",index_col='movie')
# print(dfb)
# print(dfb.squeeze()) # convert into series from dataframe

################ series methods ####################
##### .head() and .tail() -  to get the preview of some top(head) and bottom(tail) items

### .head() ###
# dfk = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")
# serk = dfk.squeeze()
# print(serk.head()) # default is top of 5 items
# print(serk.head(7)) # custom number of top items

### .tail() ###
# print(serk.tail()) # default is bottom of 5 items
# print(serk.tail(3))# custom number of bottom items

### .sample() ### - randomly shows item/row as sample
# print(serk.sample()) # default is 1 random sample
# print(serk.sample(4)) # custom numbers of random sample

### .vaule_counts() ### - to get the frequency number of each and every values
# dfb = pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\bollywood.csv",index_col='movie')
# serb = dfb.squeeze()
# print(serb.value_counts()) # getting the frequency number of each and every values, discending order

### .sort_values() ### - sorting the values
# dfk = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")
# serk = dfk.squeeze()
# print(serk.sort_values()) # default sort - ascending
# print(serk.sort_values(ascending=False)) # sorting in discending order 
# print(serk.sort_values(ascending=False).head(1)) # to get the best run_score with match_no
# print(serk.sort_values(ascending=False).head(1).values) # to get only the best run_score in np array
# print(serk.sort_values(ascending=False).head(1).values[0]) # to get the best run_score only without any array - method chaining

## belows sortings are for dataframe object ##
# print(dfk.sort_values(by='runs')) # here we have to specify the column_name that we want to sort - default is ascending
# print(dfk.sort_values(by='runs',ascending=False)) # sorting in discending order
# print(dfk.sort_values(by='runs',ascending=False).head(1)) # to get the best run_score with match_no
# print(dfk.sort_values(by='runs',ascending=False).head(1).values) # to get the best run_score only in np array
# print(dfk.sort_values(by='runs',ascending=False).head(1).values[0]) # to get the best run_score only without any array - method chaining
# print(dfk)
# dfk.sort_values(by='runs',ascending=False,inplace=True) # inplace=True means it permanently changes the series/dataframe
# print(dfk)

### .sort_index() ### - sorting the indexes
# print(serk.sort_index()) # default is ascending
# print(serk.sort_index(ascending=False)) # sorting in discending order

# dfb = pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\bollywood.csv",index_col='movie')
# serb = dfb.squeeze()
# print(serb.sort_index()) # sorting by movie name (numbers,alphabets)

##### series - mathematical methods ####
### .count() ### - count the total number of rows/items in a seriese - it only count not-null values
# dfk = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")
# serk = dfk.squeeze()
# print(serk.count())

### .sum() ### - sum of all values
# dfs = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\subs.csv")
# sers = dfs.squeeze()
# print(sers.sum()) # total number of subscriber gained in 365 days

### .product() ### - product of all values / multiplication of all values
# print(sers.product())

### .mean() ### - to get the average of all values
# print(sers.mean()) # average number of subscriber gained per day

### .median() ### - to get the median value from the series
# print(sers.median())

### .mode() ### -  to get the most frequent value from the series
# print(sers.mode())

### .std() ### - to ger the standard diviation from the series values
# print(sers.std())

### .var() ### - to get the variance from the series values
# print(sers.var())

### .min() ### - minimum value of the series
# print(sers.min())

## .max() ### - maximum value of the series
# print(sers.max())

### .describe() ### - shows some of the important mathematical methods for a series - values
# print(sers.describe())


################# series indexing ############## - getting desired items using index from a series
### series do not usually perform negative indexing--- but if the indexes are 'strings'(custom), negative indexing can be performed
# x = pd.Series([12,34,54,33,543,36,13])
# print(x)
# print(x[2])

# dfk = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")
# serk = dfk.squeeze()
# print(serk)
# print(serk[1]) # when the custom indexes are numbers, it consider the custom one as index
# print(serk[-1]) # error - do not perform negative indexing

# dfb = pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\bollywood.csv",index_col='movie')
# serb = dfb.squeeze()
# print(serb)
# print(serb[2]) 
# print(serb['The Accidental Prime Minister (film)']) # indexing using labels

### fancy indexing ### - when there are no pattern in the desired indexes we use fancy indexing, ---same as numpy 
# print(serk[[1,4,212,213,215]])

####### series slicing ####### - same as python list slicing

# dfk = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")
# serk = dfk.squeeze()
# print(serk)
# print(serk[2:6]) # when about to slicing, it consider the integrated indexes only, do not consider the custom one
# print(serk[-5:]) # negative slicing, to find out the last 5 matches scores
# print(serk[-1::-1]) # reverse


#################### editing series ##########################

# marks = [67,89,56,77]
# subjects = ['Maths','Physics','Chemistry','Biology']
# final_xm = pd.Series(marks,index=subjects,name="Saiful's final result")
# print(final_xm)
# final_xm[2]=100     # edit marks/values
# print(final_xm)

# final_xm['Higher_Math'] = 99   # add/append new item/row that did not exist before
# print(final_xm)

# runs = [23,12,45,66,24,89] 
# player_runs = pd.Series(runs)
# print(player_runs)
# player_runs[2:5] = 100  # edit marks/values using slicing
# player_runs[2:5] = [98,99,100] # edit marks/values using slicing
# print(player_runs)

### we can also edit using fancy indexing
### we can also edit using labels

######### copy and views in series ####### - if I change /modify in view, it will also change the main value. To get rid from that, we can use copy() and modify there
# dfk = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")
# serk = dfk.squeeze()

# print(serk)

# new = serk.head(5).copy()
# new[1] = 0
# print(new)

# print(serk)

############ series with python core functionalities ################
## can use len/type/dir/sorted/max/min - also applicable in pandas

# dfs = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\subs.csv")
# sers = dfs.squeeze()

# print(len(sers))
# print(type(sers))
# print(dir(sers))   # dir - shows all the methods and attributes of a series
# print(sorted(sers)) # sorted - sort all the values in a 'list'
# print(max(sers))
# print(sers.max())


## can use type conversion
# print(list(final_xm))   # convert the values into list
# print(dict(final_xm)) # convert the values into dictionary

## can use membership operator - in - 
# dfb = pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\bollywood.csv",index_col='movie')
# serb = dfb.squeeze()
# print(serb)
# print('Hum Tumhare Hain Sanam' in serb) 
# print('Anupam Kher' in serb)   # by default, it only consider the indexes, not values. That's why it shows false here
# print('Anupam Kher' in serb.values) # we have to add .values to consider values.

## can use loop (for/while)
# for i in serb:
#     print(i)  # print the values by default

# for i in serb.index: # customize it to print indexes
#     print(i)  

## can use arithmetic operator (Broadcasting)
# print(100 - final_xm) # to know, how marks should need to fullfill 100 for each subjects

## can use relational operator
# print(final_xm >= 70)

################ Boolean indexing on series #######################
# dfk = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\kohli_ipl.csv",index_col="match_no")
# serk = dfk.squeeze()
# print(serk)
##?? find the matches where vk got 49+ runs
# print(serk >= 50) # find the boolean values
# print(serk[serk >= 50]) # find the original true values only - by filtering
# print(serk[serk >= 50].size) # find- how many matches vk got 49+ runs

##? find the number of matches vk got ducks (0)
# print(serk[serk == 0].size) # ans- 9 matches

##? count the number of days where I got 199+ subscriber each day
# dfs = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\subs.csv")
# sers = dfs.squeeze()
# print(sers)
# print(sers[sers >= 200].size) # ans- 59 days

##? find actors who have done more than 20 movies
# dfb = pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\bollywood.csv",index_col='movie')
# serb = dfb.squeeze()
# print(serb)

# print(serb.value_counts())
# nma = serb.value_counts()
# print(nma[nma > 20]) # the actors who have done 20+ movies
# print(nma[nma > 20].size) # the number of actors who have done 20+ movies

################# Plotting graphs on series ###########################
# import matplotlib.pyplot as plt
# dfs = pd.read_csv("E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\subs.csv")
# sers = dfs.squeeze()
# # print(sers)
# plt.plot(sers) # for normal 2D graph
# plt.show()

# dfb = pd.read_csv(r"E:\Learn_Data_Science\Python_For_Data_Science\Pandas_Folder\Datasets_For_Pandas\bollywood.csv",index_col='movie')
# serb = dfb.squeeze()
# print(serb.value_counts().head(30))
# serb.value_counts().head(30).plot(kind='bar')  # kind='bar' is for creating bar plot
# serb.value_counts().head(10).plot(kind='pie')  # kind='pie' is for creating pie chart
# plt.show()

##------------ to continue, go to jupyter notebook