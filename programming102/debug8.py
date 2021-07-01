#1
def go_over(a,b):
    c = a*b
    return c

c = go_over(10,10)
print(c)

#2
def weird(args):
    return sum(args)

sum = weird([1,3,4])
print(sum)

new_sum = weird([4,5,6])
print(new_sum)