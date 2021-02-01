# Ian Mcloughlin 
# Python basics
# 2021-01-30

print("Hello, World!")

a = 1
b = 1.0
s = "Hello, world from  a String!"
t = '"Hello", from a diffrent String!'

print(a, b, s, t)#Print the four variables to screen

print(type(b))#What type is b

print(s[0]) #Whats the first character of string s

print(s[0:2])#Print out substring

print(s[3:10:2])#For loop to search string ( 3 is your i, 3 <10 , interate by 2)

x = [1, 2, 3, "Hello"]
print(x)
print(x[0])
print(x[2])
print(x[-1])

#Loop through x array 
#for i in x[::2] give me every second element of x
for i in x:
    print(i)
    print(i + i)

for i in range(10):
    print(i)

d = {"no_wheels": 4, "make": "Skoda"}#Dictionary
#list comprehensions
d["model"] = "Superb" #Giving a dictionary element a key
print(d["no_wheels"])

r = [1,2,3,4]#list

print(r)

s = [i*i for i in r]#lit made using another list 

print(s)