## keyword arguments

def bird(name, type='Indian', action='chirp'):
    print('--- Hey this is ', name, 'I ' , action)
    print('-'*40)
    print('My type is' , type)

## valid calls
bird('sparrow')
bird('sparrow', 'american' , action = 'bark')
bird(type='Indian' , action='bark', name= 'crow')

##invalid calls
bird()                              #missing required arg
bird(type='indian', 'sparrow')      #keyword arg must follow positional arg
bird(name='crow' , name='sparrow')  #duplicate value
bird(fly = 4)                       #unknown keyword

## arbit number of args

def animal(name, *args, **keyargs):
    print('Hello my name is', name)
    print("let's see what I can do!!")
    print('-'*40)
    for arg in args:
        print(arg)
    print('*'*40)
    for keyarg in keyargs:
        print(keyarg)

animal('dog', 23 , 'fly' , 'jump')

## lambda expressions

x = lambda x: 2**x
x(5)

##use with map

y = list(map(lambda x:2**3, range(10)))

## use with filter

mylist = [1, 5, 54, 39, 102, 39, 22]
# filter all divisible by 5.
result = list(filter(lambda x: (x % 5 == 0), mylist))

## default values are evaluated only once

a = 'hello'
def f(arg=a):
    print(arg)
a = 'world'
f()
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
## default values 2

def f(a, L=[]):
    L.append(a)
    return L

## if you don't want your default param to be shared

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
