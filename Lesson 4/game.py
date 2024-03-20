import random

def main():
    level = input_ver("Level: ")
    number = random.randint(1, level)
    while True:
        guess = input_ver("Guess: ")
        
        if guess < number:
            print("Too Small!")
            continue
        elif guess > number:
            print("Too Large!")
            continue
        else:
            break
    
    print("Just Right!")
    

def input_ver(prompt): # Verifica si es un número entero positivo
    while True:
        try:
            user_input = int(input(prompt))
            if user_input <= 0:
                raise Exception("Number has to be superior to 0")
        except(ValueError, Exception):
            pass
        else:
            return user_input


if __name__ == "__main__":
    main()