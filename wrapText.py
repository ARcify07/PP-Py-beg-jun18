def wrap(string, max_width):
    mystring=''
    for i in range(len(string)):
        if i >= max_width and i % max_width == 0 and i!=0:
            mystring += '\n'
        mystring+=string[i]
    return mystring
