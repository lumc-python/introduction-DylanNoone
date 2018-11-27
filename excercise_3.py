#Excercise three
numbers = list(range(1,101))
for number in numbers:
    if number%3 == 0 and number%5 == 0:
        print("fizzbuzz")
    elif number%5 == 0:
        print("buzz")
    elif number%3 == 0:
        print("fizz")
    else:
        print(number)