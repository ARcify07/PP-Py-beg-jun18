class Bird:

	def __init__(self):
		print('new bird')

	def who(self):
		print('Parent bird')

	def swim(self):
		print('swimming')

class Penguin(Bird):

	def __init__(self):
		super().__init__()
		print('penguin')
	#def who(self):
	#	print('child Penguin')
	def run(self):
		print('run run')

pingu = Penguin()
pingu.who()
pingu.swim()
pingu.run()
 
print(isinstance('hello' , str))

#*******************************
class Dog:
    kind = 'canine'
    act = 'bite'   # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance

d = Dog('bruno')
e = Dog('mark')
print(d.kind, d.name, d.act)
print('*'*40)
print(e.kind, e.name)
print(Dog)

#*******************************
class Animal:
    name = 'himank'
        def __init__(self, x= 5, y='hello', *arg):
            self.x = x
                self.y = y
                print(arg)
        def party(self):
            print(self.x)
                print('party yay')

dog = Animal('hello', 'python' , 393, 32, 2.3)
animal_list=[]
for i in range(10):
    animal_list.append(Animal())

for i in animal_list:
    i.party()
dog.party()
print(dog.name, dog.x, dog.y)
animal.party(dog)
