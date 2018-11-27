beer_bottle_numbers = list(range(0,10))[::-1]
print(beer_bottle_numbers)
for beer_bottle_number in beer_bottle_numbers:
    if beer_bottle_number > 2:
        print('{number} bottles of beer on the wall {number} bottles of beer. Take one'
              ' and pass it around, {number_1} bottles of beer on the wall.'.format(number = beer_bottle_number, number_1 = beer_bottle_number-1))
    elif beer_bottle_number == 2:
        print('{number} bottles of beer on the wall {number} bottles of beer. Take one'
              ' and pass it around, {number_1} bottle of beer on the wall.'.format(number = beer_bottle_number, number_1 = beer_bottle_number-1))
    elif beer_bottle_number == 1:
        print('{number} bottle of beer on the wall {number} bottle of beer. Take one'
              ' and pass it around, no more bottles of beer on the wall. .'.format(number = beer_bottle_number))
    else:
        print('No more bottles of beer on the wall, no more bottles of beer.' 
              'Go to the store and buy some more, 99 bottles of beer on the wall.')