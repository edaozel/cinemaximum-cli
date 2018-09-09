#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

print("Salon listesi oluşturuluyor...\n")

anasayfa_response = requests.get("https://www.cinemaximum.com.tr/sinemalar")
anasayfa_soup = BeautifulSoup(anasayfa_response.text, "lxml")

dict = {}
for number,item in enumerate(anasayfa_soup.find_all("div", {"class": "inner"}), 1):
    dict[number] = (item.find("h4").find("a").text, "https://www.cinemaximum.com.tr/" + item.find("h4").find("a")["href"])
    print("" + str(number) + ") " + dict[number][0])

theater = int(input('\nSalon numarası giriniz: '))
print("\nSalon: " + dict[theater][0] + "\n")
print("\nBUGÜNÜN FİLMLERİ\n")
r = requests.get(dict[theater][1])

soup = BeautifulSoup(r.text, "lxml")

for movie in soup.find("div", {"class": "movie-details-select-showtime-wrap"})\
        .find_all("section", {"class" :"movie-details-select-showtime"}):
    if movie.find("p", {"class": "text"}).text != "":
        print("" + movie.find("h4", {"class": "title"}).text + "/" + movie.find("p", {"class": "text"}).text)
    else:
        print(movie.find("h4", {"class": "title"}).text)
    print(movie.find("span", {"class": "txt"}).text)
    for time in movie.find("ul").find_all("li"):
        if time.has_attr("class"):
            print("#" + time.find("a").text + "#", end=' ')
        else:
            print(time.find("a").text, end=' ')
    print('\n')
