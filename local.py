print('Hello World')
print("Hello from inside a file!")


def hello():
    print('hello')


def pack(a, b, c):
    return ([a, b, c])


def eat_lunch(lis):
    if len(lis) == 0:
        print('lunch box empty')
    for i in range(len(lis)):
        if i == 0:
            print(f"First I eat {lis[0]}")
        else:
            print(f"Next I eat {lis[i]}")
