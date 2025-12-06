#Imports
from time import sleep

#Functions
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

#Name
name = input("Hey, I'm gonna help you pick out your clothing so can you tell me your name? ")
da_thing

#Getting data
tempreature = getint(f"Hey {name}, can you tell me the tempreature? ")

#processing
da_thing

#Output
if (tempreature < 0):
    print (f"{name}, i think you should wear a really thick clothes, its freezing outside")
elif (tempreature < 10):
    print (f"{name}, its pretty cold outside it think you should wear thick clothes")
elif (tempreature < 20):
    print ("Its a bit chilly outside, wear slightly thick clothes")
elif (tempreature < 30):
    print ("Its a nice tempreature outside, wear casual clothes")
elif (tempreature < 40):
    print ("Its pretty hot outside, you should wear shorts and a tshirt")
else:
    print ("Its really hot outside, wear thin shorts and tshirt also drink alot of water")