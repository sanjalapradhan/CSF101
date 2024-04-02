fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits: 
    print(x)
    if x == "banana":
        continue #or you can also use "break" to break the list while running 

    fruits = ["apple", "banana", "cherry"]
for x in fruits: 
    if x == "banana":
        continue
    print(x)

 #range function: for loop
for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

 #else function
for x in range(6):
    print(x)
else:
    print("finally finished!")
    


