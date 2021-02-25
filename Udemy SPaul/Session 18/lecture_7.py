from abc import ABC, abstractmethod


class Bird(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def start_flight(self):
        pass

    @abstractmethod
    def stop_flight(self):
        pass

class Eagle(Bird):
    def __init__(self, name, master_name):
        super().__init__(name)
        self.master_name = master_name

    def get_master_name(self):
        return self.master_name

    def start_flight(self):
        print('Eagle: ', super().get_name(), 'started flight in its own way')

    def stop_flight(self):
        print('Eagle: ', super().get_name(),'stopped flight in its own way')

class Owl(Bird):
    def __init__(self, name, night_vision_power):
        super().__init__(name)
        self.night_vision_power = night_vision_power

    def get_night_vision_power(self):
        return self.night_vision_power

    def start_flight(self):
        print('Owl: ', super().get_name(), 'started flight on low land')

    def stop_flight(self):
        print('Owl: ', super().get_name(), 'stopped flight on a tree')


class Game:
    def __init__(self):
        self.bird_objects = [Eagle('Super Falcon', 'Malik'), Owl('Night Captain', 10), Eagle('Knight', 'Alice')]

    def start_game(self):
        for b in self.bird_objects:
            b.start_flight()

    def stop_game(self):
        for b in self.bird_objects:
            b.stop_flight()



g = Game()
g.start_game()
g.stop_game()
