#!/usr/bin/env python
# coding: utf-8

# In[1]:


bs=int(input("Enter the basic salary\n"))
if bs>=5000:
    hra=bs*(15/100)
    da=bs*(150/100)
    gs=bs+hra+da
    print("Hra is\n",hra,"\n Da is\n",da,"\n The gross salary is\n",gs)
else:
    hra=bs*(10/100)
    da=bs*(110/100)
    gs=bs+hra+da
    print("Hra is\n",hra,"\n Da is\n",da,"\n The gross salary is \n",gs)


# In[ ]:




