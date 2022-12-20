
a = [7, 9, 3, 5]
small = a[0]
#pos

for i in range(len(a)-1):
    if a[i] < small:
        a[i] = small
    print(a[i])

