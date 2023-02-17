class Cat:
    name = ''
    age = ''
    color = ''

    # init method is called when you create a class
    def __init__(self, name):
        self.name = name
        print(f"Name of My Cat is {self.name}")

    def meow(self):
        print(f'{self.name}-Meow')
    
    def sleep(self):
        print(f'{self.name}-zzz')
        
    def hungry(self):
        for i in range(5):
            self.meow()

# it will print name of my cat is bulbul at the time of creating class
myCat = Cat(name="Bulbul")
myCat.hungry()
myCat.sleep()

x = [1,2,3]
type(x)

y = (i for i in x)
type(y)
    
