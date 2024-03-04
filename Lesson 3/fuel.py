def main():
    fuel()

def fuel():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            z = round(int(x) / int(y) * 100)
            if x > y:
                raise Exception("Invalid x or y values") # Crea un exception para evitar que X sea superior a Y
        except (ValueError, ZeroDivisionError, Exception):
            pass
        else:
            break
    
    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(z, "%", sep="")
    
        

main()