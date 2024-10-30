import random
names = []
print('Add names to shuffle! \nPress "S" to stop')
while True:
    add_name = input('Add name: ')
    if add_name.lower() != 's':
        names.append(add_name)
    else:
        random_name = random.choice(names)
        print('Chosen person: ' + random_name)
        break
