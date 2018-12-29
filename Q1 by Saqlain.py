#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=input("Enter the four digit number\n")
m=0
n=0
p=0
for x in a:
    if int(x)==0:
        m+=1
    elif int(x)%2==0:
        n+=1
    else:
        p+=1
print("No. of zero is\n",m)
print("No. of even is\n",n)
print("No. of odd is\n",p)
        


# In[ ]:




