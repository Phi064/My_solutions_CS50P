def main():
    due = 50

    while due > 0:
        print(f"Amount Due: {due}") # Printea la deuda
        coin = int(input("Insert Coin: ")) # Pide el input de la moneda
        if coin != 25 and coin != 10 and coin != 5: # Valida que la moneda sea de 25, 10 o 5
            continue
        due -= coin # Resta la deuda con la moneda introducida
    
    if due <= 0: # Si la deuda es negativa
        print(f"Change Owed: {-due}") # Printea el negativo de la deuda (lo necesario para llegar a 0)

main()