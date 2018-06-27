# Python Program to find the factors of a number

# define a function
def print_factors(x):
    print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320
print_factors(num)

## length of a string
count = 0
mystring ='this is a very large string'  
for i in mystring:
    count +=1
print(count)

##second way
print(len(mystring))

## Number of chars and digits
for c in 'My strInG IS VERy good!!':
    if ord(c) >= 65 and ord(c) <= 90:
        upper_case+=1
   elif ord(c) > 97 and ord(c) <= 124:
       lower_case+=1
   else:
       print(c, 'unkown')

## second way to do it
text = input('Enter text!!\n')
character = 0
digit = 0
for c in text:
    if c.isalpha():
        character+=1
    if c.isdigit():
        digit+=1
print('Number of chars:', character, 'Number of digits:', digit)


## Number of occurrences of a char 
def mycount(s, c) :

    res = 0
    for i in range(len(s)) :
        if (s[i] == c):
            res = res + 1
    return res

mystring = "this is a testing string"
c = 's'
print(mycount(mystring, c))


## check if string is a pallindrome
pal = 'abbccbba'
for i in range(len(pal)):
    if pal[i] != pal[len(pal) -1 -i]:
        print('Not a pal')
        break
else:
    print('pal')


## Check if there are k consecutive 1's in binary numbers

def check(s,k):

    new = "1"*k

    if new in s:
        print "yes"
    else:
        print "no"

s = "10101001111"
k = 4
check(s, k)


## Reverse a string
def reverse(s):
    str = ""
  for i in s:
      str = i + str
  return str

## Reverse a string 2
string[::-1]

## cipher
cipher_text = ''
for c in 'your string':
    cipher_text+= chr(ord(c) + 4)

for c in cipher_text:
    original_text = chr(ord(c) -4)


## different number
t=0
for i in text.split():
    t=t^int(i)
print(t)

#num of words in a string
input_string = input('Enter a string.\n')
print(len(input_string.split()))
