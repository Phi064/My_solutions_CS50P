# Implement a function that takes a str and convert any :) to 🙂 and any :( to 🙁
def convert(faces):
    return faces.replace(":)","🙂").replace(":(", "🙁")

# Implement a function called main that prompts the user for input, calls convert on that input, and prints the result
def main():
    phrase = input("What do you want to say? ")
    print(convert(phrase))

main()