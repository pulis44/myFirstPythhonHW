#!/usr/bin/env python
# coding: utf-8

# # Problem 1

# In[1]:


2 + 3


# # Problem 2

# In[2]:


print("hello world!")
print("hello world!")
print("hello world!")
print("hello world!")


# # Problem 3

# In[3]:


1 + 2


# # Problem 4

# In[25]:


x = 4 
y = x + 1 
x = 2 
print(x , y)


# # Problem 5

# In[4]:


x, y = 2, 6
x, y = y, x + 2
print(x, y)


# # Problem 6

# In[5]:


a, b = 2, 3
 c, b = a, c + 1
print(a, b, c)


# # Problem 7

# In[6]:


numcalls = 0
def square(x) :
    global numcalls
    numcalls = numcalls + 1
    return x * x
print(square(5))
print(square(2*5))


# # Problem 8

# In[7]:


x = 1
def f() :
    return x
print (x)
print (f ())


# # Problem  9

# In[8]:


x = 1
def f() :
    x = 2
    return x
print (x)
print (f())
print (x)


# # Problem 10

# In[1]:


x = 1
def f():
    global x # assign x to global variable
    y = x
    x = 2
    return x + y
print()
print(f())
print(x)


# # problem 11

# In[10]:


x = 2
def f (a) :
    x = a * a
    return x
y = f (3)
print (x,y)


# # Problem 12

# In[ ]:


count_digits(5)


# # Problem 13

# In[3]:


def istrcmp(a,b):
    return a.upper() == b.upper()


# In[4]:


istrcmp('python', 'Python')


# In[5]:


istrcmp('LaTeX', 'Latex')


# In[6]:


istrcmp('a', 'b')


# # Problem 14

# In[11]:


print 2 < 3 and 3 > 1
print 2 < 3 or 3 > 1
print 2 < 3 or not 3 > 1


# # Problem 15

# In[12]:


x = 4
y = 5
p = x < y or x < z
print(p)


# # Problem 16

# In[13]:


True, False = False, True :
print (True,False)
print (2<3)


# # Problem 17

# In[14]:


x = 2
if x == 2:
    print(x)
else:
    print(x)


# # Problem 18

# In[7]:


x=2
if x == 2:
    print (x) 
else:
    x +


# # Problem 19

# In[16]:


python add.py 3 5
python add.py 2 9


# # Problem 20

# In[17]:


x = [0,1,[2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x) 


# # Problem 21

# In[18]:


sum([1,2,3])


# # Problem 22

# In[19]:


sum(["hello","world"])
sum(["aa","bb","cc"])


# # Problem 23

# In[8]:


def product(ListA):
    product = ListA[0]
    for i in range(1,len(ListA)):
        product *= ListA[i]
    return product


# In[9]:


product([1,2,3])


# # Problem 24

# In[10]:


def product(ListA):
    product = ListA[0]
    for i in range(1,len(ListA)):
        product *= ListA[i]
    return product

def factorial (x):
    return product(list(range(1,x+1)))
factorial(4)


# # Problem 25

# In[15]:


def reverse(ListA):
    reverse = []
    for i in range(len(ListA),0,-1):
        reverse.append(ListA[i-1])
    return reverse


# In[16]:


reverse([1,2,3,4])


# In[17]:


reverse(reverse([1,2,3,4]))


# # Problem 26
# 

# In[27]:


def mymin(k):
    a = k.pop(0)
    for i in k:
        if i < a: a = i
    return a
mymin([20,13,60])


# In[29]:


def mymax(k):
    a = k.pop(0)
    for i in k:
        if i > a: a = i
    return a
mymax([20,13,60])


# # Problem 27

# In[18]:


def cumulative_sum (listnew):
    a = [listnew[0]]
    for i in range(1,len(listnew)):
        a += [listnew[i]*a[i-1]]
    return a    


# In[19]:


cumulative_sum([1,2,3,4])


# In[20]:


cumulative_sum([4,3,2,1])


# # Problem 28

# In[21]:


def cumulative_product(listnew):
    a = [listnew[0]]
    for i in range(1,len(listnew)):
        a += [listnew[i]*a[i-1]]
    return a    


# In[23]:


cumulative_product([1,2,3,4])


# In[24]:


cumulative_product([4,3,2,1])


# # Problem 29

# In[ ]:


unique([1, 2, 1, 3, 2, 5])


# # Problem 30

# In[ ]:


dups([1, 2, 1, 3, 2, 5])


# # Problem 31

# In[ ]:


group([1, 2, 3, 4, 5, 6, 7, 8, 9,], 3)


# # Problem 32

# In[ ]:


lensort(['python', 'perl', 'java', 'c', ''])


# # Problem 33

# In[ ]:





# # Problem 34

# In[ ]:





# # Problem 35

# In[ ]:


extsort (['a.c', 'a.py', 'b.py', 'bar.txt',  'foo.txt', 'x.c'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




