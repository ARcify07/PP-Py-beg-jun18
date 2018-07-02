""" This snippets explains error handling """
def divide(x,y):
    try:
        result = x/y
                #raise Exception('something bad happened')
    except ZeroDivisionError:
        print('division by zero not possible')
    except Exception as err:
        print(err, 'called custom exception')
    finally:
        print('final clause')

divide(2,2)
divide(2,0)

# use of else clause after try except
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

