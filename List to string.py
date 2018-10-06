"""
Write a function that takes a list value as an argument and returns a string with all the
items separated by a comma and a space, with and inserted before the last item. For
example, passing the previous spam list to the function would return 'apples, bananas,
tofu, and cats'. But your function should be able to work with any list value passed to
it.
"""
print('Hello there')
while True:
    try:
        length=int(input('Type the length of the list you are going to make: '))
    except ValueError:
        print("Please enter a natural number.")
        continue
    if length!=0:
        break
'''

'''
list=[]
for i in range(length):
    list.append(input("Enter item no "+str(i+1)+": "))
string=''
for i in range(length):
    if i==length-2:
        string=string+str(list[i])
        string=string+' and '
    elif i==length-1:
        string=string+str(list[i])+'.'
    else:
        string=string+str(list[i])+', '
print("Your list contains : "+string)
