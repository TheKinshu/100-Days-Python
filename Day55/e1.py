def logging_decorator(function):
    def wrapper(*arg, **kwargs):
        print(f"You called {function.__name__}{arg}")
        result = function(arg[0],arg[1],arg[2])
        print(f"It returned: {result}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return (a * b *c)


a_function(1,2,3)

