
#ask user for width and loop until they enter a number that is more than 0
def num_check(question):
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


#main routine goes here
for item in range(0, 2):
    width = num_check("width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("height: ")
    print(height)