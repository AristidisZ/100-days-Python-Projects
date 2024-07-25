def find_short(s):
    x = s.split()
    min = len(x[0])
    # print("min",min)
    for i in x:
        print(len(i))
        if min > len(i):
            min = len(i)
    return min


print(find_short("bitcoin take over the world maybe who knows perhaps"))
