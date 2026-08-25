# Let me import the functions from utuils.py
from utuils import square, is_even, celsius_to_faherenheit
number = int(input("Enter a number: "))
print(f"The square of {number} is {square(number)}")
print("Even" if is_even(number) else "Odd")
print(f"{number} degree Celsius is equal to {celsius_to_faherenheit(number)} degree Fahrenheit")