import csv
import datetime
import pizza
import decorator

myPizza = pizza.DominosPizza()

def main():
    print("main")
    print(myPizza.get_cost())
    print(myPizza.get_description())
    

main()