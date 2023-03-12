#Pizza üst sınıfı, bu sınıfın genel özelliklerini taşır. Özellikler alt sınıflara aktarılabilir.

class Pizza:
    def __init__(self,name,description,cost):
        self.name = name
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost



#Pizza alt sınıfları, üst sınıftan ortak özellikleri alır(inheritance) --> name,description,cost
class ClassicPizza(Pizza):
    def __init__(self):
        name = "Klasik Pizza"
        description = "Domates Sosu, Peynir, Sucuk, Zeytin"
        cost = 89.0
        super().__init__(name,description, cost)


class MargheritaPizza(Pizza):
    def __init__(self):
        name = "Margherita Pizza"
        description = "Domates Sosu, Mozarella Peyniri, Fesleğen"
        cost = 96.0
        super().__init__(name,description, cost)


class TurkishPizza(Pizza):
    def __init__(self):
        name = "Türk Pizzası"
        description = "Pastırma, Domates, Yeşil Biber, Soğan"
        cost = 118.0
        super().__init__(name,description, cost)


class DominosPizza(Pizza):
    def __init__(self):
        name = "Dominos Pizza"
        description = "Domates Sosu, Mozarella Peyniri, Salam, Mantar"
        cost = 112.0
        super().__init__(name,description, cost)
