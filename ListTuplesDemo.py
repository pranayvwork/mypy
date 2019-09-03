#Lists - are mutable
#list of courses
courses = ['history', 'math', 'physics', 'comp sci']
print(courses)
print(len(courses))
#print first item in list
print(courses[0])
print(courses[3])
#print(courses[4]) # error - > list index out of range
#print last item
print(courses[-1])
#slicing of list
#first index is inclusive but second index is NOT.
# so this will print item at index 0, 1. but NOT item at index 2.
print(courses[0:2])
#first index can also be omitted if we want to slice from start of the list.
print(courses[:2]) # prints item at 0,1.
#if we omit the second index then iteration goes to end of the list.
print(courses[2:])

#List methods
courses.append('Art')
print(courses)

#insert item at a position
courses.insert(0,'Paint')
print(courses)

#inserting a list inside a list
courses_2  = ['Education', 'Humanities']
#courses.insert(0, courses_2)
print(courses)

#extend method
#if we want to add only the values of a list into our list.
courses_3 = ['Ornitho', 'Yoga']
courses.extend(courses_3) #ornitho and yoga added to the end of courses.
print(courses)

#remove items from list
courses.remove('math')
print(courses)

#pop removes the last value in the list. It also returns the popped value.
poppedItem = courses.pop() #removes the last value in the list
print(poppedItem)

#reverse list 
courses.reverse()
print(courses)
#sorting list
#sort alphabetically
courses.sort() #if the list contains another inner list then we can't use this method.
print(courses)
nums = [1,3,4,2,5]
nums.sort() #sorts asecnding
print(nums)
#descending
nums.sort(reverse =True)
print(nums)
#use sorted method if you dont want to alter original list
fruits = ['Apple', 'Orange', 'Banana', 'Grapes']

sorted_fruits =  sorted(fruits)
print(sorted_fruits)
print(fruits)
print('Papaya' in fruits)
print('Orange' in fruits)

fruits_str = ', '.join(fruits)

print(fruits_str)
new_fruits_list = fruits_str.split(', ')
print(new_fruits_list)

#Tuples - are immutable

#Mutable behavior of lists
sports = ['Tennis', 'Hockey', 'Football', 'Archery']
olsports = sports #olsports is equal to sports
print(sports)
print(olsports)

sports[0] = 'Badminton' 
#changing in sports list , changes olsports as well.
print(sports)
print(olsports)

#Immutable behavior of tuples
#tuple uses Paranthesis instead of square brackets.
sauces = ('Mayo','Tomato','Mustard','Green Chilli')
hot_sauces = sauces
print(sauces)
print(hot_sauces)
# sauces[0] = 'Red Chilli' #Gives error here, because tuple is immutable
# print(sauces)
# print(hot_sauces)

#SETS - uses curly braces 
cs_courses = {'History', 'Humanities', 'Math', 'CompSci', 'Math'}
# will not be printed in the order they were added.
# the priting order may change with every other execution of print stmt.
#unlike lists or tuples , Sets don't follow order.
# because Sets are used primarily to identify the presence of a value in set (Membership test)
# or to remove duplicate values.
# Two Math items are present in set, but Only one Math item is printed.
print(cs_courses)

# The membership test is faster for Sets when compared to Lists or Tuples. 
# Sets are optimized for this test.
print('CompSci' in cs_courses)

art_courses = {'History', 'Sociology', 'Economics', 'Math'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))