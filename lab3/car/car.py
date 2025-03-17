class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower
    
class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine  
    
    def info(self):
        return f"Car details : {self.brand} {self.model}, Engine details: {self.engine.fuel_type} , {self.engine.horsepower}"


engine = Engine("petrol", 200)
car = Car("Honda", "Civic", engine)

print(car.info())
