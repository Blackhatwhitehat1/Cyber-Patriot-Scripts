# This file is responsible for creating the code that will run inside fo userd.sh
# This is necessary because the user names are constantly changing and I do not
#feel like learning how to do reading of files through BASH.
# I am using this python script to that.  Deal with it.

def readfile(filepath:str):
    file = open(filepath, "r")
    names=[]

    for line in file:
        name = ""
        for char in line:
            if char != "\n":
                name = name + char
        
        names.append(name)

    return names

#This function is the main function in which calls all the other funtions
#This a common practice in python scripts as a way to encapsulate the code
#also it serves as a way to sand box the code a little better.
#It also gives you as space to call custom functions without interfering with the rest of the code.
def main():
    print(readfile("authorized.raw"))


if __name__=="__main__":
    main()