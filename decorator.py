import pizza

Pizza = pizza.Pizza()
class Decorator(Pizza):
    def __init__(self,component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)
    

class Olive(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.cost = 5.0

    def get_description(self):
        return self.component.get_description() + ' ' + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost
