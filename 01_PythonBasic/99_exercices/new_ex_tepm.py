
def celsius_fahrenheit(celsius):


    fahrenheit = (celsius * 9) / 5 + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
   celsius = (fahrenheit - 32) * 5/9 # sau /9/5
   return celsius

celsius = float(input("Grade de convertie : "))
x_fahrenheit = celsius_fahrenheit(celsius)
print(x_fahrenheit)
x_celsius = fahrenheit_celsius(x_fahrenheit)
print(x_celsius)


