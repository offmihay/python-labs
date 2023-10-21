class Car():
    def __init__(self, brand, model, year, color) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

class DB(Car):
    def __init__(self) -> None:
        self.data = []

    def add_car(self, car):
        self.data.append(car)

    def sync_header(self, path_name):
        with open(path_name, 'w') as f:
            f.write('brand, model, year, color\n')


    def sync(self, path_name):
        with open(path_name, 'a') as f:
            for car in self.data:
                f.write(f"{car.brand},{car.model},{car.year},{car.color}\n")

    def read_file(self, path_name):
        content = []
        with open(path_name, 'r') as f:
            line = f.readline()
            while line:
                content.append(line)
                line = f.readline()
            return content
    
    def update_elem(self, car, arg, info):
        for i in self.data:
            if car.brand == i.brand and car.model == i.model and car.year == i.year and car.color == i.color:
                setattr(i, arg, info)
                break

    def delete_elem(self, car):
        for i in self.data:
            if car.brand == i.brand and car.model == i.model and car.year == i.year and car.color == i.color:
                self.data.remove(i)

database = DB()
database.add_car(Car('Mercedes', 'AMG GT', '2016', 'black'))
database.add_car(Car('Honda', 'Civic', '2003', 'grey'))
database.add_car(Car('Nissan', 'Altima', '2017', 'red'))
database.add_car(Car('Skoda', 'Octavia', '2015', 'blue'))
database.add_car(Car('Mazda', 'CX-5', '2017', 'red'))



database.update_elem(Car('Honda', 'Civic', '2003', 'grey'), 'model', 'CLS')
database.update_elem(Car('Nissan', 'Altima', '2017', 'red'), 'year', '2009')

database.delete_elem(Car('Mazda', 'CX-5', '2017', 'red'))

database.sync_header('база_даних_автомобілів.csv')
database.sync('база_даних_автомобілів.csv')


print(database.read_file('база_даних_автомобілів.csv'))