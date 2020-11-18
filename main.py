

t, f= True, False
print(type(t))

print(t)
print(f)
print (t or f)
print (t and f)
print (not t)
print(t != f) # Not Equal
print(t==f) # Equal

# %s: is used as a placeholder for string values you want to inject into a formatted string.
# %d: is used as a placeholder for numeric or decimal values.
hello = "Hello"
world = "World"
world2 = '%s %d' % (world, len(world))
print(world2)

print(world, len(world))

hello= "Hello"
print(hello)
print(hello[0])
print(hello[1])
print(hello[2])
print(hello[3])
print(hello[4])

print(hello[2:4])  # [x:y] --> take the values from x th to y th but don't take y th value.
print(world)
print(world[1:4])
print(hello)
print(hello[:4])

print(world[2:4:1])   # [start:end:step]
city = "Istanbul"
print(city[0:6:2])

print("t" in city)
print("y" in city)

n=10
str(n)
print(type(n))

# y = input("Please enter a city name: ")  #input method always takes string type.
# print(y)

# print(type(y))

# x= int(input("Please enter an integer: "))
# print(x)
# print(type(x))

mylist = [3,5,6,7] # creating a list
print(mylist)

print(mylist[0])
print(mylist[2])
print(mylist[-1])
print(mylist[-3])

mylist[2] = "python"   # lists can be taken different types of data
print(mylist)

mylist.append('course')  # append(): adding some items end of the list
print(mylist)

mylist = [3,4,5,6,7]
mylist.append('course')
mylist.append('course')
print(mylist)

thelast = mylist.pop()  # pop(): removing the last item of the list
print(thelast)
print(mylist)

print(mylist.index("course"))

list2 = ["Python","Java","R","JavaScript","Ruby","Python","Python"]
print(list2.count("Python"))

list3 = [100,23,87,13,1000]
list3.sort()
print(list3)

list3.reverse()
print(list3)

mylist.extend(list3) # list extend.
print(mylist)

list_in_list = ["python","Java",3.2, 4, 11, [5,65,7,8,9]]
print(list_in_list[5])

print(mylist)
mylist.insert(5,55)   # insert(x,y) --> adding x th index the y value but don't change the x th value, it remains the same.
print(mylist)

list1 = list()
numbers = list(range(8))

print(numbers)
print(list1)

numbers2 = list(range(2,15,3)) #range(start, stop, step)
print(numbers2)
numbers2.reverse()
print(numbers2)

numbers[5:8] = [10,11,12]
print(numbers)

print(12 in numbers)

List4= [1,2,3] + [4,5]
print(List4)

List5= [1,2,3] * 3
print(List5)

List6= [[1,2],3,[4,5,6]]
print(List6[2][1])


