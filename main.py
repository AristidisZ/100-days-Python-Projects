def remove_every_other(arr):
    result = []
    for i in range(len(arr)):
        print(i)
        if i % 2 == 0:
            result.append(arr[i])
            print(result)
    return result

remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])