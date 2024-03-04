def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        date = input("Date: ").title()
        try:
            if "/" in date:  # Clasifica por MM/DD/YYYY
                month, day, year = date.split("/")
            elif "," in date:  # Clasifica por MM DD, YYYY
                monthday, year = date.split(",")  # Divide la fecha en meses/días y años
                month, day = monthday.split(" ")  # Divide los meses y días
                month = (
                    months.index(month) + 1
                )  # Obtiene el index del mes (empieza por 0, de ahí el +1)

            if (
                int(day) > 31 or int(month) > 12
            ):  # Filtra días superiores al 31 o meses superiores al 12
                continue

        except ValueError:
            pass

        else:
            break

    print(f"{int(year):04}-{int(month):02}-{int(day):02}")


main()
