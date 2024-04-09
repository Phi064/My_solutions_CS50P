def main():

    twitter = input("Input: ")
    print("Output: ", end='')
    print(shorten(twitter))
    print() # Printea un /n para que no quede feo

def shorten(twitter):
    s = ""
    full_tweet = []
    for tweet in twitter: # Por cada letra 
        if tweet.lower() == "a" or tweet.lower() == "e" or tweet.lower() == "i" or tweet.lower() == "o" or tweet.lower() == "u": # Si es vocal
            continue # Ignórala
        full_tweet += tweet

    return s.join(full_tweet).lower()

if __name__ == "__main__":
    main()