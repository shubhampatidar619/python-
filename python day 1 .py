#!/usr/bin/env python
# coding: utf-8

# In[1]:


#string 
s = "shubham"
print(s)


# In[2]:


print(s[4])


# In[3]:


# lenth of any string 
print(len(s))


# In[4]:


# absolute function
m=-15
print(abs(m))


# In[5]:


l="hello world!"
l[0:7]


# In[6]:


l[7:]


# In[7]:


u="i love india"
u[7:]


# In[8]:


u[::-1]


# In[9]:


# min function
j=10,12,15
min(j)


# In[10]:


max(j)


# In[11]:


0.1+0.2==0.3


# In[12]:


(0.1+0.2)==0.3


# In[13]:


0.1+0.2


# In[14]:


(43.55+2/2)


# In[15]:


2**(3**2)


# In[16]:


2**3**2  


# In[17]:


(2**3)**2


# In[18]:


n=int(input("enter the number"))
if n%2==1:
    print('Weird')
elif n%2==0 and 2 <= n <=5:
    print('not weird')
elif n%2==0 and 6 <= n <=20:
    print(' weird')
elif n%2==0 and n >20:
    print('not weird')


# In[19]:


a = int(input())
b = int(input())

sum=a+b
print(sum)
sub=a-b
print(sub)
multi=a*b
print(multi)


# In[20]:


a = int(input())
b = int(input())

div=a//b
print(div)

floatdiv= a/b
print(floatdiv)


# In[21]:


n = int(input())

for i in range (n):
    squre=i**2
    print(i,  squre)    


# In[22]:


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input())
print(is_leap(year))


# In[23]:


n = int(input("Enter a number: "))

for i in range(1, n+1):
   print(i,end='')

   


# ## for loop

# In[24]:


for i in range (10):
    print("shubham")


# In[25]:


# step value
for j in range (1, 30 , 3):
    print(j)


# In[26]:


#without range 


w="shubhampatidar"
for i in w:
    print(w)


# In[27]:


w="shubhampatidar"
for i in w:
    print(i)


# In[28]:


# table of 5


for i in range(5,51,5):
    print(i)


# In[29]:


# table of 18


for i in range(1,11):
    print(i*18)


# In[31]:


#table 1 to 20

for i in range (1,11):
    for j in range (1,21):
        print(i*j, end="\t")
    print()


# In[30]:


#table 1 to 20

for i in range (1,11):
    for j in range (1,11):
        print(i*j, end=" ")
    print()


# In[5]:


# pattern 


for i in range (1,6):
    for j in range (1,i+1):
        print(j, end="")
    print()


# In[6]:


# pattern 


for i in range (1,6):
    for j in range (1,i+1):
        print(i, end="")
    print()


# In[9]:


for i in range (1,6):
    for j in range (1,i+1):
        print(j, end=' ')
    for k in range (1,i-1):
        print(k, end=" ")
    print()


# ## while loop

# In[1]:


f=0
while (f<10):
    print("abc")
    f=f+1
    


# In[12]:


## BREAK STATEMENT

for i in range (10):
    if i==4:
        break
    print(i)


# In[13]:


## continue STATEMENT

for i in range (10):
    if i==4:
        continue
    print(i)


# In[28]:


m=str("shubham")
for i in m:
    if i=='a':
        break
    print(i)  


# In[29]:


m=str("shubham")
for i in m:
    if i=='a':
        continue
    print(i)  


# In[2]:


# Write your code here
first_name=str(input())
last_name=str(input())

full = f" Hello {first_name} {last_name}! You just delved into python."
print(full)


# In[1]:


def print_full_name(first_name, last_name):
    full = f"Hello {first_name} {last_name}! You just delved into python."
    print(full)

# Taking input for first and last names
first_name_input = input("Enter the first name: ")
last_name_input = input("Enter the last name: ")

# Calling the function with provided inputs
print_full_name(first_name_input, last_name_input)


# In[ ]:




