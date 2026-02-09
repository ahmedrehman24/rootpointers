def total_sum(*args):
    return sum(args)

def display(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)

print(total_sum(10, 20, 30))
display(name="Sam", role="Developer")
