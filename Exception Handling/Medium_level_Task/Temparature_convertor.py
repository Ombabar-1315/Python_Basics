def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


while True:

    try:
        print("======= Menu =======")
        print("1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")

        choice = int(input("Choose option: "))

        if choice == 1:
            cel = float(input("Enter Celsius: "))
            print("Fahrenheit:", celsius_to_fahrenheit(cel),"°F")
            break

        elif choice == 2:
            fer = float(input("Enter Fahrenheit: "))
            print("Celsius:", fahrenheit_to_celsius(fer),"°C")
            break

        else:
            print("❌ Enter a valid choice (1 or 2).")

    except ValueError:
        print("❌ Enter Valid Number.")