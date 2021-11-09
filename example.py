from custom import Automatic
from custom import set_attributes


class Vehicle(metaclass=Automatic):
    
    def __init__(self, **kwargs):

        props = {
            'private': {
                'fuel': str, 'doors': int, 'brand': str, 'model': str,
                'tires': int, 'tank_limit': int
            },
            'public': {'speed': int}
        }
        set_attributes(self, props, cls_name=self.__class_name__, **kwargs)
        self.__tank = .0

    def fill_tank(self, amount: float) -> int:
        """This function fill the tank with
           the specified amount of fuel.

        Args:
            amount (float): Amount of fuel in liters.

        Returns:
            int: Leftover fuel
        """
        if amount + self.__tank <= self.__tank_limit:
            self.__tank += amount
            return 0
        
        self.__tank = self.__tank_limit
        return amount - self.__tank_limit

    def get_fuel(self) -> float:
        return self.__tank
    
    def get_speed(self):
        print(self.__speed)

    def get_brand(self):
        return self.__brand

class Car(Vehicle):
    def __init__(self, **kwargs):
        props = {
            'private': {
                'color': str, 'owner': str, 'year': int, 'plate': str,
                'alarm': bool, 'armored': bool
            },
            'public': {}
        }
        set_attributes(self, props, **kwargs)
        super().__init__(**kwargs)

    def get_my_obj(self):
        return self.__myObject

    def get_class2(self):
        return self.__class__.__name__

car = Car(**{
    'fuel': 'gas', 'doors': 2, 'brand': 'BMW', 'model': 'M3',
    'speed': 330, 'tires': 4, 'tank_limit': 60, 'color': 'red', 
    'year': 2021, 'plate': '2FA22B', 'alarm': True, 'armored': False,
    'owner': 'Murilo'
})

print(car.get_fuel())
car.fill_tank(50)
print(car.get_fuel())

