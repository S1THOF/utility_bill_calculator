print("""
Welcome to Utility bill calculate!
For start need enter mode:
1. Electricity
2. Water
""")

global mode, water_now, water_after, price_water


def insert_mode():
    global mode
    mode = input("Enter need mode: ")
    while True:
        if mode == "1":
            return mode
        elif mode == "2":
            return mode
        else:
            mode = input("Enter 1 or 2: ")


def insert_indicators():
    global water_now, water_after, price_water
    if mode == "1":
        print("Good! Calculate electrically!")
        v = input("Enter amount of electricity used: ")
        price_kwt = input("Enter price for 1 KWt: ")
        print("You need pay:", float(v) * float(price_kwt))

    elif mode == "2":
        print("""Good! Calculate water!""")
        water_now = input("Enter the current counter value: ")
        water_after = input("Enter the value of the counter for the last month: ")
        price_water = input("Enter the current price for one cubic meter of water: ")
        print("You need pay:", (float(water_now) - float(water_after)) * float(price_water))


if __name__ == '__main__':
    insert_mode()
    insert_indicators()
