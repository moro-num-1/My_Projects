import random
def hang_man(head, left_hand, body, right_hand, left_leg, right_leg):
    print(" +---+")
    print(f" {head}   |")
    print(f"{left_hand}{body}{right_hand}  |")
    
    
    

def 
    
    
    
    
    
    
    
    
    
    
    
    
    ]
    word = random.choice(words)
    hide_word = ["_" for _ in range(len(word))]
    wrong_guesses = 6
    while wrong_guesses > 0:
        print(f"Word: {hide_word}")
        guess = input("Enter your guess: ")
        if len(guess) > 1:
            print("Just one character valid!!")
            continue
        if guess.isdigit():
            print("Only letters are allowed!!")
            continue
        ltr_ind = 0
        while ltr_ind < len(word):
            if guess == word[ltr_ind]:
                hide_word[ltr_ind] = guess
            
            ltr_ind += 1

                    
                
if __name__ == "__main__":
    main()
