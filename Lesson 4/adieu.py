import inflect

def main():
    p = inflect.engine()
    names = []
    
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    
    output = p.join(names) # Toma los nombres de la lista y los formatea

    print("Adieu, adieu to", output)

if __name__ == "__main__":
    main()