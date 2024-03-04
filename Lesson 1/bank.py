# Prompt the user for a greeting, remove whitespaces and sensitiveness
greeting = input("Greeting: ").lower().strip()

# If the greeting starts with "hello", output 0$
if  greeting.startswith("hello") == True:
    print("0$")

# If the greeting starts with an "h", but not "hello", output 20$
elif greeting.startswith("h" or "H") == True:
    print("20$")

# Otherwise, output 100$
else:
    print("100$")