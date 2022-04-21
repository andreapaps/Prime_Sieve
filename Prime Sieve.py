#!/usr/bin/env python
# coding: utf-8

# In[2]:


def make_list(num):
    return list(range(3,num+1))

make_list(10)


# In[8]:


def divides(num1,num2):
    return num2 % num1 == 0


# In[11]:


def add_to_list(item,my_list):
    return my_list.append(item)


# In[ ]:





# In[ ]:





# In[27]:


#Prime Sieve

number = 1000
number_list = make_list(number)
primes = [2]
potential_primes = []

while len(number_list) > 1:
    for i in number_list:
        if divides(primes[-1],i) == False:
            add_to_list(i,potential_primes)
            
            
    number_list = potential_primes
    add_to_list(number_list[0],primes)
    potential_primes = []
            

print(f'The primes are {primes} and there are {len(primes)} prime numbers')
            
            


# In[ ]:




