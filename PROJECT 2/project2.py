# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Main program loop
def main():
    print("Welcome to the Temperature Converter!")
    print("You can convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    
    while True:
        print("\nChoose the conversion you want to perform:")
        print("1. Celsius to Fahrenheit and Kelvin")
        print("2. Fahrenheit to Celsius and Kelvin")
        print("3. Kelvin to Celsius and Fahrenheit")
        print("4. Exit")
        
        choice = input("Enter the number corresponding to your choice (1-4): ")
        
        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
                print(f"{celsius}°C is {celsius_to_kelvin(celsius):.2f}K")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
                print(f"{fahrenheit}°F is {fahrenheit_to_kelvin(fahrenheit):.2f}K")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "3":
            try:
                kelvin = float(input("Enter temperature in Kelvin: "))
                print(f"{kelvin}K is {kelvin_to_celsius(kelvin):.2f}°C")
                print(f"{kelvin}K is {kelvin_to_fahrenheit(kelvin):.2f}°F")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()





