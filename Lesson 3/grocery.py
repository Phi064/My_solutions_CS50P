def main():
    items = {}
    i = 0

    while True:
        try:
            item = input().upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            for key in sorted(items.keys()):
                print(items[key], key)
            break


main()