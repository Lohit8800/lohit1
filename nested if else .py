#!/usr/bin/env python
# coding: utf-8

# In[18]:


# IF else statement
salary=int(input("Enter THe salary "))
if salary >1000:
    print("You salary is good ")
    if salary <5000:
        print("I will go with nano car ")
        if True:
            print("false code")
    elif salary <10000:
        print("I will go with maruti car")
    elif salary <50000:
        print("I will go with toyta car ") 
    elif salary >50000:
            print("I will go with range rover")
    else :
        print("I will rent a car")
elif salary >500:
    print ("I will go with bike")
elif salary >100:
    print ("I will continue with bicycle")
else:
    print("I will go for saving")


# In[32]:


total =0
if a in range(2,25):
    print(a*a)
    total=total+(a*a)
print("The total value is ",total)    


# In[6]:


list(range(10,-5,-1))


# In[7]:


l=("hi how are you")


# In[8]:


l


# In[16]:


l[::-1]


# In[73]:


n=int(input ("Enter the number "))
for i in range(0,n):

    print('hi')    


# In[67]:


n=int(input ("Enter the number "))
while n>0:
    print ("8",n," ",2*n-1)


# In[77]:


t=(4,5,5,5,5,48454,4549866,487,45,45,47,8698,4654684,84,7465,5,4,"hi")


# In[78]:


s=set(t)


# In[79]:


s


# In[81]:


t[::-1]


# In[5]:


t=(3,4,4,5,6,6,7,7)


# In[95]:


for i in range(len(t)-1,-1,-1) :
    print(t[i])


# In[2]:


a=7
while a<7:
    pass


# In[6]:


for i in range (len(t)-1,-1,-1):
    print(t[i])


# In[ ]:


study_hour =float (input("Enter the numbers of years"))
if study_hour<2:
    print('you have to study well')
elif study_hour<4:
    print ('You should increse the study time')
elif study_hour>=6:
    print ('Go with the flow')
else:
    print("study well")


# In[ ]:




