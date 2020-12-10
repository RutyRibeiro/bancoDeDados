import mysql.connector
import csv
lista = []
with open('escolas.csv', encoding='utf-8', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        dicionario={}
        dicionario["grupo"]="A1_GRPECON = '{}'".format(row[0].strip())
        dicionario["email"]=row[1].strip()

        lista.append(dicionario)
print(lista)


config = {
    'host': 'easyfenix.c6gbw6pywtzi.sa-east-1.rds.amazonaws.com',
    'user': 'datvs',
    'password': '124MudarMudar',
    'database': 'EasyBI'
}


def select():
    try:
        conn = mysql.connector.connect(**config)
        print("Acesso ao banco de dados: Conexão Estabelecida - INSERT")
    except mysql.connector.Error as err:
        print(err)
    else:
        cursor = conn.cursor()
        try:
            for i, row in enumerate(lista):
                
                buscaDados = """SELECT USR_VINCULO, USR_EMAIL FROM EasyBI.usuarios usr WHERE USR_CODCLI = 3284 AND USR_EMAIL= '%s'"""
                cursor.execute(buscaDados % (row['email']))
                resul = cursor.fetchall()
                
                if (row['grupo']!=resul[0][0]):
                    print (f'\033[33m olhe : {resul[0][1]}\033[m')
        except Exception as e:
            print(e)
        finally:           
            cursor.close()
    
            conn.commit()
            conn.close()
            print("Fechamento do banco de dados: Com sucesso - INSERT")
select()

