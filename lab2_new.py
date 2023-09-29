import random

class Animal:
    def __init__(self, weight, age, quality, isReproduced):
        self.weight = weight
        self.age = age
        self.quality = quality
        self.isReproduced = isReproduced

class Cow(Animal):
    def __init__(self, weight, age, quality, isReproduced):
        super().__init__(weight, age, quality, isReproduced)
    def produce(self):
        if self.age > 2 and self.quality > 0:
            return self.quality * 20
        else:
            return 0
    
class Chicken(Animal):
    def __init__(self, weight, age, quality, isReproduced):
        super().__init__(weight, age, quality, isReproduced)
    def produce(self):
        if self.age > 0.5 and self.quality > 0:
            if self.quality < 0.5:
                return 0
            else:
                return 1
        else:
            return 0

class Pig(Animal):
    def __init__(self, weight, age, quality, isReproduced):
        super().__init__(weight, age, quality, isReproduced)
    def produce(self):
        return 0


class Storage:
    def __init__(self, milk, eggs, meat):
        self.milk = milk
        self.eggs = eggs
        self.meat = meat


class Farm:
    def __init__(self, cows, chickens, pigs, money, storage):
        self.cows = cows
        self.chickens = chickens
        self.pigs = pigs
        self.money = money
        self.storage = storage

        self.soldEggs = 0
        self.soldMilk = 0
        self.soldMeat = 0
        self.boughtFeed = 0
    
    def collect_produce(self):
        milk = sum(cow.produce() for cow in self.cows)
        eggs = sum(chicken.produce() for chicken in self.chickens)
        self.storage.milk += milk
        self.storage.eggs += eggs
    
    def sell_produce(self):
        milk = self.storage.milk
        eggs = self.storage.eggs
        meat = self.storage.meat
        productPrice = milk * milkPrice + eggs * eggPrice + meat *  meatPrice
        self.money += productPrice
        self.soldEggs += eggs
        self.soldMilk += milk
        self.soldMeat += meat

        self.storage.milk = 0
        self.storage.eggs = 0
        self.storage.meat = 0

    
    def feed_animals(self):
        for animal in self.cows + self.chickens + self.pigs:
            if animal.quality < 1:
                countWeightFeed = animal.weight * 0.02
                countFeed = (1 - animal.quality) * countWeightFeed
                if self.money > countFeed * priceFeed:
                    self.boughtFeed += countFeed
                    self.money -= countFeed * priceFeed
                    animal.quality = 1
                    animal.weight += countFeed * 0.01

    def auto_progressing(self):
        for animal in self.cows + self.chickens + self.pigs:
            animal.quality -= 0.3
            animal.age += 1/365
        for cow in self.cows:
            if cow.weight < 1000:
                cow.weight += 0.5
        for chicken in self.chickens:
            if chicken.weight < 10:
                chicken.weight += 0.005
        for pig in self.pigs:
            if pig.weight < 150:
                pig.weight += 0.03
    
    def kill_animal(self):
        for cow in self.cows:
            if cow.age > 12 or cow.quality < -4:
                self.storage.meat += cow.weight * 0.6
                self.cows.remove(cow)
        for chicken in self.chickens:
            if chicken.age > 2 or chicken.quality < -4 or len(self.chickens) > 1000:
                self.storage.meat += chicken.weight * 0.6
                self.chickens.remove(chicken)
        for pig in self.pigs:
            if pig.age > 8 or pig.quality < -4:
                self.storage.meat += pig.weight * 0.6
                self.pigs.remove(pig)

    def reproduce_animal(self):
        for cow in self.cows:
            if cow.age > 3 and not cow.isReproduced:
                for i in range(random.randint(1, 2)):
                    self.cows.append(Cow(50, 0, 1, False))
                cow.isReproduced = True
        for chicken in self.chickens:
            if chicken.age > 2 and not chicken.isReproduced:
                for i in range(random.randint(3, 5)):
                    self.chickens.append(Chicken(0.3, 0, 1, False))
                chicken.isReproduced = True
        for pig in self.pigs:
            if pig.age > 3 and not pig.isReproduced:
                for i in range(random.randint(1, 2)):
                    self.pigs.append(Pig(20, 0, 1, False))
                pig.isReproduced = True

    def check_economics(self):
        print(f"Sold: {round(self.soldEggs, 2)} eggs, {round(self.soldMilk, 2)} liters of milk, {round(self.soldMeat, 2)} kg meat")
        print(f"Income: {round(self.soldEggs * eggPrice + self.soldMilk * milkPrice + self.soldMeat * meatPrice, 2)} $, Outcome: {round(self.boughtFeed * priceFeed, 2)} $")
        
        


# Ціни на товар
meatPrice = 2
priceFeed = 1
milkPrice = 0.7
eggPrice = 0.04

storage1 = Storage(0, 0, 0)

cows_list = [Cow(400, 5, 1, False)]
chickens_list = [Chicken(5, 1.5, 0.51, False)]
pigs_list = [Pig(100, 1.5, 0.5, False), Pig(100, 0, 0.5, False)]

farm1 = Farm(cows_list, chickens_list, pigs_list, 10000, storage1)


print('-----------------------------------------')
for i in range(10):
    
    for j in range(365):
        farm1.auto_progressing()
        farm1.feed_animals()
        farm1.collect_produce()
        farm1.sell_produce()
        farm1.reproduce_animal()

    farm1.kill_animal()

    print(f"Year {i + 1}")
    print(f"Budget: {round(farm1.money, 2)} $")
    print(f"On the farm: {len(farm1.cows)} cows, {len(farm1.chickens)} chickens and {len(farm1.pigs)} pigs.")
    farm1.check_economics()
    print('-----------------------------------------')