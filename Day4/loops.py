favourite_drinks = ["Coke", "Pepsi", "Monster"]

for x in favourite_drinks: 
    print (x)

for i in range (2, 12, 1):
    print (i) 

name = ""

while len(name) == 0: #while the length of name is equal to zero 
    name = input("Enter your name: ") #ask the user to enter their name

print ("Hello " +name + " you filthy swine!")

films = [
    "Deadpool",
    "Donnie Darko",
    "Moana"]


for films in films:

    print(films)
def film_check():
    if films[2] == "Ghostbusters":
        print ("Yay, its Ghostbusters!!!")
    else:
        print ("Booooo, we want ghostbusters")
film_check()


import time

for seconds in range (9,0,-1):
    print (seconds)
    time.sleep(1)
print ("KEIRA IS F***ING AMAZING!!!!!!!!")

name = ""

while len(name) == 0: #while the length of name is equal to zero 
    name = input("Enter your name: ") #ask the user to enter their name
    
print ("Hello " +name)

num = 0
while num <10: #while number is less than 10, keep printing
    num+= 1
    print (num)

    import random

    rand_num = random.randint(0,50)
    my_num = 50
    while rand_num != my_num:
        print (rand_num)
        rand_num = random.randint(0,50)

print ("You've found {}".format(my_num))

for x in range(13):
    print("Hello World ")
print()

x = 1
while x <= 13:
    print ("Hello World")
    x += 1

# Python program to shuffle a deck of card

current_card = [
    ]
random.randint (1,len(current_card))

current_card = ""
cards = ["Diamond", "Spade", "Club", "Hearts"]
pick_card = random.choice(cards)

print("Your card is", pick_card)

while pick_card != current_card:
    current_card = random.choice(cards)
    print(current_card)