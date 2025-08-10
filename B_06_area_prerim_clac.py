def num_check(question):
    """ask user for width and loop until they enter a number that is more than 0"""
    error1 = "please pick a number above zero\n you want to calculate stuff, dont you?"
    error2 = "please pick a NUMBER to continue calculating"
    while True:

        try:
            #ask user for width
            response = float(input(question))

            #check that width is more than 0
            if response > 0:
                return response
            else:
                print(error1)
        except ValueError:
            print(error2)
#main routine starts here

keep_going = ""
while keep_going == "":

    #get width and height
    width = num_check("width: ")
    height = num_check("height: ")
    #calculate area perimeter
    area = height * width
    perimeter = 2 * (height + width)
    #display output
    print()
    print(f"the area is {area} square units")
    print(f"the perimeter is {perimeter} square units")
    #ask user if they want to keep going
    keep_going = input("press any key to exit or enter to go again")

print("thank you for using the area perimeter calculator")