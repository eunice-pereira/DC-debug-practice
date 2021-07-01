#1
x = 10
def add_to_x(a):
    global x
    x = a + x
    print(x)
    return x

result = add_to_x(4)+ add_to_x(2)
print(result)

#2
def give_me_something(c):
    return c/2

print(give_me_something(22))
print(give_me_something(33))
