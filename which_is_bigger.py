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

num_one = getint(f"Hey {name}, can you tell me the first number? ")
num_two = getint(f"Hey {name}, can you tell me the second number? ")
if (num_one > num_two):
    print (f"num_one is greater than num_two")
elif (num_one < num_two):
    print (f"num_one is less than num_two")
else:
    print ('They are equal')