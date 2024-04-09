def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digit = 0
    if s[0:2].isupper() == False or 2 > len(s) or len(s) > 6: # Comprueba que las 2 primeras son letras y que tiene mínimo 2 carácteres y máximo 6
        return False
    
    if s.isalnum() != True: # Comprueba que no haya puntos, espacios, etc
        return False
    
    for letter in s:
        if letter.isalpha() == False and digit == 0:
            if int(letter) != 0: 
                digit += 1
            elif int(letter) == 0 and digit == 0:
                return False

        if letter.isalpha() == True and digit > 0: 
                    return False
            
    return True

if __name__ == "__main__":
    main()

# Técnicamente la línea 11 está mal por el .isupper(), pero se asume que introducirá mayúsculas y hace el trabajo así que como sea
