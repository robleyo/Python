#creating empty list
teams = []
#inserting into list using insert method
teams.insert(0, "Miami")
teams.insert(1, "Philadelphia")
teams.insert(2, "Toronto")
teams.insert(3, "Milwaukee")
teams.insert(4, "Memphis")
#inserting into list using append method
teams.append("Brooklyn")
teams.append("Boston")
teams.append("Chicago")
teams.append("New York")
teams.append("Los Angeles")
print (teams)
x = len(teams)
print(f'there are {x} teams')
#deleting from the list using a name
teams.remove("Philadelphia") 
print (teams)
x = len(teams)
print(f'there are {x} teams')
#deleting from list by index
del teams[8]
print(teams)
x = len(teams)
print(f'there are {x} teams')


