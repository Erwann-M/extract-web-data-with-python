import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')


# Fonction d'extraction des données
def extract_data(tag, class_name):
    datas = soup.find_all(tag, class_name)

    data_list = []

    for data in datas:
        data_list.append(data.string)

    return data_list


# stockage dans des listes
title_list = extract_data('a', 'gem-c-document-list__item-title')

description_list = extract_data('p', 'gem-c-document-list__item-description')

header_list = ["titre", "description"]

with open("data.csv", "w") as file_csv:
    writer = csv.writer(file_csv, delimiter=",")
    writer.writerow(header_list)
    for title, description in zip(title_list, description_list):
        row = [title, description]
        writer.writerow(row)


with open("data.csv") as read_file_csv:
    reader = csv.DictReader(read_file_csv, delimiter=",")
    print("voici les données récupéré :")
    for line in reader:
        print("\n" + line["titre"] + ":\n" + line["description"])
