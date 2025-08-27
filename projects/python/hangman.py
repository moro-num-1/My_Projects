import random
def hang_man(head, left_hand, body, right_hand, left_leg, right_leg):
    print(" +---+")
    print(f" {head}   |")
    print(f"{left_hand}{body}{right_hand}  |")
    print(f"{left_leg} {right_leg}  |")
    print("     |")
    print("=========")

def main():
    words = [
    "apple", "banana", "grape", "orange", "peach", "lemon", "melon", "berry", "cherry", "mango",
    "kiwi", "plum", "apricot", "fig", "pear", "coconut", "olive", "date", "lime", "papaya",
    "guava", "tomato", "onion", "garlic", "carrot", "potato", "pepper", "broccoli", "cabbage", "spinach",
    "lettuce", "celery", "beans", "peas", "rice", "bread", "pasta", "pizza", "cheese", "butter",
    "sugar", "honey", "milk", "cream", "coffee", "tea", "water", "juice", "soda", "cake",
    "candy", "chocolate", "cookie", "house", "room", "door", "chair", "table", "window", "garden",
    "street", "school", "class", "teacher", "student", "book", "pencil", "paper", "phone", "clock",
    "radio", "music", "guitar", "piano", "violin", "drum", "light", "star", "moon", "sun",
    "earth", "cloud", "rain", "storm", "river", "ocean", "island", "forest", "desert", "mountain",
    "stone", "fire", "snow", "wind", "train", "plane", "truck", "ship", "horse", "tiger",
    "zebra", "snake"
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