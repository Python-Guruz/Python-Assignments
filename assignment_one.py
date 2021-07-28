#ASSIGNMENT ONE


#NUMBERS
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25.

print((10*12)+(50/200)-20)

#What is the type of the result of the expression 3 + 1.5 + 4?

result=(3+1.5+4);
print(result);
print(type(result));



#What would you use to find a number’s square root, as well as its square?
#print(math.sqrt(100));
#or 
print(100**0.5)
print(3**2)





#STRINGS
#Given the string 'hello' give an index command that returns 'e'
greeting="hello"

print(greeting[1])

#Reverse the string 'hello' using slicing:
x=greeting[::-1]
print(x)

#Given the string hello, give two methods of producing the letter 'o' using indexing.

print(greeting[4])
print(greeting[4::])


#LISTS
#Build this list [0,0,0] two separate ways.
#print(list[3])

#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)

#Sort the list below:
list4 = [5,3,4,6,1]
print(list.sort(list4) )

#DICTIONARIES
#Using keys and indexing, grab the 'hello' from the following dictionaries: 
d = {'simple_key':'hello'} 
 
print(d['simple_key'])


d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

 
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])


 
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

 
#Can you sort a dictionary? Why or why not?
#no you cant sort a dictionary because it is not ordered.


#TUPLES
#What is the major difference between tuples and lists?

#tuples are immutable while lists are mutable.


#How do you create a tuple?

tup=('chicken','crisps')
print(tup)


#SETS
#What is unique about a set?

###a set cannot have duplicates.

#Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))





#BOOLEANS
#What will be the resulting Boolean of the following pieces of code
2 > 3
#false

3 <= 2
#false

3 == 2.0
##false

3.0 == 3
##print(3.0 == 3)
##true
4**0.5 != 2
##false

#What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
 
# True or False?
l_one[2][0] >= l_two[2]['k1']
 ##false
 
 
 
 
 
 
 
 
 

 


 

