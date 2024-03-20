import sys, requests, json

def main():
    num = input_validator()
    print(get_bitcoin(num))

def input_validator(): # Comprueba que tiene los argumentos necesarios y correctos
    try:
        user_bitcoin = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        return user_bitcoin
    
def get_bitcoin(num): # Intenta obtener el JSON, obtiene el precio y lo multiplica
    try:
        bitcoins = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        )

    except requests.RequestException:
        sys.exit()

    else:
        bitcoin_json = bitcoins.json()
        price = bitcoin_json["bpi"]["USD"]["rate_float"] * num
        return f"${price:,.4f}"
    

if __name__ == "__main__":
    main()