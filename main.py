import csv
import datetime
import pizza
import decorator

myPizza = pizza.DominosPizza()

f = open("pizzaDelivery/menu.txt", "r")

def getInfo():
    nameSurname = input("Ad Soyad: ")

    while True:
        idNum = input("TC Kimlik Numarası: ")
        if len(idNum) == 11:
            break
        print("TC Kimlik numarası 11 haneli olmalı !!")

    while True:
        creditCard = input("Kredi Kart Numarası: ")
        if len(creditCard) == 16:
            break
        print("Kredi kartı numarası 11 haneli olmalı !!")

    while True:
        cCardPasw = input("Kredi Kart Şifresi: ")
        if len(cCardPasw) == 4:
            break
        print("Kredi kartı şifresi 4 haneli olmalı !!")
    

def main():
    print(f.read())
    pizzaTab = int(input("Pizza Tabanı(1-4): "))
    pizzaSos = int(input("Sos seçiminiz(11-16): "))
    getInfo()
    

main()