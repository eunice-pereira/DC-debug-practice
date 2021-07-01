#1 Add both items to list
my_list = [1,3,5]
my_list.extend([7,9])
print(my_list)

#2
fruit = ["Pears", "Oranges", "Apples", "Bananas"]
del fruit[3] #I ate the bananas
print(fruit)

#3 use concatenate
result_list = []+["Item1"] + ["Item2"]+["Item3"]
print(result_list)

#4 update list
final_list = ["It's","The", "Final"]
final_list.append("Countdown!")
print(final_list)