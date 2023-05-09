def odd_sum(a, b):
    sum = 0
    i = a
    while (i <= b):
        if (i % 2 != 0):
            sum += i
        i += 1
    return sum

a = 4362
b = 8831
print(odd_sum(a, b))