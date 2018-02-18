birthdays={'Aditi':'Sept 25','Sagar':'Jan 15', 'Piyush':'Sept 5','Piyush Ranjan':'Apr 28'}
while True:
    name=input('Enter a name(blank to quit):')
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of ' +name)
    else:
        print('I do not have birthday information for '+name)
        bday=input('What is their birthday? ')
        birthdays[name]=bday
        print('Birthday database updated.')