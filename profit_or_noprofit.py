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

name = input("Hey, I'm gonna help you do random maths stuff about pofit/loss so can you tell me your name? ")
da_thing
how_much_made= getint(f"Hey, {name}, can you tell me how much money you have made this quarter? ")
invested = getint(f"Hey, {name}, can you tell me how much money you have spent this quarter? ")
da_thing
if (invested > how_much_made):
    print (f"Your in debt of {invested-how_much_made}")
elif (invested < how_much_made):
    print (f"You made a profit of {how_much_made-invested}")
elif (invested == how_much_made):
    print ("Your just barely breaking even")
else:
    pass
da_thing