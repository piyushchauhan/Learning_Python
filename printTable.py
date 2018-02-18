#Organising Lists of Lists in tablular Form
def GetNestedList:
    x=int(input("Enter the number of main items in the list: "))
    y=int(input("Enter the number of sub items that each list will contain: "))
    listOfList=[]
    for i in range(x):
        newList=[]
        for j in range(y):
            newList.append(input('('+str(i+1)+','+str(j+1)+'):'))
        listOfList.append(newList)
#DEBUGGER
GetNestedList(listOfList)
print(listOfList)
def printTable(nestedList):
    maxLen=0
    ColWidth=[]
    #this loop finds the max Length of any string in the nestedList
    for i in range(x):
        for j in range(y):
            if len(nestedList[i][j])>maxLen:
                ColWidth.insert(j,len(nestedList[i][j]))
            else:
                ColWidth.insert(j,maxLen)
    #Loop to display table
    for i in range(x):
        for j in range(y):
            print(nestedList[i][j].ljust(maxLen[j]),end='|')
        print()
printTable(listOfList)
