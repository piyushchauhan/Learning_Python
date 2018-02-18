'''
Random Chore Assignment Emailer

Write a program that takes a list of people’s email addresses and a list of chores
that need to be done and randomly assigns chores to people. Email each person
their assigned chores. If you’re feeling ambitious, keep a record of each
person’s previously assigned chores so that you can make sure the program avoids
assigning anyone the same chore they did last time. For another possible feature,
schedule the program to run once a week automatically.

Here’s a hint: If you pass a list to the random.choice() function, it will return
a randomly selected item from the list. Part of your code could look like this:


chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
randomChore = random.choice(chores)
chores.remove(randomChore) # this chore is now taken, so remove it
'''
