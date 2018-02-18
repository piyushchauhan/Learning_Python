import random,sys,os
class animal    #creating a class
    __name=""   #Two under score represents that it is a private variable
    __height=0  #To change a private variable in a class we need to use a
    __weight=0  #function of that class

    def __init__(self,name,height,weight,sound):    #this is constructor
        self.__name=name
        self.__weight=weight
        self.__height=height


    def set_name(self,name):  #defi
        self.__name=name
    def get_name(self):
        return self.__name
    def 