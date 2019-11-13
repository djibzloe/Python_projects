def ask():
    while True:
        try:
            x = int(input("Input an integer:"))
            x=x**2
            print(f"integer**2 = {x}")
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print("Done!")
            break


ask()
