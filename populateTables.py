import mysql.connector as mysqlpy
import codecs
import json

def get_db_connection():
    user = 'root'
    password = 'example'
    host = 'localhost'
    port = '3308'
    database = 'CHU_caen'
    bdd = mysqlpy.connect(user=user, password=password, host=host, port=port, database=database)
    return bdd

def insertion_matériel():
    bdd = get_db_connection()
    inFile = codecs.open("brief_240123-API REST\data.json", "r", "utf8")
    data = json.load(inFile)
    cursor = bdd.cursor()
    for i in range(len(data['materiel'])):
        data_i = data['materiel'][i]
        for j in data_i:
            cursor.execute(
                f'''INSERT INTO matériel (nom_du_produit, dimensions, état)
                VALUES("{data_i[j][0]}", "{data_i[j][1]}", "{data_i[j][2]}");''')
            bdd.commit()
    cursor.close()
    bdd.close()

def insertion_employés():
    bdd = get_db_connection()
    inFile = codecs.open("brief_240123-API REST\data.json", "r", "utf8")
    data = json.load(inFile)
    cursor = bdd.cursor()
    for i in range(len(data['employé.e informatique'])):
        data_i = data['employé.e informatique'][i]
        for j in data_i:
            cursor.execute(
                f'''INSERT INTO employés (nom, prénom, âge, profession)
                VALUES("{data_i[j][0]}", "{data_i[j][1]}", "{int(data_i[j][2])}", "{data_i[j][3]}");''')
            bdd.commit()
    cursor.close()
    bdd.close()

insertion_matériel()
insertion_employés()