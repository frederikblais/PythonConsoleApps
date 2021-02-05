# Define script's variables
prompt1 = 'Enter the value of a: '
prompt2 = 'Enter the value of b: '
sum_result = 'The sum of a and b is: '
dif_result = 'The difference of a and b is: '
prod_result = 'The product of a and b is: '
div_result = 'The division of a and b is: '
line = '--------------------------------'

# Prompt user to enter a temperature in Celsius
print(line)
a = float(input(prompt1))
b = float(input(prompt2))

# Calculate sum
sum = a + b

# Calculate dif
dif = a - b

# Calculate prod
prod = a * b

# Calculate div
div = a / b

# Print results
print('\n')
print(sum_result, sum)
print(dif_result, dif)
print(prod_result, prod)
print(div_result, div)
print(line)