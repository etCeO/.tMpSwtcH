
# Ethan E. Lopez
# 002425516
# etlopez@chapman.edu
# CPSC 230 - Section 2
# Program Assignment 1

# input degrees celcius as a string
degrees_celcius = input('Please enter degrees Celcius: ')
# convert celcius string to float
c = float(degrees_celcius)

# calculate degrees fahrenheit using the standard formula
degrees_fahrenheit = (c * 9) / 5 + 32
# typecase fahrenheit to float for proper calculation
f = float(degrees_fahrenheit)

# print the result in the terminal
print(c, 'degrees celcius is', f, 'degrees farenheit.')
