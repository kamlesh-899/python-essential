#!/usr/bin/env python
# coding: utf-8

# # List
# 

# In[8]:


l1=[1,2,3,"kamlesh","karan","deep",[1,4,5]]


# In[14]:


print(l1)
l1[1] ##for indices 
l1[5]
print(l1[1])
print(l1[3])


# In[18]:


l1[-1] ## for negative index
l1[6][1] ## index of index


# In[22]:


l1[1:] ##Range 


# In[21]:


l1[:-2]


# In[25]:


l1[5]="python" ## change the value with index
print(l1)


# In[26]:


print(len(l1)) ## finding length of  list


# In[31]:


l1.append("fruits")##append is the function that add element in last of the list

l1.append("vegetables")
print(l1)


# In[34]:


l1.insert(0,"JAVA") ## insert in the function that add the value at the index in list
print(l1) 


# In[35]:


l1.remove(1) ## remove function is to remove the elment from the list in python
print(l1)


# In[36]:


l1.pop()
print(l1)


# In[38]:


l1.clear() ### its clear the whole list
print(l1)


# In[42]:


## additiopn of two list-
l2=[1,2,3,4]
l3=[5,6,78,78]
print(l2+l3)


# # TUPLES

# In[55]:


t1=("python","java","MYSQL","HTML")## creating tuples in round brackets
print(t1)
t2=(1,2,3,4,5)
print(t2)


# In[59]:


t1[1]
print(t1[1])           ## getting index in tuples
t1[0]
print(t1[0])
t1[3]
print(t1[3])
print(len(t1)) ## length in tuples


# In[56]:


t1+t2 ## addition of tuples


# In[58]:


x = ("apple", "banana", "cherry")
 ## for loop in tuples
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# 
# # DICTONARIES

# In[60]:


d1 = { "brand": "Ford","model": "Mustang","year": 1964}
print(d1)


# In[61]:


x = d1["model"]


# In[63]:


d1 = {
  "brand": "Ford",                
  "model": "Mustang",
  "year": 1964              ## changing the value
}
d1["year"] = 2018
d1


# In[64]:


d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in d1:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# In[65]:


print(len(d1))


# In[67]:



d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d1["color"] = "red"
print(d1)


# In[68]:


d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d1.pop("model")
print(d1)


# In[69]:


d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del d1["model"]
print(d1)


# In[70]:


d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d1.clear()
print(d1)


# In[72]:


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


# # SETS

# In[73]:


s1={1,2,3,"kamlesh","address","java",8,9,10}
s1


# In[75]:


s1 = {1,2,3,"kamlesh","address","java",8,9,10}

s1.add("orange")

print(s1)


# In[76]:


s1={1,2,3,"kamlesh","address","java",8,9,10}
## update the sets

s1.update(["orange", "mango", "grapes"])

print(s1)


# In[77]:


print(len(s1))


# In[78]:


s1 = {"apple", "banana", "cherry"}

s1.remove("banana")

print(s1)


# In[79]:


s1 = {1,2,3,"kamlesh","address","java",8,9,10}

x = s1.pop()

print(x)

print(s1)


# In[81]:


s1 = {1,2,3,"kamlesh","address","java",8,9,10}

s1.clear()

print(s1)


# In[82]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# In[83]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# # STRINGS

# In[84]:


a=("Basics of python")
a


# In[85]:


a=("Beginner of python "+"advance of python")
a


# In[86]:


b="hello world"    ##getting index in string
b[1]


# In[87]:


a = " Hello, World! "
print(a.strip())


# In[88]:


a = "Hello, World!"
print(a.replace("H", "J"))


# In[90]:


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


# In[91]:


a = "Hello"
b = "World"
c = a + b
print(c)


# In[ ]:





# In[ ]:





# In[ ]:




