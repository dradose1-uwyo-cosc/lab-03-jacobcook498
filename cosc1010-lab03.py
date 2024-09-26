# Jacob Cook
# UWYO COSC 1010
# 09/29/24
# Lab 03 
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
mountain_states=('Wyoming', 'Colorado', 'Montana')



#print the entire list
print(mountain_states)

#now print the first element in the list
print(mountain_states[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(mountain_states[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f'{mountain_states[1]} is south of {mountain_states[0]}')



print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
mountain_states = ['Wyoming','Colorado','Montana']
mountain_states.append('Washinton')
mountain_states.append('Oregon')
mountain_states.append('California')
print(mountain_states)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
mountain_states.insert(-1,'Maine')
print(mountain_states)

#Insert the state Texas to be the third element in the list, again printing your list
mountain_states.insert(2, 'Texas')
print(mountain_states)

#Using the `del` statement remove the fourth item from the list, print your list 
del mountain_states[3]
print(mountain_states)

#Remove Texas using its value, print the list
del mountain_states[2]
print(mountain_states)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(sorted(mountain_states))
print(mountain_states)

#Permanently sort your list in reverse order, printing it out

mountain_states.sort(reverse=True)
print(mountain_states)


#Using the reverse method reverse the list and print it

mountain_states.reverse()
print(mountain_states)