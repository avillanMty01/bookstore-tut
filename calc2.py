# a calculator in python

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return false
    else:
        return x/y

# now we moved the commit to edit branch
# and we reset the commit on main, plus we unstaged calc2.py
# with   git restore --staged calc2.py
