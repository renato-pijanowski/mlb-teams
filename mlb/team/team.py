class Team:

    def __init__(self, name, city):
        self.__name = name
        self.__city = city

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city