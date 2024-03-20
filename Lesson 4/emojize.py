import emoji

def main():
    sign = input("Input: ")
    print("Output:", emoji.emojize(sign, language="alias"))

if __name__ == "__main__":
    main()