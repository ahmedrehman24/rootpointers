def add(*args):
    print(sum(args))

add(1, 2, 3)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(name="John", age=30)
