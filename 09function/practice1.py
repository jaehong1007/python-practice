def fruits(color):

    if color == 'red':
        return 'apple'
    elif color == 'yellow':
        return 'banana'
    elif color == 'green':
        return 'melon'
    else:
        return "I don't know"

result1 = fruits('red')
print(result1)

result2 = fruits('yellow')
print(result2)

result3 = fruits('green')
print(result3)

result4 = fruits('black')
print(result4)
