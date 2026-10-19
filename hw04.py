# ------------------------------------------------------
#        Name: Jenny
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Continuously ask user for text input.
    If user enters secret_word, print secret word message and exit loop.
    If user enters dog or Dog, print dog/Dog message and exit loop.
    Otherwise print Try again and repeat input. """
    while True:
        text = input("Give me a sentence: ")
        if secret_word in text:
            print("You used the secret word!")
            break
        if "dog" in text or "Dog" in text:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else:
            print("Try again")



# Task 2
def check_greater():
    """ Continuously ask user for two integers.
    If first > second, print First is Greater and stop.
    If first < second, print Second is Greater and stop.
    If equal, print Try again and repeat. """
    while True:
        user1 = int(input("Give me a first integer: "))
        user2 = int(input("Give me a second integer: "))
        if user1 > user2:
            print("First is Greater")
            break
        elif user1 < user2:
            print("Second is Greater")
            break
        else:
            print("Try again")
            
        
    


# Task 3
def get_special_numbers():
    """ print numbers from 1 to 40 that are odd, divisible by 3 and not divisible by 5.
     """
    for num in range(1,41):
        if num%2 == 0:
            continue
        if num%3 != 0:
            continue
        if num%5 == 0:
            continue
        print(num)
            


# Task 4.a
def my_for_loop():
    """ Get a string input. If length <=2 or >5 or contains space, return early.
    Otherwise loop over each character, print if each character is vowel or consonant. """
    string = str(input("Give me a string: "))
    if len(string)< 2 or len(string)> 5  or " " in string:
        print("bad word")
        return
    else:
        vowels = {"a", "e", "i", "o", "u"}
        for char in string:
            if char.lower() in vowels:
                print(f"{char} is a vowel")
            else:
                print(f"{char} is a consonant")

# Task 4.b
def my_while_loop():
    """ Menu with options a,b,c.
    a repeats menu, b prints Goodbye and returns, c exits program, other input prints Try again. """
    while True:
        opt = input("Choose one option: a, b, or c: ")
        if opt == "a":
            continue      
        elif opt == "b":
            print("Goodbye")
            return        
        elif opt == "c":
            exit()
        else:
            print("try again")
    
        

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
