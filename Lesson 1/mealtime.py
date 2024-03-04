def main():
    time = input("What time is it? ") # Prompts the user for a time
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    # Outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all
    if 7 <= int(hours) <= 8:
        print("Breakfast time")
    elif 12 <= int(hours) <= 13:
        print("Lunch time")
    elif 18 <= int(hours) <= 19:
        print("Dinner time")

main()