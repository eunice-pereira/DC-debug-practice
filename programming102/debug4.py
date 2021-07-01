# Should be a list of 3 lists
grouped_list = [
    [
        "kittens",
        "birds",
        "meat"],
    [
        "Children", 
        "people", 
        "Aliens"],
    ["More","Less","Other"]
]
print(grouped_list)

#2 List the actors credits individually
actor_list = [
    ["Star Wars", "Indiana Jones", "The Fugative"],
    ["Star Wars", "Batman Cartoons", "Master of Orion"],
    ["Star Wars", "Community", "Atlanta"]
]
for actor in actor_list:
    print("Who is this actor? \nHe appeared in:")
    for idx, media in enumerate(actor): 
     print(f"{idx+1}. {media}")
   