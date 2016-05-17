def get_name():
    import sys

    return_name = "World"
    if len(sys.argv) > 1:
        return_name = " ".join(sys.argv[1:])

    return return_name

def say_hello(name):
    print("Hello " + name + "!")

name = get_name()

say_hello(name)
