import random

ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%"

while 1:
    pl = int(input("How many character? : ")) 
    pn= int(input("how many variation? : ")) 
    for x in range(0,pn):

        p = ""

        for x in range(0,pl): 
            pc = random.choice(ch)

            p = p + pc

        print("Here is your strong password : ", p)
