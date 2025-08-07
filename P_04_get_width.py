#ask user for width and loop until they enter a number that is more than 0
error1 = "please pick a number above zero\n you want to calculate stuff, dont you?"
error2 = "please pick a NUMBER to continue calculating"
while True:

    try:
        #ask user for width
        width = float(input("width: "))

        #check that width is more than 0
        if width > 0:
            break
        else:
            print(error1)
    except ValueError:
        print(error2)
