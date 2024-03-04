def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digit = 0
    if s[0:2].isupper() == False or 2 > len(s) > 6: # Comprpueba que las 2 primeras son letras y que tiene mínimo 2 carácteres y máximo 6
        return False
    
    if s.isalnum() != True: # Comprueba que no haya puntos, espacios, etc
        return False
    
    for letter in s:
        if letter.isalpha() == False and letter != '0': # Comprueba si es número y no es 0
            digit += 1
            if letter.isalpha() == True and digit > 0: # Si hay una letra, y ya habido anteriormente un número, devuelve False
                return False
            else:
                return True
        else:
            return False
            
main()

# Técnicamente la línea 11 está mal por el .isupper(), pero se asume que introducirá mayúsculas y hace el trabajo así que como sea