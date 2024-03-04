twitter = input("Input: ")
print("Output: ", end='')
for tweet in twitter: # Por cada letra 
    if tweet.lower() == "a" or tweet.lower() == "e" or tweet.lower() == "i" or tweet.lower() == "o" or tweet.lower() == "u": # Si es vocal
        continue # Ignórala
    print(tweet, end='') # Printea la letra

print() # Printea un /n para que no quede feo