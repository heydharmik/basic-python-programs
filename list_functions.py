

lucky_numbers =[3, 8 ,15, 16, 23, 42]
friends = ["Niraj", "Tushar", "Juzar","Juzar", "Chintan", "Aniket"]

#  friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Nayan")
friends.remove("Chintan")
#  friends.clear()
friends.pop()
print(friends.index("Aniket"))
print(friends.count("Juzar"))
friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
