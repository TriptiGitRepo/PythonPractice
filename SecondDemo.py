#LIST

# #This is a List, this data type allows multiple values and can have different data types
values = [1,2,"tripti",4,5]


#printing using single index
print(values[0]) #prints 1
print(values[2]) #prints tripti
print(values[3]) #prints 4
print(values[-1]) #reference to the last index, prints 5

#printing a sequence of items in the given list
print(values[1:3]) #prints 2 and tripti because this only prints till n-1 item ie in this case 3-1

print(values)
#inserting another value to values list
values.insert(3,"Singh")
print(values)

#insert another item at the end of the list
values.append("End")
print(values)

#updating value
values[2] = "Tripti"

#deleting a value
del values[0]

print(values)

#Tuple

#This is a Tuple, this data type allows multiple values and can have different data types
#Tuple is similar to List, but it is Immutable

val = (1, 2, "Tripti",4.5)

print(val[1])
# val[2] = "Tripti"
#this will fail with error - TypeError: 'tuple' object does not support item assignment


#Dictionary

di1 ={"a":2,4:"bcd","c":"Hello World"}
print(di1[4])
print(di1["c"])

di2 ={}
di2["First Name"]="Tripti"
di2["Last Name"]="Singh"
di2["Gender"]="Female"
print(di2)
print(di2["Last Name"])