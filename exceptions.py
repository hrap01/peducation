def f():
    #raise RuntimeError('not today')
    0/0

def g():
    try:
        f()
    except ZeroDivisionError as re:
        print(repr(re))
        print(f" {re} vyjímka: ojoj")

g()