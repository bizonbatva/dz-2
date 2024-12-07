class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')

    def play(self):
        print(f'{self.name} is playing.')

    def meow(self):
        print(f'{self.name} says "meau"')


my_cat = Cat(name='dog')


my_cat.eat()
my_cat.sleep()
my_cat.play()
my_cat.meow()
