#1 modify a and b to test script as needed
a == 10
b = 10

if a > b:
    print('A is bigger')
else a < b:
    print("A is smaller")
else:
    print("{a} and {b} are the same number")

# Fix errors
if a = 10:
    print("A is equal to 10!!")
else:
    b == 10
    print("{b} is equal to 10!")

#3 No errors, but doesnt work properly make where
if a > 0:
    print("A is larger than 0 and nothing else!")
elif a > 5:
    print("A is larger than 5 and nothing else!")
elif a == 10:
    print("A is just barely larger than 10!!!")
else:
    print("Wow a is greater than 10")
