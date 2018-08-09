def custom_enumerate(lst, start=1):
    count = start
    for i in lst:
        yield (count, i)
        count += 1


lst = [1,2,3,4,5]
#custom enumerate()
for i in custom_enumerate(lst, 2):
    print(i)

#built in enumarate()
for i in enumarate(lst, 2):
    print(i)

