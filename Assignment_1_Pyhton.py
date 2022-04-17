#!/usr/bin/env python
# coding: utf-8

# # PROGRAM TO FIND FACTORIAL OF A NUMBER

# In[1]:


#Python program to find the factorial of a number provided by the user.
num= int(input("enter a number:"))
fac= 1
for i in range(1,num+1):
    fac=fac*i
print("factorial of",num,"is",fac)  


# # Program to find whether a number is prime or composite

# In[2]:


n= int(input("Enter any number:"))
if (n==0 or n==1):
    printf(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"is not prime but composite number")
            break
    else:
        print(n,"number is prime but not composite number")
else:
        print("Please enter positive number only ")
    


# # Program to check whether a given string is palindrome or not.

# In[5]:


def isPalindrome(a):
    return a == a[::-1]
a = "malayalam"
ans = isPalindrome(a)

if ans:
    print("Yes")
else:
    print("No")


# # Program to get the third side of right-angled triangle from two given sides.

# In[6]:


import math
a = float(input("Enter base: "))
b = float(input("Enter height: "))
x = float(input("Enter angle: "))

c = math.sqrt(a ** 2 + b ** 2)

print("Hypotenuse =", c)


# # Program to print the frequency of each of the characters present in a given string

# In[7]:


string1 = input ("Enter the string: ")
d = dict()
for c in string1:
    d[c] = d.get(c, 0) + 1
print(d)


# In[ ]:




