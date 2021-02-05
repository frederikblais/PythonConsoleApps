import math

# Define the script's variables
prompt = 'Enter the radius of the circle: '
result = 'The area of the circle is: '
line = '--------------------------------'

# Prompt user to enter a radius
print(line)
rad = float(input(prompt))

# Calculate area -> area = PI * rad_sqr
area = math.pi * rad * rad

# Print result
print('\n')
print(result)
print(area)
print(line)