import csv
import datetime
import pizza
import decorator

Pizza = pizza.Pizza("name","desc",14)


f = open("menu.txt", "r")

#Kişisel verileri almaya ve tutarlılığını kontrole yarayan fonksiyon
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
        print("Kredi kartı numarası 16 haneli olmalı !!")

    while True:
        cCardPasw = input("Kredi Kart Şifresi: ")
        if len(cCardPasw) == 4:
            break
        print("Kredi kartı şifresi 4 haneli olmalı !!")
    
#Pizza ve sos seçimini kontrol eden fonksiyon
def pizzaInfo():
    while True:
        pizzaTab = int(input("Pizza Tabanı(1-4): "))
        if pizzaTab == 1:
            myPizza = pizza.ClassicPizza()
            break
        print("1'den 4'e kadar seçim yapabilirsiniz !!")

    while True:
        pizzaSos = int(input("Sos seçiminiz(11-16): "))
        if pizzaSos == (11 or 12 or 13 or 14 or 15 or 16):
            break
        print("11'den 16'ya kadar seçim yapabilirsiniz !!")

    return pizzaTab,pizzaSos

def main():
    print(f.read())
    #print(pizzaInfo())
    #getInfo()


main()