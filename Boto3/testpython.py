
first_name = "Monty"
last_name = "Python"
print(first_name + " " + last_name)

first_name = "John"
surname = "Doe."
print("My first name is {}. My family name is {}".format(first_name, surname))

firstname = "Jane"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")

my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

user = {"first_name":"Ada"}
print(user)
{'first_name': 'Ada'}

user = {"first_name":"Ada"}
print(user["first_name"])

user["family_name"] = "Byron"
print(user)

user["family_name"] = "Lovelace"
print(user)

del user["family_name"]
print(user)

fruit = ["apples","oranges","bananas"]
print(fruit[1])

print(fruit[-1])
print(fruit[-2])

fruit.append("kiwi")
print(fruit)

fruit.insert(2, "passion fruit")
print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

fruit.sort()
print(fruit)
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']

fruit.reverse()
print(fruit)


del fruit[1]
print(fruit)
['passion fruit', 'kiwi', 'bananas', 'apples']

favorite_fruit = fruit.pop()
print(favorite_fruit)

fresh_fruit = fruit.pop(1)
print(fresh_fruit)

fruit.remove('bananas')
print(fruit)
['passion fruit']

print(fruit)

my_variable = "A string"
print(type(my_variable))

my_variable = "A string"
print(str(my_variable))

my_number = 50
some_string = "The number is "
print(some_string + str(my_number))















