print("Hello World!")
print("This is a simple Python script.")

#Data types
integer_var = 10
float_var = 20.5
string_var = "Hello"
boolean_var = True
list_var = [1, 2, 3, 4, 5]
dict_var = {"key1": "value1", "key2": "value2"}
tuple_var = (1, 2, 3)
set_var = {1, 2, 3, 4, 5} 
range_var = range(0, 10)
none_var = None
print(integer_var, float_var, string_var, boolean_var, list_var, dict_var, 
tuple_var, set_var, range_var, none_var)

isinstance(integer_var, float)
print(isinstance(integer_var, float))

#Strings
single_str_1 = 'inigma'
single_str_2 = "inigma"
multi_str_1 = '''inigma
              inigma'''
multi_str_2 = """inigma
              inigma""" 
msg_str_1 = "inigma's inigma"
quote_str_1 = 'inigma, "inigma"'

#Using \
msg_str_2 = 'inigma\'s inigma'
quote_str_2 = "inigma, \"inigma\""
print(single_str_1, single_str_2, multi_str_1, multi_str_2, msg_str_1, 
quote_str_1, msg_str_2, quote_str_2)

#in operator
print('m' in msg_str_1)
print('q' in msg_str_1)
print('1' in msg_str_1)

#length operator
print(len(msg_str_1))

#index operator
print(msg_str_1[3])
print(msg_str_1[7])
print(msg_str_1[0])

#negative index
print(msg_str_1[-1])
print(msg_str_1[-13])

#string are immutable
msg_str_1 = 'no inigma'
print(msg_str_1)

#string cannot be changed directly
#msg_str_1[3] = 'u'
#msg_str_1[3] = '7'

#string concatination
str_1 = 'maya'
str_2 = 'hi'
str_3 = 'maya'
str_com = str_1 + ' ' + str_2 + ' ' + str_3
print(str_com)

#str() function
str_4  = 6
print(str_com + ' ' + str(str_4))

