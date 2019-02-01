value=[]
value.extend([11,11,2,22,23,3,2])#add more than a value inv a list
value.append(55)#add single value
print(value)
print(value.count(11))#count no.of given value
value.insert(3,12)#insert value @ given position (position,value)
print(value)
value[2]=99#replace the value 
print(value)
value.remove(99)#remove the value
value.pop(1)#remove the value on the given position
print(value)
value2=value.copy() #to copy the list
print(value2)
value.sort()#arranging in order
print(value)
print(len(value))#to know length of value
value3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(value3[0:9])#to take and print the value from given position(0-9)
print(value3[5:9])
print(value3)
value4=[]
value4=value3[11:14]#to copy the required value from previous list
print(value4)
print(value3[1:15:2])#value3[position:end position:itretation]
print(value3[-3])# '-'ve shows the value checking from RHS to LHS
print(value3[:])#to print all the values in a list "[:]"
print(value3[::-1])#to reverse the list 
value.extend(['YUGI',55.54,.5456])#can add various types
print(value)


