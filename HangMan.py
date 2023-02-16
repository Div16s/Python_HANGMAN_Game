import random  #importing random library to choose random words from word_list
from words import word_list

def get_word():
    word = random.choice(word_list)  #choosing a word randomly from the word_list
    return word.upper()   #returning randomly chosen word all in uppercase



def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []  #list that will contain the letters guessed by player
    tries = 6
    name = input("Enter your name: ")
    print("\n")
    print("-----"+name+", Let's Play The HangMan-----🎮🤖")
    print(display_HANGMAN(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()

        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word❌")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("Good job👍",guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        else:
            print("Not a valid guess!! 🥲")
        
        print(display_HANGMAN(tries))
        print(word_completion)
        print("\n")

    if(guessed==True):
        print("Congrats " + name + " 🎉🥳, you guessed the word, YOU WIN🏆")
    else:
        print("Sorry",name,"you ran out of tries. The word was " + word + ", maybe next time!")


def display_HANGMAN(tries):
    stages = ["""
               ------------
               |          |
               |          O
               |         /|\
               |         / \
               |
             """,
             """
               ------------
               |          |
               |          O
               |         /|\
               |         / 
               |
             """,
             """
               ------------
               |          |
               |          O
               |         /|\
               |          
               |
             """,
             """
               ------------
               |          |
               |          O
               |         /|
               |          
               |
             """,
             """
               ------------
               |          |
               |          O
               |          |
               |          
               |
             """,
             """
               ------------
               |          |
               |          O
               |         
               |          
               |
             """,
             """
               ------------
               |          |
               |          
               |         
               |          
               |
             """]
    return stages[tries]



def main():
    word = get_word()
    play(word)
    while input("Do you wanna play again? (Yes/No): ").upper() == "YES":
        word = get_word()
        play(word)

if __name__=="__main__":
    main()
    




