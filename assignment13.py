# Write a python script to store multiple items in a single variable ( Items are “Java”
# ,“Python”, “SQL”, “C” ) using list

items = ['Java',"Python",'Sql','C']
print(items)

# 2. Write a python script to get the data type of a list.
print(type(list()))

# 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["Java", "C", "Python"]
print(mylist[-1])

# 4. Write a python script to Change the values "SQL" and "Reactnative" with the values
# "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
# "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
for i in thislist:
    if(i=='SQL' or i=='Reactnative'):
        thislist.remove(i)
        if i=='SQL':
            thislist.insert(1,"NoSQL")
        else:
            thislist.insert(3,"Flutter")
print(thislist)

# 5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
# ["Java", "SQL", "C", "Reactnative"]

mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append('Python')
print(mylist)

# 6. Write a python program to append elements from another list to the current list.

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] 

print(firstlist+secondlist) # First Method as I understand the problem

for i in secondlist:
    firstlist.append(i)
print(firstlist) # Second Method According to the problem language

# 7. Write a python program to Print all items by referring to their index number (thislist =
# ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

for i in range(len(thislist)):
    print(thislist[i],' and index->',i)

# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
# "C", "Reactjs", "Javascript", "Python"]

thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
sortedList = sorted(thislist)
print(sortedList)
thislist.sort()
print(thislist)
print(sorted(thislist))

# 9. Write a Python script to create a list of city names taken from the user.

citynames = input("Enter list of citynames")
eval(citynames)
print(citynames)

# 10. Write a Python script to create a list, where each element of the list is a digit of a
# given number.

number = input('Enter any number')
print(list(number))