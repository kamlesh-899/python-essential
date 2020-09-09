#!/usr/bin/env python
# coding: utf-8

# # assignment 2

# # list
# 

# In[ ]:


l1=[1,2,3,"kamlesh","karan","deep",[1,4,5]]


# In[ ]:


print(l1)
l1[1] ##for indices 
l1[5]
print(l1[1])
print(l1[3])


# In[ ]:


l1[-1] ## for negative index
l1[6][1] ## index of index


# In[ ]:


l1[1:] ##Range 


# In[ ]:


l1[:-2]


# In[ ]:


l1[5]="python" ## change the value with index
print(l1)


# In[ ]:


print(len(l1)) ## finding length of  list


# In[ ]:


l1.append("fruits")##append is the function that add element in last of the list

l1.append("vegetables")
print(l1)


# In[ ]:


l1.insert(0,"JAVA") ## insert in the function that add the value at the index in list
print(l1) 


# In[ ]:


l1.remove(1) ## remove function is to remove the elment from the list in python
print(l1)


# In[ ]:


l1.pop()
print(l1)


# In[ ]:


l1.clear() ### its clear the whole list
print(l1)


# In[ ]:


## additiopn of two list-
l2=[1,2,3,4]
l3=[5,6,78,78]
print(l2+l3)


# # TUPLES

# In[ ]:


t1=("python","java","MYSQL","HTML")## creating tuples in round brackets
print(t1)
t2=(1,2,3,4,5)
print(t2)


# In[ ]:


t1[1]
print(t1[1])           ## getting index in tuples
t1[0]
print(t1[0])
t1[3]
print(t1[3])
print(len(t1)) ## length in tuples


# In[ ]:


t1+t2 ## addition of tuples


# In[ ]:


x = ("apple", "banana", "cherry")
 ## for loop in tuples
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# 
# # DICTONARIES

# In[ ]:


d1 = { "brand": "Ford","model": "Mustang","year": 1964}
print(d1)


# In[ ]:


x = d1["model"]


# In[ ]:


d1 = {
  "brand": "Ford",                
  "model": "Mustang",
  "year": 1964              ## changing the value
}
d1["year"] = 2018
d1


# In[ ]:


d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in d1:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# In[ ]:


print(len(d1))


# In[ ]:



d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d1["color"] = "red"
print(d1)


# In[ ]:


d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d1.pop("model")
print(d1)


# In[ ]:


d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del d1["model"]
print(d1)


# In[ ]:


d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d1.clear()
print(d1)


# In[ ]:


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

# In[ ]:


s1={1,2,3,"kamlesh","address","java",8,9,10}
s1


# In[ ]:


s1 = {1,2,3,"kamlesh","address","java",8,9,10}

s1.add("orange")

print(s1)


# In[ ]:


s1={1,2,3,"kamlesh","address","java",8,9,10}
## update the sets

s1.update(["orange", "mango", "grapes"])

print(s1)


# In[ ]:


print(len(s1))


# In[ ]:


s1 = {"apple", "banana", "cherry"}

s1.remove("banana")

print(s1)


# In[ ]:


s1 = {1,2,3,"kamlesh","address","java",8,9,10}

x = s1.pop()

print(x)

print(s1)


# In[ ]:


s1 = {1,2,3,"kamlesh","address","java",8,9,10}

s1.clear()

print(s1)


# In[ ]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# In[ ]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# # STRINGS

# In[ ]:


a=("Basics of python")
a


# In[ ]:


a=("Beginner of python "+"advance of python")
a


# In[ ]:


b="hello world"    ##getting index in string
b[1]


# In[ ]:


a = " Hello, World! "
print(a.strip())


# In[ ]:


a = "Hello, World!"
print(a.replace("H", "J"))


# In[ ]:


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


# In[ ]:


a = "Hello"
b = "World"
c = a + b
print(c)


# # Assignment 3

# In[13]:


pilot=number

if(number  <1000):
   num =int(input("Enter the number"))
   print("Pilot want to land the plane at 1000 feet")
elif(number  >5000):
   num =int(input("Enter the feet"))

   print("pilot want to land the plane at 4500 feet")
else:
   num =int(input("Enter the feet"))

   print("pilot want to land the plane at 6500 feet")


# In[1]:


for Number in range (1, 200):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')


# # Asssignment no 3 

# In[14]:


num =int(input("Enter the number"))



sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# # Assignment no 5

# In[18]:



l1 = [9, 4, 5, 8, 10] 
sub_list = [10, 5, 4] 
 

print ("Original list : " + str(l1)) 
print ("Original sub list : " + str(sub_list)) 
 

flag = 0
if(all(x in l1 for x in sub_list)): 
   flag = 1

if (flag) : 
   print ("Yes,  it is match.") 
else : 
   print ("No, no it is not match.")


# In[20]:


def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

fltrObj=filter(isPrime, range(2500))
print ('Prime numbers between 1-10:', list(fltrObj))


# # Assignment 6

# In[21]:



import math 
pi = math.pi 
  

def volume(r, h): 
    return (1 / 3) * pi * r * r * h 
  

def surfacearea(r, s): 
    return pi * r * s + pi * r * r 

radius = float(5) 
height = float(12) 
slat_height = float(13) 
print( "Volume Of Cone : ", volume(radius, height) ) 
print( "Surface Area Of Cone : ", surfacearea(radius, slat_height) ) 


# In[23]:


class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
  


# In[24]:



s = Bank_Account() 
   

s.deposit() 
s.withdraw() 
s.display() 


# In[ ]:




