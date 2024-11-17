# This file is responsible for creating the code that will run inside fo userd.sh
# This is necessary because the user names are constantly changing and I do not
#feel like learning how to do reading of files through BASH.
# I am using this python script to that.  Deal with it.

#!/bin/python3

#This function reads the lines inside of a file and then generates a list based on that
def readfile(inputfilepath:str):
    file = open(inputfilepath, "r")
    names=[]

    for line in file:
        name = ""
        
        for char in line:
            
            if char != "\n":
                name = name + char
        
        names.append(name)
    
    file.close()

    return names

def writef(inputfile,name):
    print("sudo usrdel " + name, inputfile)

#Will write BASH code to userd.sh
def bashwrite(list_auth, list_full, inputfilepath):
    file = open(inputfilepath,"w")


    for name in list_full:
        
        if name in list_auth:
            pass
        
        else:
            print("sudo userdel " + name, file=file)

    file.close()

#This function is the main function in which calls all the other funtions
#This a common practice in python scripts as a way to encapsulate the code
#also it serves as a way to sand box the code a little better.
#It also gives you as space to call custom functions without interfering with the rest of the code.
def main():
    authorized = readfile("authorized.raw")
    all = readfile("totalusrs.raw")
    bashwrite(authorized, all, "userd.sh")


if __name__=="__main__":
    main()