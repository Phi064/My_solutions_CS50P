def main():
    camel = input("camelCase: ") # Toma Input en camelCase
    convert_camel(camel)

def convert_camel(camel):
    print("snake_case: ", end="") # Printea el "snake_case: "
    for letter in camel: # Por cada letra en la palabra
        if letter.isupper() == False: # Si la letra es minúscula
            print(letter, end="") # Printea la letra tal cual
        else: # Si es mayúscula
            print("_", letter.lower(), sep="", end="") # Printea primero un guión bajo y luego la letra en minúscula
    print() # Printea un \n para el final

main()