def square_or_multi(value1, value2=None):
    if value2 is None:
        return(value1 * value1)
    else:
        return(value1 * value2)

result1 = square_or_multi(7)
print(result1)

result2 = square_or_multi(5, 7)
print(result2)
