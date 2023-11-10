def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper

@validate_args
def check(arg):
    return arg

print(check(100)) 
print(check(-1))
print(check(1, 2, 3))
print(check("Hi"))
print(check())