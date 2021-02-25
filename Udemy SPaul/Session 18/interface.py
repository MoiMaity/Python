from abc import ABC, abstractmethod
from typing import Union


class Bird:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name



class Flyable(ABC):
    @abstractmethod
    def start_flight(self):
        pass

    @abstractmethod
    def stop_flight(self):
        pass

class Eagle(Bird, Flyable):
    def __init__(self, name, master_name):
        super().__init__(name)
        self.master_name = master_name

    def get_master_name(self):
        return self.master_name

    def start_flight(self):
        print('Eagle: ', super().get_name(), 'started flight in its own way')

    def stop_flight(self):
        print('Eagle: ', super().get_name(),'stopped flight in its own way')


class Owl(Bird, Flyable):
    def __init__(self, name, night_vision_power):
        super().__init__(name)
        self.night_vision_power = night_vision_power

    def get_night_vision_power(self):
        return self.night_vision_power

    def start_flight(self):
        print('Owl: ', super().get_name(), 'started flight on low land')

    def stop_flight(self):
        print('Owl: ', super().get_name(), 'stopped flight on a tree')


class Kiwi(Bird):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power



class Airplane(Flyable):
    def __init__(self, make, fuel_capacity):
        self.make = make
        self.fuel_capacity = fuel_capacity

    def start_flight(self):
        print('Airplane: ', self.make, 'started flight.')

    def stop_flight(self):
        print('Airplane: ', self.make, 'stopped flight.')



class Game:
    def __init__(self):
        self.game_objects = [Kiwi('Sweetie', 10),Eagle('Super Falcon', 'Malik'),
                                Owl('Night Captain', 10), Eagle('Knight', 'Alice'), Airplane('Boeing', 1000)]

    def start_game(self):
        for b in self.game_objects:
            if isinstance(b, Flyable):
                b.start_flight()

    def stop_game(self):
        for b in self.game_objects:
            if isinstance(b, Flyable):
                b.stop_flight()



g = Game()
g.start_game()
g.stop_game()
