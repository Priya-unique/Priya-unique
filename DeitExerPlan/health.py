def getdate():
    import datetime
    return datetime.datetime.now()


def wr():
    n = input("1.Harry\n2.Larry\n3.Carry\nEnter the name: ")
    data = int(input("Enter 1.Exercise and 2.Diet: "))
    if n == "Harry":
        text = input("Input the data: ")
        if data == 1:
            with open("eharry.txt", "a") as f:
                f.write(str([str(getdate())])+":"+text+"\n")
        else:
            with open("dharry.txt", "a") as f:
                f.write(str([str(getdate())])+":"+text+"\n")
    elif n == "Larry":
        text = input("Input the data: ")
        if data == 1:
            with open("elarry.txt", "a") as f:
                f.write(str([str(getdate())])+":"+text+"\n")
        else:
            with open("dlarry.txt", "a") as f:
                f.write(str([str(getdate())])+":"+text+"\n")
    elif n == "Carry":
        text = input("Input the data: ")
        if data == 1:
            with open("ecarry.txt", "a") as f:
                f.write(str([str(getdate())])+":"+text+"\n")
        else:
            with open("dcarry.txt", "a") as f:
                f.write(str([str(getdate())])+":"+text+"\n")
    else:
        print("INVALID ENTRY")
    print("Successfully updated")


def re():
    n = input("1.Harry\n2.Larry\n3.Carry\nEnter the name: ")
    data = int(input("Enter 1.Exercise and 2.Diet: "))
    if n == "Harry":
        if data == 1:
            with open("eharry.txt") as f:
                a = f.read()
                print(a)
        else:
            with open("dharry.txt") as f:
                b = f.read()
                print(b)
    elif n == "Larry":
        if data == 1:
            with open("elarry.txt") as f:
                a = f.read()
                print(a)
        else:
            with open("dlarry.txt") as f:
                b = f.read()
                print(b)
    else:
        if data == 1:
            with open("ecarry.txt") as f:
                a = f.read()
                print(a)
        else:
            with open("dcarry.txt") as f:
                b = f.read()
                print(b)


do = 'no'
while do == 'no':
    ch = int(input("you want to 1.write or 2.retrieve the data: "))
    if ch == 1:
        wr()
    else:
        re()
    do = input("Do u want to exit say yes or no: ")
