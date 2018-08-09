def square(start, stop):
    for i in range(start, stop):
        yield i * i 

for x in square(1, 10):
    print(x)