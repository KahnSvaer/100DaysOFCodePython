# default value arguments

def greeter(fname, lname=""):
    print(f"Welcome {fname} {lname}")

greeter("Kahn")


# *args
def adder(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

