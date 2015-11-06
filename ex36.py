from sys import exit

def mountains():
    print "There is a tiger in the mountains, What are you doing? taunt or flee?"

    choice = raw_input(">")
    if choice == "taunt":
        print "Congratulation! Tiger run away!"
        print "Then you go down the mountains and walk in the road."
        walk()
    elif choice == "flee":
        dead("You are coward!")
        exit(0)
    else:
        print "I don't know what you input?"
        mountains()



def walk():
    print "You will see a house on the road,What will you do? flee or into?"

    choice = raw_input(">")
    if choice == "flee":
        print "You are so coward!"
        dead()
    elif choice == "into":
        print "There are banana egg and mango in the table,which do you choice?"

        choice = raw_input(">")
        if choice == "banana":
            print "You are look like a lecher man,but pure inside."
            exit(0)
        elif choice == "egg":
            print "You are look like a pure man but actually a lecher man."
            exit(0)
        else:
            print "You are look like a lecher man but you are so pure."
            exit(0)
    else:
        print "I don't know what your input , please input again."
        walk()



def swim():
    print "While you swimming, you see a shark.What would you do? flee or flight?"
    choice = raw_input(">")
    if choice == "flee":
        print "You are a coward!"
        dead()
    else:
        print "shark run away! You can see some gold."
        gold()



def gold():
    print "There are full of golds, how much would you take?"

    choice = raw_input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)

    else:
        dead("Hey man! You should learn how to type a number.")

    if how_much < 100:
        print "Nice, you are not greedy, you win!"
        exit(0)
    else:
        print "You are so greedy!"
        dead()



def dead(why):
    print why, "good job!"
    exit(0)


def start():
    print "Welcome to my game!"
    print "What's your favorite sports?"
    print "climb mountains walk or swimming!"
    print "You have five times to input you words?"

    i = 0

    while i < 5:
        choice = raw_input(">")
        if choice == "climb mountains":
            mountains()
        elif choice == "walk":
            walk()
        elif choice == "swimming":
            swim()
        else:
            print "I don't know what your input,please input again."

        i += 1

start()
