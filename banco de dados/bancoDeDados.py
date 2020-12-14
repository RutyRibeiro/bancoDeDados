import mysql.connector
import csv
lista = []
config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}


with open('Lista_cha_de_cozinha_1.csv', encoding='utf-8', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        dicionario={}
        dicionario['nome']=row[0].strip()
        dicionario['quant']=row[1].strip()
        dicionario['img']=row[2].strip()
        lista.append(dicionario)
print(lista)

def insere():
    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida - INSERT")
    except mysql.connector.Error as err:
        print(err)
    else:
        cursor = conn.cursor()
        
        for row in lista:
            for i in range(int(row['quant'])):
                buscaDados ='insert into produtos(nome_produto, descricao_produto, img_produto) values (%s, %s, %s)'
                cursor.execute(buscaDados, (row['nome'], 'Utilizar cores neutras <br>Imagens meramente ilustrativas',row['img']))          
        cursor.close()
    
    conn.commit()
    conn.close()
    print("Fechamento do banco de dados: Com sucesso - INSERT")

insere()
