### 1. find the common elements of two list

# a = [1,2,3,3,"potato","sweet","tomato",45,58 ]
# b = [14,23,3,3,"lulu","sweet","apple",45,55 ]

# m_set = set(a).intersection(set(b))
# print(list(m_set))

## alternative way
# def comm(x,y):
#     c_list = []
#     for i in a :
#         if i in b and i not in c_list:
#             c_list.append(i)
#     return c_list
# print(comm(a,b))

## alternative way using list comprehension
# def com_c (x,y):
#     return[i for i in a if i in b] # returns duplicate values in same lists
# print(com_c(a,b))

### 2. Find the Most Frequent Element in a List? 
# numbers = [1,2,2,3,3,3,4,7,7,7,7]

# def most_freq(lst):
#     max_count = 0 
#     most_freq = None 
#     for item in lst:
#         count = lst.count(item)
#         if count > max_count:
#             max_count = count 
#             most_freq = item 
#     return most_freq 

# print(most_freq(numbers))

### 3. Find Cumulative Sum of a List
# numbers = [1, 2, 3, 4]

# def cumulative_sum(lst):
#     cum_sum = [] 
#     total = 0 
#     for num in lst: 
#         total += num 
#         cum_sum.append(total) 
#     return cum_sum 
# print(cumulative_sum(numbers))

### alternative Using List Comprehension: 
# print([sum(numbers[:i + 1]) for i in range(len(numbers))]) 

### 4. remove duplicates from a list
## using loops
# f_list = ["apple", "banana", "cherry", "banana", "orange"]
# def r_d (x):
#     basket = []
#     for i in f_list:                
#         if i not in basket:
#             basket.append(i)
#         else:
#             pass
#     return basket
# print(r_d(f_list))

## alternative - using set constructor
# print(list(set(f_list)))

### 5. find the index of an element in tuple
# ttt = ('a', 'b', 'c', 'd')
# def i_t (tpl, ele):
#     return tpl.index(ele) if ele in tpl else "invalid"
# print(i_t(ttt, 'd'))

### 6. find the most frequent value in dictionary

# data = {'a':1, 'b':2, 'c': 1, 'd':3, 'e':1}
# def fre(d):
#     m_fre = None
#     m_cou = 0
#     cou = 0
#     for i in d.values():
#         cou = list(d.values()).count(i)
#         if cou > m_cou:
#             m_cou = cou
#             m_fre = i
#     return m_fre
# print(fre(data))

### 7. merge dictionary with summation
# dic1 = {'a': 10, 'b': 20, 'c': 30}
# dic2 = {'b': 15, 'c': 35, 'd': 25, 'e': 12}

# def merge_dic(x,y):
#     result = x.copy()
#     for key,value in y.items():
#         if key in result:
#             result[key] += value  # here key means 'value' of that key
#         else:
#             result[key] = value   # here key means 'value' of that key
#     return result

# print(merge_dic(dic1,dic2))

### 8. flatten a nested dictionary  - #output: {a.b.c: 42, a.d: 7, e:10} - {not fully clear}

# ddd = {'a':{'b':{'c':42}, 'd':7}, 'e':10}

# def flatten_dic (ddd, parent_key = '', sep = '.'): 
#     items = {}
#     for key, value in ddd.items():
#         new_key = f'{parent_key}{sep}{key}' if parent_key else key
#         if isinstance(value,dict):   # If the value is a dictionary, recursively call flatten_dic
#             items.update(flatten_dic(value, new_key, sep))  # recursion and update
#         else:
#             items[new_key] = value
#     return items
# print(flatten_dic(ddd))

### 9. sort dictionary by values

# dicc = {'a':20,'b':50,'c':10,'d':40,'e':30}

# def s_dic_v(x):
#     sorted_items = sorted(x.items(), key = lambda item : item[1])
#     return {key: value for key, value in sorted_items}
# print(s_dic_v(dicc))

## alternative
# def s_dic(x):
#     v = sorted(x.items(), key=  lambda i: i[1] )
#     return dict(v)
# print(s_dic(dicc))

### 10. access values from nested dictionary .   Retrieve- (42, target,77)
# data = {
#     "level1":{
#         "level2":{
#             "level3":{
#                 "value1": 10,
#                 "value2": [1,2,{'deep_key':42}],
#                 "value3": {"inner_key": "target"}  
#             },
#             "other_key": 99    
#         },
#         "list_key":[
#             {"list_inner_key1": 88},
#             {"list_inner_key2": {"deep_list_key":77}}
#         ]
#     }
# }

# ## for 42
# print(data['level1']['level2']['level3']['value2'][2]['deep_key'])

# ## for "target"
# print(data['level1']['level2']['level3']['value3']['inner_key'])

# ## for 77
# print(data['level1']['list_key'][1]['list_inner_key2']['deep_list_key'])
