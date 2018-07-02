## Scoping rules

def increment(n):
    n+=1
    print(n)
    return n

n = 1
increment(n)
print(n)

def increment(n):
    print(id(n))
    n+=1
    print(id(n))
    print(n)
    return n

n = 1
print(id(n))
increment(n)
print(n)

## tell functions as a variable first then this

def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z =', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()

## Next example

x = 10
def bar():
    print(x)

x = 10
def foo():
    print(x)
    x += 1

foo()
print(x)

*********************************
## usecase of non local

def foo():
    x = 10
    def bar():
        nonlocal x
        print(x)
        x += 1
    bar()
    print(x)
foo()

***********************************
## use case of global
age = 10
def f():
    age = 12
    def g():
     global age
     print(age)
     g()

***********************************
age = 10
def t():
    age = 15
    def h():
       nonlocal age
       print(age)
    age = 20
    def j():
        global age
     print(age)
    h()
    j()
