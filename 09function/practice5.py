def print_args(*args):
    args_count = len(args)
    print('args_count:{}' .format(args_count))
    return args_count

result = print_args(1, 3, 5, 'a', [], [4])
print(result)
