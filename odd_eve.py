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
            print (f"{e}\n\nPlease enter a whole number:")
            da_thing

name = input("Hey, I'm gonna help you do random maths stuff so can you tell me your name? ")
da_thing
number = getint(f"Hey {name}, can you please tell me a number and I'll just tell you if it is odd or eve: ")
da_thing
numbert = number%2
if (numbert == 0):
    print ("Even")
else:
    print ("Odd")