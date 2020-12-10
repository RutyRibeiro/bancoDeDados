import csv

lista=[]
with open('escolas.csv', encoding='utf-8', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        dicionario={}
        dicionario["grupo"]="A1_GRPECON = '{}'".format(row[0].strip())
        dicionario["email"]=row[1].strip()

        lista.append(dicionario)
print(lista)

# with open('escolas.txt', "r") as textFile:
#     lines = textFile.readlines()
#     lines = list(map(lambda s: s.strip(), lines))
#     for row in lines:
#         k = row.split())