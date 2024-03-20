import random

def main():
    level = get_level("Level: ")
    for i in range(10): # Loop para obtener las 10 preguntas
        x, y = generate_integer(level)
        result = x + y
        counter = 0 # Cuenta cuántas veces se ha intentado un problema, si no se resuelve, muestra la solución
        for j in range(3): # Loop para dar 3 intentos
            print(f"{x} + {y}: ", end="")
            guess = input_ver() # Verifica que sea un número entero superior a 0
            if guess != result:
                print("EEE")
                counter += 1
                if counter == 3:
                    print(f"{x} + {y} = {result}")
            else:
                break

def generate_integer(level): # Genera X e Y
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(0,99)
        y = random.randint(0,99)
    elif level == 3:
        x = random.randint(0,999)
        y = random.randint(0,999)
    
    return x, y

def get_level(prompt): # Verifica si es 1, 2 o 3
    while True:
        try:
            user_input = int(input(prompt))
            if user_input != 1 and user_input != 2 and user_input != 3:
                raise Exception("Number has to be 1, 2 or 3")
        except(ValueError, Exception):
            pass
        else:
            return user_input

def input_ver(): # Verifica si es un número entero positivo
    while True:
        try:
            user_input = int(input())
            if user_input <= 0:
                raise Exception("Number has to be superior to 0")
        except(ValueError, Exception):
            print("Has to be a number superior to 0")
            pass
        else:
            return user_input

if __name__ == "__main__":
    main()