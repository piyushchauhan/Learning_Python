#! python3
# birthdayDatabase.py
# import shelve
# file=shelve.open('birthdayDatabase')
bday = {'Aditi': (25, 9, 1999), 'Sagar': (15, 1, 2000), 'Piyush': (5, 9, 1999), 'Piyush Ranjan': (28, 4, 1999)}
while True:
    name = input('Enter a name(blank to quit):')
    if name == '':
        break
    if name in bday:
        print(str(bday[name]) + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        bday = input('What is their birthday? ')
        bday[name] = bday
        print('Birthday database updated.')
        # file['birthdays']=birthdays
        # file.close()
