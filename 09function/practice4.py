def return_tuple(value1, value2):
    return(value1+value2, value1-value2 if value1>value2 else value2-value1)

print(return_tuple(3,5))
