
choice = input("Choose conversion: (1) Celsius to Fahrenheit (2) Fahrenheit to Celsius: ")


temp = float(input("Enter the temperature: "))


if choice == "1":
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp}°F")
elif choice == "2":
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print("Invalid choice.")
