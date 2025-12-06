from time import sleep

def da_thing():
    sleep(1)
    print ("...")
    sleep(1)

def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
            da_thing
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number:")
            da_thing
name = input("Hey, I'm gonna help you do random maths stuff so can you tell me your name? ")
da_thing

number = getint(f"Hey {name}, can you please tell me a number and I'll just tell you if it is positive, negative or 0: ")
da_thing
if (number > 0):
    print ('This number is positive!')
elif (number < 0):
    print ("This number is negative!")
else:
    print ("This number is 0 which means it is neither negative nor positive")
da_thing