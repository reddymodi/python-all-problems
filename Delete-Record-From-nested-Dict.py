#Python Program to delete a record from nested dictionary
  # people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
   #       2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}

people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
del people[1]['profession']
print(people)