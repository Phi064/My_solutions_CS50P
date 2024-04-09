def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            z = round(int(x) / int(y) * 100)
            if x > y:
                raise Exception("Invalid x or y values") # Crea un exception para evitar que X sea superior a Y
        except (ValueError, ZeroDivisionError, Exception):
            fraction = input("Fraction: ")
        else:
            return z

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    
        
if __name__ == "__main__":
    main()