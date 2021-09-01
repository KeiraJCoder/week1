import random

music = "Rock?", "Classical?", "Pop?", "Metal?", "Country?", "RnB?", "No music"
rand_music = random.choice(music)
def let():
    if rand_music == "Classical?":
        print(f"{rand_music} Tchaikovski? no....Beethoven? mmmm....I'll be Bach")
    elif rand_music == "No music? boooo":
        print(f"{rand_music} THE SILENCE IS DEAFENING!!!!!!")
    elif rand_music == "Rock?":
        print (f"{rand_music} Turn it up to 11!!!!")
    elif rand_music == "Pop?":
        print(f"{rand_music} Why even?")
    elif rand_music == "Metal?":
        print(f"{rand_music} *INCOHERENT SCREAMING*")
    elif rand_music == "Country?":
        print(f"{rand_music} A red truck, a dirt road, a cold beer, a corn field")
    elif rand_music == "RnB?":
        print(f"{rand_music} Turn off that noise! Damn whippersnappers.....")
    else:
        print ("Huh?")
let()