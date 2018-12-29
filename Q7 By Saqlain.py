#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("Enter the number\n"))
sum=0
while(num>0):
    dig=num%10
    sum=sum+dig
    num=num//10
print("The total sum of the digit is\n",sum)


# In[ ]:




