#1
my_list = [1,2,3,4,5,7,8,9,10]
i = 0
while i < len(my_list):
    print(my_list[i])
    i+=1

#2 Why does this not work
another_list = [1,3,5,7,9]
i = len(another_list)
while i >= 0:
    #only change below here
    print(f"{another_list[i-1]} is an odd number!")
    i -= 1

#3
items = []
for item in [3,4,5,6]:
    items.append(item * 10)
print(items)

#4
stuff = ["Cars","Trucks","Planes"]
for item in stuff:
    print(f"I Really like my {item}")