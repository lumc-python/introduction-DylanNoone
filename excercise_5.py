# 5. Dictionaries
#We are going to store the output of a function (f(x)=x2) together with its input in a dictionary.
#- Make a dictionary containing all squares smaller than 100.
#- Print the content of this dictionary in english, e.g., "4 is the square of 2".
numbers = list(range(0,101))
def f(x):
    return x**2
dictionary = {number: f(number) for number in numbers}
new_dictionary = dict()
for number in dictionary:
    if dictionary[number] < 100:
        new_dictionary[number] = dictionary[number]
for key in new_dictionary:
    print('{square} is the square of {number}'.format(square = new_dictionary[key], number = key))