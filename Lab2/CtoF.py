# Define script's variables
prompt = 'Enter the temperature in Celsius: '
line = '--------------------------------'
degree_sign= u"\u00b0"

# Prompt user to enter a temperature in Celsius
print(line)
cel = float(input(prompt))

# Make the temperature conversion
fah = (cel * 1.8) + 32

# Output result
print('\n')
print(cel,degree_sign,'C is equal to',fah, degree_sign , 'F')
print(line)