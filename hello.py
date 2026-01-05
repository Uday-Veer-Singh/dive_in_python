# Intergers and float numbers

int_num = 4
float_num = 2.0

add_num = int_num + float_num
print(add_num)

sub_num = int_num - float_num
print(sub_num)

multi_num = int_num * float_num
print(multi_num)

div_num = int_num / float_num
print(div_num)

# The modulo operator (%) returns the remainder when the value on the left is 
# divided by the value on the right:
modulus_num = int_num % float_num
print(modulus_num)

# Floor division divides two numbers and returns the greatest integer less 
# than or equal to the result. This is done with the double forward 
# slash operator (//):
floor_div_num = int_num // float_num
print(floor_div_num)

# Exponentiation raises a number to the power of another, and is done with 
# the double asterisk operator (**):
exponentiation_num = int_num ** float_num
print(exponentiation_num)

# The float() function returns a floating-point number constructed from the 
# given number:
float_func = float(int_num)
print(float_func)

# The int() function returns an integer constructed from the given number:
int_func = int(float_num)
print(int_func)

# We can also use these functions on strings
str_to_int = int('9')
print(str_to_int)
str_to_float = float('9.00')
print(str_to_float)

# round(): Rounds a number to the specified number of decimal places.
round_num = round(float_num)
print(round_num)

# abs(): returns the absolute value of a number
abs_num = abs(-9.8898)
print(abs_num)

# pow(): raises a number to the power of another or performs modular 
# exponentiation.
pow_num = pow(2, 2)
print(pow_num)
