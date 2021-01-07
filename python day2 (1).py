#!/usr/bin/env python
# coding: utf-8

# # loops

# In[ ]:


# print numbers from 1 to 100


# In[ ]:


i=1
while i<101:
    print(i)
    i=i+1


# In[ ]:





# In[ ]:





# In[ ]:


i = 3 ## initialisation
while i < 7:   # while keyword (condition ):
  print(i)
  i += 1 # i=i+1


# In[ ]:


i = 1
j=3
while i < 6 or j<10:  # using the "and " keyword here , loop will only run when both the conditions are true
  print("i=",i,"j=",j)
  i += 1
  j=j+2


# In[ ]:


#for loop intro 
#syntax 
# for condition :
#     statements
# 3 parameters in range function  #(start,end,increment/increase)


for i in range (0,9,1):#default step size will be 1
    print(i)

    


# In[ ]:


for i in range(0,9,2): #( start=0, end =9, increment=2)
    print(i)


# In[ ]:


for i in range(9): # start  value will be automatically 0
    print(i)


# In[ ]:


animal="hippo"  #string to variable 
for i in animal:  #picks one charachter of a string everytime and prints it
    print(i)


# In[ ]:


sports=["football","cricket","basketball","volleyball"]  # list of strings 
for x in sports:    # picks one string at a time and prints it
    print(x)
    


# In[ ]:


for i in range (5):
    if i==2:  # if   statement in for loop
        pass     # pass is a do nothing keyword 
        print("pass executeed")
    else:
        print(i)


# In[ ]:


i = 3
while i < 8:
  print(i)
  if i == 5:
    print("break .... coming out of loop")  # "break" abruptly comes out of the loop even if the condition is true 
    break
  i += 1


# In[ ]:


i = 3
while i < 8:
  print(i)
  if i == 5:
    print("continue .... loop") # continue will skip the iteration IE the statements below continue wont be executed in loop
    continue
  print("hello")
  i += 1


# In[ ]:



#else while loop
i = 1
while i < 6:
  print(i)
  i += 1
else: 
  print("i is no longer less than 6")


# # list and it's functions

# In[ ]:


#list declaration
series=["Breaking_Bad","Broklyn99","MoneyHeist"]  

'''
here breaking_bad =series[0]
Broklyn99 =series[1]
moneyheist=series[2]

series has 3 elements ,so length of  list is 3 
'''
for x in series:
    print(x)


# In[ ]:


series=["Breaking_Bad","Broklyn99","MoneyHeist"]

# using .append() function here to insert a new element at the end of list
# now length of list will be 4 


series.append("FRIENDS")
for x in series:
    print(x)

print(len(series))


# In[ ]:


series.sort()

#sort the list of strings in alphabetical order 
#sort the list of integers/floats in ascending order
for x in series:
    print(x)


# In[ ]:


series.reverse()

# reverses the list 
for x in series:
    print(x)
    


# In[ ]:


# new way of displaying a list
#len is a function which returns length of list


for x in range (len(series)): # for x in range(0,4):
    print(series[x])


# In[ ]:


series.pop(1)

# pop function takes position as arguement and removes that element from list

for x in range (len(series)):
    print(series[x])


# In[ ]:


#returns minimum and maximum value of list

print(min(series))
print(max(series))


# In[ ]:


# .insert() takes 2 args (pos,ele)
   
series.insert(2,"hello") # listname.insert(position,element)
for x in range (len(series)):
   print(series[x])


# In[ ]:


#Q what if we try to sort this list


mixlist=["apple","orange",1,5,6,"banana",-2]
mixlist.sort()

for x in range (len(mixlist)):
    print(mixlist[x])


# In[ ]:


mixlist.reverse()
for x in range (len(mixlist)):
    print(mixlist[x])


# In[ ]:


print(min(mixlist))
print(max(mixlist))


# In[ ]:


list1=["hello","hi","hola"]
list2=["bye","welcome","bonjour","thankyou"]
list3=list2+list1

# using + sign  here ro make a new list which comprises of ele of lst 1 and 2  in order 
for x in range (len(list3)):
    print(list3[x])


# In[ ]:


list4=list1*3 

# using * sign to make a new list of size 3* repeating elements of list again and again
for x in range (len(list4)):
    print(list4[x])


# In[ ]:





# # dictionary 

# In[ ]:



#collection of key-value pairs

sample_dic = dict({1: 'Welcome', 2: 'to', 3:'SIT'}) #keyword dict
print("\n printing sample dictionary: ") 
print(sample_dic) 
  


# In[ ]:


fruit = dict({1: 'banana', 2: 'mango', 3:'apple',4:'pineapple'})
print(fruit)


# In[ ]:



my_dict = {'name': 'Jack', 'age': 26}

#way to access value using key in dictionary

print(my_dict['name'])
 

print(my_dict.get('age'))


print(my_dict.get('address'))

print(my_dict['address'])

#both methods are similar except in .get method we don't get error , we get output as none.
# so we prefer .get fucntion while handling  dictionary


# In[ ]:


#add element into dictionary

my_dict['address']="Mumbai"   # name-of-dictionary[key]=value
print(my_dict)


# In[ ]:


sumdictionary = {x: x+x for x in range(7)}  #{key: value, condition/loop}

print(sumdictionary)


# In[ ]:


# another way to decalre a dictionary

odd_squares = {x: x*x for x in range(8) if x % 2 == 1}

print(odd_squares)


# In[ ]:


squares = {}        #empty dictionary
for x in range(6):
    squares[x] = x*x 
print(squares)


# In[ ]:


#q how to print all the values
#print all the values
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])


# In[ ]:


# .fromkeys to intialise all the keys the same value
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)


# In[ ]:


#printing keys and values of dictionary

print(marks.keys())
print(marks.values())


# In[ ]:


#updating the value in dictionary 

marks['Math']=89
marks['English']=78
marks['Science']=94
marks['Social']=64
print(marks)


# In[ ]:


#.copy() will create a replica of the same dictionary into another one

newmarks=marks.copy()
print(newmarks)


# In[ ]:


#.clear() will erase all the contents ofdictionaryand dictionary will be empty

newmarks.clear()
print(newmarks)


# In[ ]:


# .popitem by default pops the last kkey value pair of the dictionary

newmarks=marks.copy()
newmarks.popitem()
#.poprint(newmarks)


# In[ ]:


#.pop()  removes the key value pair of the passed key 

newmarks.pop('English') 
print(newmarks)


# In[ ]:


#q


# # set and tuple

# tuple is immutable form of list 
# we can't sort the tuple 
# it is enclosed in paranthesis ()
# 

# In[ ]:




sampletuple=(1,4,5,8,4,5,2)
samplelist=[1,4,5,8,4,5,2]
for i in samplelist:
    print (i)
print("\n list ended \n tuple started")
for i in sampletuple:
    print(i)
print(sampletuple)


# In[ ]:


samplelist.sort()
print(samplelist)


# In[ ]:


sampletuple.sort()
print(sampletuple)


# In[ ]:


#convert list to tuple
list1=[1,5,8,0,3]
print(tuple(list1))


# In[ ]:


#string to tuple

st="hello"
t=tuple(st)
print (t)


# In[ ]:


# tuple can consist of int,char,string,list
#sample tuple of mixed datatypes
tuple1=(1,"hello",'h',[1,4,5])
print(tuple1)


# In[ ]:


SETS


# In[ ]:


sampleset={1,4,7,3,4,2,5,3,10,0,4}
print(sampleset)


# In[ ]:



# adding a new element into set using .add method
sampleset.add(100)
print(sampleset)


# In[ ]:


#removing element from set using .discard method

sampleset.discard(7)
print(sampleset)


# In[ ]:


#adding a list to a set
## we cannot add list to a set because list is mutable and set is immutable
sampleset.add([19,54,78])
print(sampleset)


# In[ ]:



#string is also immutable so we can add it to set

sampleset.add("hello")
print(sampleset)


# In[ ]:


# tuple also is immutable so we can add

sampleset.add((109,44,5,3))
print(sampleset)


# # list iterations

# In[ ]:


exlist=[1,2,4,5,6]
for i in exlist:
    print(i)


# In[ ]:


#another way of printing the list

for  i in range(0,len(exlist)):
    print(exlist[i])


# In[ ]:


for  i in range(2,len(exlist)-1):
    print(exlist[i])


# In[ ]:


for  i in range(0,len(exlist),2):
    print(exlist[i])


# In[ ]:


for  i in range(0,len(exlist)):
    if i==2:
        print(exlist[i])


# In[ ]:


for  i in range(0,len(exlist)):
    if exlist[i]==6:
        print(exlist[i])
        print("\n the element is 6")


# In[ ]:


#Q write  code to print even numbers
#fizzbuzz


# In[ ]:


origlist=[1,4,5,6,7,10,48]
duplist=[]
print(origlist[0:4:])
#[beginning : end : step]


# In[ ]:


print(origlist[1:5:2])


# In[ ]:


# Q how will you reverse the list

print(origlist[::-1])


# In[ ]:





# In[ ]:


extuple=(1,3,"hello",'h',[3,4,5,"yo"])
print(extuple[0])


# In[ ]:


print(extuple[2][3])


# In[ ]:


#get " y " of yo in extuple


# In[ ]:





# # functions

# In[ ]:


#function definition

def function():
    print("hello world")
    
    
#function call /main function    
function()


# In[ ]:


def sumfun(a ,b):
    s=a+b
    print(" sum is ",s)

    #main 
x=int(input('\n enter First Value  '))
y=int(input(" Enter second Value  "))
sumfun(x,y)
    


# In[ ]:


def sumfun(a ,b):
    s=a+b
    return s

x=int(input('\n enter First Value  '))
y=int(input(" Enter second Value  "))
sums=sumfun(x,y)    #sums=s
print("\n sum is ",sums)


# In[ ]:


#recursive functions

def recsum(sum):
    a=int(input("\n Enter number less than 10 "))
    if(a<10):
        sum=a+sum
        print("sum is ",sum)
        recsum(sum)
    else:
        return 0
 
recsum(0)
    

