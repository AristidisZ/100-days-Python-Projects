def get_sum(a, b):
    numbers = []
    for i in range(a, b+1):
        numbers.append(i)
    print(numbers)
    return sum(numbers)


print(get_sum(-5, 10))
