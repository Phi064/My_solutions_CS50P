def main():
    # Prompt the user for a greeting, remove whitespaces and sensitiveness
    greets = input("Greeting: ").lower().strip()
    print(value(greets))

def value(greeting):
    # If the greeting starts with "hello", output 0$
    if  greeting.lower().startswith("hello") == True:
        return 0

    # If the greeting starts with an "h", but not "hello", output 20$
    elif greeting.lower().startswith("h") == True:
        return 20

    # Otherwise, output 100$
    else:
        return 100

if __name__ == "__main__":
    main()