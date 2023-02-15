#1. What is List? How will you reverse a list?

l1=[1,1.1,'Mihir',101,True,55,False]
l1.reverse()
print(l1)

#2. How will you remove last object from a list?

#(hint) using pop

l2=[1,1.1,'Mihir',101,True,55,False]
l2.pop()
print(l2)


#3. Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?


list1=[2, 33, 222, 14,25]
print(list1[-1])



#4.Differentiate between append () and extend () methods?
#ans= append will adding single elements at last and extend will adding multiple elements

l4=[1,1.1,'Mihir',101,True,55,False]
l4.append(77)
print(l4)

l4.extend(['Champaneri',22])

print(l4)



#5.Write a Python function to get the largest number, smallest num and sum 
#of all from a list.

l5=[1,2,8,11]
b=0


a=max(l5)
b=min(l5)
c=sum(l5)
print('largest num :',a,'smallest num :',b,'Sum Of All List :',c)



#6.How will you compare two lists?

l6=list(input('Enter List 1 : '))#[1,1.1,2,2.2,3,4,5]
l6_1=list(input('Enter List 2 : '))#[1,1.1,2,2.2,3,4,5]

if l6==l6_1:
    print('Both Lists Are Same :')
else:
    print('Both Lists Are Not Same :')



#7.Write a Python program to count the number of strings where the string 
#length is 2 or more and the first and last character are same from a given 
#list of strings

a=['564123','Mihir','abca']
b=0
for i in a:
    print(i)
    if len(i)>=2 and i[0]==i[-1]:
        b+=1
print(b)



#8.Write a Python program to remove duplicates from a list.

l8=[2,3,5,2,3,8,7,4,9,10,'Mihir']
print(list(set(l8)))

#or

l8_1=[2,3,5,2,3,8,7,4,9,10,'Mihir']
c=[]
for i in l8_1:
    if i not in c:
        c.append(i)
print(c)




#9.Write a Python program to check a list is empty or not


i9=[]

if i9==[]:
    print('empty')
else:
    print('Not An Empty')




#10.Write a Python function that takes two lists and returns true if they have 
#at least one common member.

l10=[1,2,3]
l10_1=[3,4,5]
for i in l10:
    if i in l10_1:
        print('true')
        break
else:
    print('false')




#11.Write a Python program to generate and print a list of first and last 5 
#elements where the values are square of numbers between 1 and 30.


l11 =[]
for i in range(1,30):
    l11.append(i*i)
print(l11[:5])
print(l11[-5:])




#12.Write a Python function that takes a list and returns a new list with unique 
#elements of the first list

l12=[2,3,5,2,3,8,7,4,9,10,'Mihir']
c=[]
for i in l12:
    if i not in c:
        c.append(i)
print(c)



#13.Write a Python program to convert a list of characters into a string.

l13=['Mihir','Champaneri','j']
print(''.join(l13))
#print(str)



#14.Write a Python program to select an item randomly from a list.


import secrets

l14=['Mihir',1,'Champaneri','Nitin',55,44,88,99,100]
print(secrets.choice(l14))


#or

import random

l14=['Mihir',1,'Champaneri','Nitin',55,44,88,99,100]
print(random.choice(l14))

#or

c=[]
for i in range(1,100):
    c.append(i)
#print(c)
import secrets
print(secrets.choice(c))



#15.Write a Python program to find the second smallest number in a list

l15=[2,5,8,9,45,2,5,4,9,2,12,5,51,515,0.21,0.02]
l15.sort()
print(l15)
print(l15[1])



#16.Write a Python program to get unique values from a list

l16=[2,2,5,8,7,9,3,4,56,56]
print(list(set(l16)))

#or

c=[]
for i in l16:
    if i not in c:
        c.append(i)
print(c)


l17=[1,5,3,56,4,6,1,5,3,2,1,5,4]
for i in l17:
    if type (i)==list:
        print('sublist present in list')
        break
else:
    print('not in sublist')



#18.Write a Python program to split a list into different variables.

l18= [(1,2,1.1,True,5,6,),('Champaneri',5.5,7,3,1.1,False,),(5.5,786,'Mihir',22)]
print(l18)
var1,var2,var3=l18
print('Var1 -:',var1)
print('Var2 -:',var2)    
print('Var3 -:',var3)


#19.What is tuple? Difference between list and tuple.

#20.Write a Python program to create a tuple with different data types.

s=(1,1.1,'Mihir',2222,True)
print(s)


#21.Write a Python program to create a tuple with numbers.

s1=1,1.1,55,2222,47
print('Print Tuple With Numbers-:',s1)
print(type(s1))


#22.Write a Python program to convert a tuple to a string.
    
s2=(1,1.1,55,2222,47,True,'sk')

s3=str(s2)
print(s3)
print(type(s3))



#23.Write a Python program to check whether an element exists within a 
#tuple.
     
t=('Mihir',10,5,8,'k',88)
print('Mihir' in t)
print(99 in t)


#24.Write a Python program to find the length of a tuple.


t1=tuple('learning Python in Tops')
print(t1)
print(len(t1))


#25.Write a Python program to convert a list to a tuple.

l25=[11,'Mihir',5,22]
print(l25)
t2=tuple(l25)
print(t2)



#26.Write a Python program to reverse a tuple.

t3=(11,55,22,'Mj',77)
print(t3)
t4=reversed(t3)
print(tuple(t4))


#27.Write a Python program to replace last value of tuples in a list.

l27=[(11,55,'Mj'),('Mj',5,8,66),(88,55,33)]
print(l27)
print([t[:-1] + (1992,) for t in l27])


#28.Write a Python program to find the repeated items of a tuple.

t4=8,9,22,5,'Mj',5,8,22,'Mj',5
print(t4)
print(t4.count('Mj'))


#count=t4.count('Mj')
#print(count)



#29.Write a Python program to remove an empty tuple(s) from a list of tuples

l29=[(),(''),('M'),(22),('a','c'),()]
print(l29)
l29=[t for t in l29 if t]
print(l29)

#30.Write a Python program to unzip a list of tuples into individual lists.

l30=[(1,3,5),(2,4,6),(7,9,11)]
print(l30)
print(list(zip(*l30)))


#31.Write a Python program to convert a list of tuples into a dictionary.

l31=[('Mj',1),('jM',2),('ab',3)]
print(dict(l31))

#print(l31)
#d=dict(l31)
#print(d)

#32.How will you create a dictionary using tuples in python?
#Ans:-To convert a tuple to dictionary in Python use the dict() method.


#33.Write a Python script to sort (ascending and descending) a dictionary by value.

d={'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}

s=dict(sorted(d.items(),key=lambda x:x[1]))
print(s)


s=dict(sorted(d.items(),key=lambda x:x[0],reverse=True))
print(s)


#34.Write a Python script to concatenate following dictionaries to create a new one.

d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4={}

for d in (d1,d2,d3): d4.update(d)
print(d4)


#35.Write a Python script to check if a given key already exists in a dictionary.

d3={1: 'Ahmedabad',2: 'Baroda',3: 'Rajkot',4: 'Surat'}
print('The Given Dictionary :',d3)
def is_key_present(a):
    if a in d3:
        print('Key Is Present In Dictionary')
    else:
        print('Key Is Not Present In Dictionary')
is_key_present(1)
is_key_present(5)

#or

a = {'Mon':3,'Tue':5,'Wed':6,'Thu':9}
print("The given dictionary : ",a)
key = "Fri"
if key in a:
   print(key,"is Present.")
else:
   print(key, " is not Present.")


#36.How Do You Traverse Through A Dictionary Object In Python?

#You can iterate through a Python dictionary using the keys(), items(), and values()
#methods. keys() returns an iterable list of dictionary keys. items() returns the key-value pairs
#in a dictionary.
        

#37.How Do You Check The Presence Of A Key In A Dictionary?

d4 = {"a": 1, "b":2, "c":3}
if "a" in d4:
    print("Exists")
else:
    print("Does not exist")

#Using has_key() method returns true if a given key is available in the dictionary,
#otherwise, it returns a false. With the Inbuilt method has_key(), use the if statement to
#check if the key is present in the dictionary or not.

#Note: has_keys() method has been removed from the Python3 version. Therefore, it can be used in Python2 only



#38. Write a Python script to print a dictionary where the keys are numbers 
#between 1 and 15.

d5=dict()
for x in range(1,16):

    d5[x]=x**2
print(d5)


#39.How can you pick a random item from a list or tuple?

import random

myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]

print (random.choice(myList))

#40. How can you pick a random items of a range?

import random

num = random.randrange(100,200,2)
print(num)

#41. Python program to return sum of all divisors of a number.

def totaldiv(no):
    div=[1]
    for k in range(2,no):
        if(no % k)==0:
            div.append(k)
    return sum(div)
print('sum of all divisors 14 is : ',totaldiv(14))
print('sum of all divisors 18 is : ',totaldiv(18))
print('sum of all divisors 24 is : ',totaldiv(24))
print('sum of all divisors 34 is : ',totaldiv(34))

#42. Write a python program to find the maximum and minimum numbers from the specified decimal numbers.

num=int(input("Enter N number : "))

arr=[]
for n in range(num):
    number=int(input("Enter number : "))
    arr.append(number)
print(arr)

print("Maximum value in the list is : ",max(arr))
print("Minimum value in the list is : ",min(arr))


    













































  



