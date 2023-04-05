#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with a while loop along with a try...except 
# block so that the user will keep entering in a number
# until they have entered a value integer value
a = 0
b = 0 
while True:
    try:
        a = input("type a number")
        b = int(a)
        print (f"you're number is {b}")
        break
    except:
        print ("NOT A NUMBER DUMBASS RUN IT BACK")