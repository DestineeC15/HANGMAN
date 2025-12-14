# importing random
import random

# creating category lists

animals = ['ANACONDA','LEOPARD','IGUANA','HUMMINGBIRD','KANGAROO','ZEBRA','VULTURE','RHINOCEROS','ZEBU','GIRAFFE']
sports = ['HOCKEY','CRICKET','GYMNASTICS','BASKETBALL','FOOTBALL','BADMINTON','SWIMMING','VOLLEYBALL','RUGBY','WRESTLING']
countries = ['UZBEKISTAN','AUSTRALIA','ZIMBABABWE','CHILE','FRANCE','MALAYSIA','BOLIVIA','CZECHIA','YEMEN','SURINAME']
languages = ['URDU','ARABIC','HEBREW','CROATIAN','RUSSIAN','ROMANIAN','JAVANESE','ENGLISH','GREEK','GUJARATI']
food = ['CUPCAKE','BURGER','CROISSANT','NIHARI','KORMA','SAUSAGE','PIZZA','WAFFLES','RAMEN','SHAWARMA']


valid_input = False

while not valid_input:
    print("Please choose a category by entering the number representing each category.")
    user_input = input("1: Animals, 2: Sports, 3: Countries, 4: Languages, 5: Food  ")

    try:
        chosen_category = int(user_input)

        match chosen_category:
            case 1:
                chosen_word = random.choice(animals)
                valid_input = True
            case 2:
                chosen_word = random.choice(sports)
                valid_input = True
            case 3:
                chosen_word = random.choice(countries)
                valid_input = True
            case 4:
                chosen_word = random.choice(languages)
                valid_input = True
            case 5: 
                chosen_word = random.choice(food)
                valid_input = True
            case _:
                print("Invalid input!")
    except ValueError:
        print("Please enter valid number for the category")



display = []
for _ in range(len(chosen_word)):
    display.append("_")
print(display)

# guesses
guesses = 7
while "_" in display and guesses > 0:
    player_guess = input("Please enter the letter that you have guessed: ").upper()
    
    if  player_guess == chosen_word:
        display = list(chosen_word)
        continue # will skip and go to final part of the loop

    elif player_guess in chosen_word:

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if player_guess == letter:
                display[position] = player_guess
        print(f"You guessed correctly! The word looks like {display}")    # this outside for loop so that it doesn't print the message twice for when we have the same letter appear more than once in the word


    else:
        guesses -= 1
        print(f"Oops! That was an incorrect guess! Guesses left: {guesses} ")

if guesses == 0:
    print(f"You lose! The word was {chosen_word} ")
else:
    print(f"You win! The word was {chosen_word} ")
           



