from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts=figlet.getFonts() # Pilla las fuentes

# Comprueba que no haya argumentos y pone una fuente aleatoria
    if len(sys.argv) == 1:
        text = input("Input: ")
        rand_font = random.choice(fonts)
        figlet.setFont(font=rand_font)
        print(figlet.renderText(text))

# Comprueba el número de argumentos, que sean correctos y si la fuente existe
    elif len(sys.argv) == 3 and sys.argv[2] in fonts:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit("Invalid Usage")

    else:
        sys.exit("Invalid Usage")


if __name__ == "__main__":
    main()