
# coding: utf-8

# # INTRODUCTION - 7 exercises

# In[ ]:


# 1. Say 'Hello' to the world with Python

# Use function print to output the bot_message

print('Hello, World!')


# In[ ]:


# 2. Python if-else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
#explicit conditions using if-elese statements
#use the reminder to check if it is an even or odd number

if n%2 != 0 : #if n is odd
    print("Weird")
elif n%2==0 and 2<=n<=5 : # elif n is even and included in 2-5
    print("Not Weird")
elif n%2==0 and 6<=n<=20 : #elif n is even and included in 6-20
    print("Weird")
elif n%2==0 and n>20 : #elif n is even and bigger than 20
    print("Not Weird")


# In[ ]:


# 3. Arithmetic Operators

if __name__ == '__main__':
    a = int(input()) #take two integers inputs, a and b
    b = int(input())
    if a in range(1,(10**10)): #check if they respects the contrains given by the exercise
        if b in range(1,(10**10)):
            print(a+b) #print sum of a and b
            print(a-b) #print difference between a and b
            print(a*b) #print product between a and b


# In[ ]:


# 4. Python division

if __name__ == '__main__':
    a = int(input()) #take teo integers inputs, a and b
    b = int(input())
    print(a//b) #print integer division between a and b
    print(a/b) #print division between a and 4


# In[ ]:


# 5. Loops

if __name__ == '__main__':
    n = int(input()) #take an integer input, n
    if n>=1 and n<=20: #check if it respects the contrains
        for i in range(n): #iterate over a for loop n time
            print(i**2) #each iteration print i squared
    else:
        print("n is out of contrains") #give back an error message if n is out of range


# In[ ]:


# 6. Write a function

def is_leap(year):
    leap = False
    if year >= 1900 and year <= 10**5:
        if year%4 == 0: #use reminder to chek if year its evenly divisible by 4
            return True #if so return true
        else:
            if year%100 == 0: # else check if evenly divisible by 100
                return False #if so return false
            else:
                if year%400 == 0: #else chek if evenly divisible by 400
                    return True #if so return true
    
    #
    
    return leap #output the result

year = int(input()) #call the function


# In[ ]:


# 7. Print a function

if __name__ == '__main__':
    n = int(input()) #take an integer input n
    
    for i in range(1,n+1): #execute the for loop n times, starting from 1 to exclude 0
        
        print(i,end='') #print i all in one line withpout spaces in between


# # DATA TYPES - 6 exercises

# In[ ]:


# 1. List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list=[] #create an empty list
    
    #using list comprehension with foor loops to happend values to that list that respect the if (i+j+k != n)
    [list.append([i,j,k]) for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k) !=n)]
   
    print(list)


# In[ ]:


# 2. Find the Runner-up score

if __name__ == '__main__':
    n = int(input()) #take an integer input n
    arr = map(int, input().split()) #use the function map to apply the int function to each element of the space-separated string input. use split() to make each element an indipendent string 


# In[ ]:


# 3. Nested Lists

if __name__ == '__main__':
    n=int(input()) #take an integer input n, number of students
    l=[] #create an empty list
    for i in range(n): #iterate n times to take each student data(name and score) and append each entry to the list
        l.append([input(),float(input())])

    second_highest= sorted(list(set([marks for name, marks in l])))[1] #take second-highest score from the sorted list of scores
    print('\n'.join([a for a, b in sorted(l) if b== second_highest])) #print the name(s) of that stutent(s), if more thank one sort them alpabetically


# In[ ]:


#4. Find the percentage

if __name__ == '__main__':
    n = int(input()) #take an integer input, number of students
    marks={} #create an empty dictionary
    for _ in range(n): #iterate n times
        line = input().split() # take the input string containing scores, split them by space and make them integers
        marks[line[0]]= list(map(float,line[1:])) # store the list of marks into the dictionary
        name,scores = line[0],line[1:] #identify the 'name' and the 'score' data
    print('%.2f' %(sum(marks[input()])/3)) #print the average marks of the student name in input


# In[ ]:


# 5. Lists

if __name__ == '__main__':
    n = int(input()) #take integer input n, number of commands
    l =[] #create an empty list
    for _ in range(n): #iterate n times
        s=map(int,input().split()) #each iteration take the command input
        c= s[0] #these are names of commands
        a = s[1:] # values to use in each command
        if c != "print": #take all the commands apart from print
            c += "("+",".join(a) +")" #built the line of the command
            eval("l."+c) #execute the command
        else:
            print(l) #print the result
    


# In[ ]:


#6. Tuples

if __name__ == '__main__':
    n = int(input()) #take integer input as number of elements of the tuples
    
    integer_list = map(int,input().split()) #split them, make the integers using map 
    
    t=tuple(integer_list) #tranform the list into a tuple
    print(hash(t))


# # STRINGS - 14 exercises

# In[ ]:


#1. Swap Cases

import string
def swap_case(s):
    if len(s)>0 and len(s)<=1000: #check if length is in constrains
        return s.swapcase() #output swapcases



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:


# 2. String Split and join

import string
def split_and_join(line):
    
    s = line.split(" ") #split string when encounte blanck space
    a = "-".join(s) #join the strings generated using -
    return a

    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:


# 3. Waht's your name?

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(first_name,last_name))
#I used .format to insert inputs (name and surmname) into he sentence
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


# 4. Mutations

def mutate_string(string, position, character):
    l= list(string) #make the string a list
    l[position]= character #replace the character in the desired position
    new_string = ''.join(l) #store the new string
    return new_string #return the new list

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:


# 5. Find a string

def count_substring(string, sub_string):
    if len(string)>= 1 and len(string)<=200: #check if contrains are respected
        count=0 #start counting from zero
        for i in range(len(string),0,-1): #loop backwards for (len(string))times
            if string[i-len(sub_string):i] == sub_string: #check if the substring appear in the string
                count +=1 #increment count to take note of the number of observations
            
        return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:


# 6. String Validator

if __name__ == '__main__':
    s= input()
    if any(char.isalnum() for char in s): #check is there is any alphanumeric
        print(True)
    else:
        print(False)
    if any(char.isalpha() for char in s): #check if there is any alphabetic
        print(True)
    else:
        print(False)

    if any(char.isdigit() for char in s): #check if there is any digit
        print(True)
    else:
        print(False)

    if any(char.islower() for char in s): #check if there is any lowercase
        print(True)
    else:
        print(False)
    if any(char.isupper() for char in s): #check if there is any upercase
        print(True)
    else:
        print(False)
    


# In[ ]:


# 7. Text alignment

thickness = int(input()) #This must be an odd number
if thickness %2 != 0:
    c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[ ]:


# 8. Text Wrap

import textwrap

def wrap(string, max_width):
    
    return textwrap.fill(string,max_width) #wrap the string into a pararaph of w width

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[ ]:


# 9. Designer Door Mat
#use strings concatenation and .center method

n,m= input().split()
n=int(n)
m=int(m)
print(".|.".center(m,'-'))
for i in range(1,(n//2)):
    print(("."+ i *"|..|.."+"|"+ ".").center(m,'-'))
print("WELCOME".center(m,'-'))
for i in range((n//2 -1),0,-1):
    print(("."+ i * "|..|.."+"|" + ".").center(m,'-'))
print(".|.".center(m,'-'))


# In[ ]:


# 10. String Formatting
#use functions oct for octal, hex for hexadecimal and bin for binary
def print_formatted(number):
    l= len(bin(number)[2:])
    for i in range (1,number+1):
        print(str(i).rjust(l,' '), str(oct(i)[2:]).rjust(l,' '), str(hex(i)[2:].upper()).rjust(l,' '), str(bin(i)[2:]).rjust(l,' '),sep=' ')
    # your code goes her

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[ ]:


# 11. Alphadet Rangoli

def print_rangoli(size):
    import string
    char= string.ascii_lowercase

    
    l=[]
    for i in range(n): #iterate n times, where n is the desired size of the rangoli
        s= '-'.join(char[i:n]) #use methods .join and centre to obrain the correct output
        l.append((s[::-1]+s[1:]).center(4*n-3,'-'))
    print('\n'.join(l[:0:-1]+l))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# In[ ]:


# 12. Capitalize

import math
import os
import random
import re
import sys
import string

#use method .capitalize to tranform the input with first capital letter
def solve(s):
    n= s.split(' ')
    return ' '.join([i.capitalize() for i in n])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# In[ ]:


# 13. The Minion game


def minion_game(string):
    v= 'AEIOU'  #write the strings with vowels and use it to distinguish which player has the point
    kev=0
    stu=0
    for i in range (len(s)):
        if s[i] in v: #if the string start with vowels give point to kevin
            kev += (len(s)-i)
        else:
            stu += (len(s)-i) #else give a point to stuart
    
    if kev>stu:
        print("Kevin",kev)
    elif kev<stu:
        print("Stuart", stu)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[ ]:


# 14. Merge the tools!

# split the string into n/k subsegment
def merge_the_tools(string, k):
    for part in zip(*[iter(string)]*k): #iterate over the string
        d = dict() #transform into a dictionary
        
        print(''.join([d.setdefault(c,c) for c in part if c not in d]))
        #print the substrings without the  repeated characters
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# # SETS - 13 exercises

# In[ ]:


# 1. Introduction to sets

def average(array):
    return sum(set(array))/len(set(array)) #compute the average
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[ ]:


# 2. No Idea!


n, m = map(int, input().split()) # take inputs n and m
array = list(map(int, input().split())) #take the input cointaining the elements of the array and transform it into a list
a = set(map(int, input().split())) #take inputs a and b
b = set(map(int, input().split()))

x = 0 #start counting at 0
for elem in array: #increment count for each 'a' elemnt and decrement it for each 'b' element
    x += elem in a
    x -= elem in b
print(x)


# In[ ]:


# 3. Symmetric Difference

# take the input integers and return the symmetric difference
a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')


# In[ ]:


# 4. Set. add()
# count the total countries contained in the list ( without double counting)
s = set()
for _ in range(int(input())):
    s.add(input())
print(len(s))



# In[ ]:


# 5. Set.discard().remove() & pop()

n = int(input())
s = set(map(int, input().split()))
# modify the input set and return sum of the elemnts ramaining

for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))



# In[ ]:


# 6. set.union() operations
# pritn the number of the students to have at least one subscription.

print(len((set(input().split()) if input() != '-1' else '')|(set(input().split()) if input() != '-1' else '')))


# In[ ]:


# 7. Set intersection() operations

_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.intersection(b)))


# In[ ]:


# 8. Set difference() operations

n1 = int(input())
set_1 = set(map(int,input().split()))
n2 = int(input())
set_2 = set(map(int,input().split()))
print(len(set_1-set_2))



# In[ ]:


# 9. set.symmetric difference operations

n,s1=int(input()),set(map(int,input().split()))
b,s2=int(input()),set(map(int,input().split()))
print(len((s1.difference(s2)).union(s2.difference(s1))))


# In[ ]:


# 10. set mutations

#compute the sum of elements in set A

if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))




# In[ ]:


# 11. the capitain's room

d=input()  
a=input().split() 
s1=set()  #room number
s2=set() #room number occur more than onc
for i in a:
    if  i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
print(list(s3)[0])


# In[ ]:


# 12. check subset
#check if it is a subset using method .issubset
for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))


# In[ ]:


# 13. Check strict superset
#print true if a is a super set of each input, using method .issuperset
a = set(map(str, input().split(' ')))
is_strict_superset = []
for i in range(int(input())):
     is_strict_superset.append(a.issuperset(set(map(str, input().split(' ')))))
print(all(is_strict_superset))


# # COLLECTIONS - 8 exercises

# In[ ]:


# 1. Collections.Counter()

import collections

n_shoes= int(input()) #number of the shoes
#available sizes
available_sizes= collections.Counter(map(int,input().split()))

n_custumer= int(input()) #number of costumers

gain=0

desired=[]

for i in range(n_custumer): #iterate as many times as the number of customer
    x,y= map(int,input().split()) #for each of them store the value of the desired size and the price
    if available_sizes[x]: #check if the size is available and sum the prices of the pair of shoes sold
        gain += y
        available_sizes[x] -= 1
print(gain)


# In[ ]:


# 2. DefaultDict

# use defaultdict fuction to count how many times each character appears in the string and output thei position idices
import collections
from collections import defaultdict
d= defaultdict(list)

n,m= map(int, input().strip().split())
[d[input().strip()].append(str(a)) for a in range(1, n+1)]


for a in range(m):
    f = input().strip()
    if not d[f]:
        print(-1)
        continue
    print(" ".join(d[f]))


# In[ ]:


# 3. Collections.namedtuple()

#use namedtuple function to built the table containig the data
from collections import namedtuple

(n,cat) = (int(input()), input().split())
Grade = namedtuple('Grade', cat)

#print the average of column MARKS, rounded to 2 decimal places
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print(round(sum(marks)/len(marks,2))


# In[ ]:


# 4. Collection.OrderedDict()

#use function OrderedDict to output item_name and net price in order of its first occurrence
from collections import OrderedDict

a = OrderedDict()
for _ in range(int(input())):
    i = input().rpartition(" ")
    
    a[i[0]] = int(i[-1]) + a[i[0]] if i[0] in a else int(i[-1])
    

for l in a:
    print(l,a[l])


# In[ ]:


# 5. Word Order

from collections import OrderedDict

a = OrderedDict()

for _ in range(int(input())): #iterate to count the times of number of occurrencies for each word
    x= input()
    a.setdefault(x,0)
    a[x] += 1

print(len(a))
print(*a.values())


# In[ ]:


# 6. Collection.deque()

from collections import deque
que= deque()
#apply the methods in input to an empty deque
for _ in range(int(input())):
    method, _, args = input().strip().partition(" ")
    getattr(que,method)(*args.split())

print(*list(que))


# In[ ]:


# 7. Company Logo

import math
import os
import random
import re
import sys
from operator import itemgetter


if __name__ == '__main__':
    
    chars= list(input())
    d = [[c, chars.count(c)] for c in set(chars)] #iterate to buld the list d
    d.sort(key=itemgetter(0)) 
    d.sort(key=itemgetter(1), reverse= True)
#print most common characters
    for i in d[:3]:
        print("{0} {1}".format(i[0], i[1]))


# In[ ]:


#8. Piling up!

for i in range(int(input())):
    n = int(input())
    a_list= list(map(int,input().split()))
    
    b= 0
    

    while b < n-1 and a_list[b] >= a_list[b+1]:
        b += 1
    while b < n-1 and a_list[b] <= a_list[b+1]:
        b += 1
    
    print("Yes" if b == n-1 else "No")


# # DATE AND TIME - 2 exercises

# In[ ]:


# 1. Calendar Module

import calendar
#outputthe correct week day of the date in input

n= input().split()
month = int(n[0])
day = int(n[1])
year= int(n[2])
weekday=(calendar.weekday(year,month,day))

days= ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

print(days[weekday])


# In[ ]:


# 2. Time Delta

import math
import os
import random
import re
import sys
from datetime import datetime as dt

# print the absolute difference in seconds
def time_delta(t1, t2):
    time1 = int(dt.strptime(t1, '%a %d %b %Y %H:%M:%S %z').timestamp())
    time2 = int(dt.strptime(t2, '%a %d %b %Y %H:%M:%S %z').timestamp())
    diff= time1 - time2
    return str(abs(diff))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# # EXCEPTIONS - 1 exercise

# In[ ]:


# 1. Execptions

n= int(input())
#handle errors and print correct error message for each case
for i in range(n):
    a,b= input().split()
    try:
        div= int(a)//int(b)
        print(div)
    except:
        if b.isnumeric() == False:
            print("Error Code: invalid literal for int() with base 10: '{}'".format(b))
        elif a.isnumeric() == False:
            print("Error Code: invalid literal for int() with base 10: '{}'".format(a))
        else:
            print("Error Code: integer division or modulo by zero")




# # BUILD-INS - 3 exercises

# In[ ]:


# 1. Zipped!

n,x = map(int,input().split())
# print the average mark for each student rounded to 1 decimal place
A=[]
for _ in range(x):
    A.append(map(float,input().split()))

for i in zip(*A):
    print(rount(sum(i)/len(i),1)


# In[ ]:


# 2. Athlete Sort

import math
import os
import random
import re
import sys
import operator

#sort the data into the table based in kth input
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    a_sorted=(sorted(arr, key=operator.itemgetter(k)))
    for line in a_sorted:
        print(*line, sep=' ')


# In[ ]:


# 3. GinsortS

#output the sorted string
s = input()
print(*sorted(s, key=lambda c:(c.isdigit() - c.islower(),c in '02468',c)),sep='')


# # PYTHON FUNCTIONALS - 1 exercise

# In[ ]:


# 1. MAp and Lambda

cube = lambda x: x**3 #lambda function

fib= [0,1]
def fibonacci(n): #function to compute the fubonacci numbers
    for i in range(2,n):
        fib.append(fib[i-2] + fib[i-1])
    return fib[0:n]

    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n)))) #output the cube of fibonacci numbers


# # REGEX AND PARSONG - 17 exercises

# In[ ]:


# 1. Detect floating point numbers
# verify if n is a float
import re
[print(bool(re.match(r'[-+]?[0-9]*\.[0-9]{1,}$',input()))) for i in range(int(input()))]


# In[ ]:


# 2. Re.split()

regex_pattern = r"[.,]+"
#use re.split to split the simbols , and .
import re
print("\n".join(re.split(regex_pattern, input()))) 


# In[ ]:


# 3. Group(), Groups() & Grouped()
 #check to find first occurrence of an alphanumeric char in s with consecutive repetition
import re
m = re.search(r"([a-z0-9])\1+", input())
print(m.group(1) if m else -1)


# In[ ]:


# 4. Re.findall() & Re.finditer()

import re
s = '[qwrtypsdfghjklzxcvbnm]'
#see if there is any substring in s that contains two or more vowels between two consonants
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))


# In[ ]:


# 5. Re.start & Re.end()
 # build a tuple containing start and end indices of strin k in s
import re
s, k = input(), input()
matches = list(re.finditer(r'(?={})'.format(k), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')


# In[ ]:


# 6. Regex substitution

import re
N = int(input())
#use a for loop to iterate over the N lines of the text
#modify && into and, || into or
for i in range(N):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))


# In[ ]:


#7. Validating Roman numerals
#explicit how each numerical term is expressed in roman numbers
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

#use these terms to decide if the roman number is valid
regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)

import re
print(str(bool(re.match(regex_pattern, input()))))


# In[ ]:


# 8. validating phone numbers
#print only the phone numbers that respect the constrains
import re
[print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]


# In[ ]:


# 9. Validating and parsing email address

import re

email = re.compile(r"^[a-zA-Z0-9]+[a-zA-Z0-9-_.]*\@[a-zA-Z]*\.[a-zA-Z]{1,3}$")
#iterate as many times as the number of emails
# check if the conditions in email match

for _ in range(int(input())):
    in_str = input()
    if email.match(in_str.split()[1].strip("<>")):
            print(in_str)


# In[ ]:


# 10. Hex color code
#print hex code for the color in the list 
import re
for i in range(int(input())):
    a = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*a, sep='\n')


# In[ ]:


# 11. HTML parser- part 1

#print start tags, end tags and empty tags for the HTML code
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))


# In[ ]:


# 12. HTML parser - parte 2
#given an HTML code, print only the signle and multi line of commments and the data
from html.parser import HTMLParser
class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line>1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

parser = CustomHTMLParser()

n = int(input())

html_string = ''
for i in range(n):
    html_string += input().rstrip()+'\n'
    
parser.feed(html_string)
parser.close()


# In[ ]:


# 13. Detect HTML tags, attributes and atrribute values

from html.parser import HTMLParser
# print html tags, attributes and values in the code given the simbols
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

parser = MyHTMLParser()

for i in range(int(input())):
    parser.feed(input())


# In[ ]:


# 15. Validating UID

import re
#check if all IDs respect the constrins given in the esecise
def valid(s):
    if len(s) != 10:
        return 'Invalid'
    else:
        if  not re.search(r'.*[A-Z].*[A-Z].*', s):
            return 'Invalid' 
        if not re.search(r'.*\d.*\d.*\d.*', s):
            return 'Invalid' 
        if not re.search(r'[a-zA-Z\d]{10}', s):
            return 'Invalid'
        if re.search(r'(.).*\1', s):
            return 'Invalid'
        return 'Valid'

for _ in range(int(input())):
    s = input()
    print(valid(s))
    


# In[ ]:


# 16. validating Credit cards

import re
# iterate over the credit cards numbers to check if they respect the conditions
for _ in range(int(input())):
    s = input()

    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")


# In[ ]:


# 17. MAtrix Script

import math
import os
import random
import re
import sys

# take only the alphanumeric char into each column and connect theme
n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))


# # XML - 2 exercises

# In[ ]:


# 1. XML 1 - find the score

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    #return the score o f each xml document, by adding each element 
    return len(node.attrib) + sum(get_attr_number(child) for child in node)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# In[ ]:


# 2. XML2 - find the maximum depth

import xml.etree.ElementTree as etree
#output the maximum value of nesting
maxdepth = -1

def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child,level +1)
    
    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# # CLOSURES AND DECORATIONS - 2 exercises

# In[ ]:


# 1. standardize mobile numbers

#check if the given numbers respect the contrains
def wrapper(f):
    def fun(l):
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# In[ ]:


# 2. Decorators2 - name dictionary

import operator

# return all people data sorted by their age starting from yungest
def person_lister(f):
    def inner(people):
        return map(f, sorted(people,key=lambda x: int(x[2])))
        
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# # NUMPY - 15 exercises
# 

# In[ ]:


# 1. Arrays
#print the reverse numpy array using float type
def arrays(arr):
    return numpy.array(arr[::-1],float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[ ]:


# 2. shape and reshape

import numpy
import numpy as np
#convert the list into a 3 by 3 array
print(np.array(input().split(),int).reshape(3,3))


# In[ ]:


# 3. transpose and flatten

import numpy
# print transpose and flatten results using .transpose and .flatten
n , m = input().split();
a = [];
for i in range(int(n)):
    my_array = input().split();
    a.append(my_array);
lis1 = numpy.array(a,int);
print(numpy.transpose(lis1))
print(lis1.flatten())



# In[ ]:


# 4. Concatenate
#concatenate the arrays alon gx axis

import numpy

N, M, _ = [int(x) for x in input().strip().split()]
a, b = map(lambda x: numpy.array([input().strip().split() for i in range(int(x))], int), [N, M])
print(numpy.concatenate((a, b), axis = 0))


# In[ ]:


# 5. zeroes and ones
#print an array of zeros and ones
import numpy

shape= tuple(map(int,input().split()))
print(numpy.zeros(shape,int), numpy.ones(shape,int), sep='\n')



# In[ ]:


# 6. eye and identity

import numpy
#pritn eye array of given dimensions
numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))



# In[ ]:


# 7. array mathematics

import numpy

N, M = list(map(int, input().split()))

a1 = numpy.array([input().split() for _ in range(N)], int)
a2 = numpy.array([input().split() for _ in range(N)], int)
#print the mats between given arrays
print(*[eval('a1'+i+'a2') for i in ['+','-','*','//','%','**']], sep='\n')


# In[ ]:


# 8. floor ceil and rint

import numpy

numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# In[ ]:


# 9. sum and prod

import numpy

import numpy

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(numpy.prod(numpy.sum(arr,axis=0)))


# In[ ]:


# 10. min and max

import numpy

arr=[]
n,m=map(int,input().split())
for row in range(n):
    my_arr=list(map(int,input().split()))
    arr.append(my_arr)
my_array=numpy.array(arr)
result=numpy.min(my_array, axis = 1)
print(max(result))



# In[ ]:


# 11. mean var and standard deviation

import numpy

N, M = map(int, input().split())
_ = numpy.array([input().split() for i in range(N)], int)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(_, axis=1))
print(numpy.var(_, axis=0))
print(numpy.std(_, axis=None))


# In[ ]:


# 12. dot and cross

import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))


# In[ ]:


# 13. Inner and outer

import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)
print(numpy.inner(a, b),numpy.outer(a, b), sep='\n')



# In[ ]:


# 14. linear algebra

import numpy

numpy.set_printoptions(legacy='1.13')
n = int(input())
print(numpy.linalg.det(numpy.array([list(map(float, input().split())) for _ in range(n)], float)))



# # BIRTHDAY CAKE CANDLES

# In[ ]:


import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


# # KANGOROO

# In[ ]:


import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# # STRANGE ADVERTISING

# In[ ]:


import math
import os
import random
import re
import sys


def viralAdvertising(n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# # RECURSIVE DIGIT SUM

# In[ ]:


import math
import os
import random
import re
import sys


def superDigit(n, k):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# # INSERTION SORT PART 1

# In[ ]:


import math
import os
import random
import re
import sys

def insertionSort1(n, arr):

    ##
    
    target = arr[-1]
    idx = n-2

    while (target < arr[idx]) and (idx >= 0):
        arr[idx+1] = arr[idx]
        print(*arr)
        idx -= 1

    arr[idx+1] = target
    print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# # INSERTION SORT PART 2
# 

# In[ ]:


import math
import os
import random
import re
import sys


def insertionSort2(n, arr):

    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

