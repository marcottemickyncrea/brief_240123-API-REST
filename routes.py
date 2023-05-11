from flask import Flask, jsonify, request
import mysql.connector as mysqlpy

app = Flask(__name__)

def get_db_connection():
    user = 'root'
    password = 'example'
    host = 'localhost'
    port = '3308'
    database = 'CHU_caen'
    bdd = mysqlpy.connect(user=user, password=password, host=host, port=port, database=database)
    return bdd

@app.route('/materiel/<int:id>', methods=['GET'])
def get_materiel_id(id): 
    """Récupération des informations d'un seul object à partir de l'id"""
    if request.method == 'GET':  
        bdd = get_db_connection()
        cursor = bdd.cursor()
        cursor.execute(f'''SELECT id, nom_du_produit, dimensions, état FROM matériel WHERE id = {id};''')
        materiel = cursor.fetchone()
    

        materiel_json = [{'id': materiel[0], 'nom_du_produit':materiel[1], 'dimension': materiel[2], 'état': materiel[3]}]

        cursor.close()
        bdd.close()
        return jsonify(materiel_json)

@app.route('/materiel/', methods=['GET'])
def get_materiel():    
    """Récupération des informations de tous le matériel"""
    if request.method == 'GET':  
        bdd = get_db_connection()  
        cursor = bdd.cursor()
        cursor.execute(f'''SELECT id, nom_du_produit, dimensions, état FROM matériel;''')
        materiels = cursor.fetchall()
    
        music_list = []
        for materiel in materiels:
            music_list.append({'id': materiel[0], 'nom_du_produit':materiel[1], 'dimension': materiel[2], 'état': materiel[3]})

        cursor.close()
        bdd.close()
        return jsonify(music_list)

@app.route('/materiel/', methods=['POST'])
def post_materiel():
    """Insertion de nouveau matériel"""
    if request.method == 'POST':  
        bdd = get_db_connection()
        data= request.get_json()

        cursor = bdd.cursor()
        cursor.execute(
            f'''INSERT INTO matériel (nom_du_produit, dimensions, état)
            VALUES("{data['nom_du_produit']}", "{data['dimension']}", "{data['état']}");''')
        bdd.commit()
        cursor.close()
        bdd.close()  

        return jsonify({'message': 'Nouveau matériel ajouté !'})

@app.route('/materiel/', methods=['PUT'])
def put_materiel():
    "modification des dimensions d'un objet à partir de l'id"
    if request.method == 'PUT':
        bdd = get_db_connection()
        data= request.get_json()        

        cursor = bdd.cursor()
        cursor.execute(f'''UPDATE matériel SET dimensions = "{data['dimension']}" WHERE id = {data['id']};''')
        bdd.commit()
        cursor.close()
        bdd.close()

        return jsonify({'message': 'Modification réalisée !'})

@app.route('/materiel/', methods=['DELETE'])
def delete_materiel():
    '''suppression d'un matériel à partir de l'id'''
    if request.method == 'DELETE':
        bdd = get_db_connection()
        data= request.get_json()

        cursor = bdd.cursor()
        cursor.execute(f'''DELETE FROM matériel WHERE id = {data['id']};''')
        bdd.commit()
        cursor.close()
        bdd.close()

        return jsonify({'message': 'Suppression réalisée !'})

@app.route('/employés/<int:id>', methods=['GET'])
def get_employé_id(id): 
    '''récupération des informations d'un employé à partir de son id'''   
    if request.method == 'GET':  
        bdd = get_db_connection()
        cursor = bdd.cursor()
        cursor.execute(f'''SELECT id_employé, nom, prénom, âge, profession FROM employés WHERE id_employé = {id};''')
        employe = cursor.fetchone()
    

        employe_json = [{'id_employé': employe[0], 'nom':employe[1], 'prénom': employe[2], 'âge': employe[3], 'profession': employe[4]}]

        cursor.close()
        bdd.close()
        return jsonify(employe_json)

@app.route('/employés/', methods=['GET'])
def get_employé():    
    '''récupération de toutes les informations de tous les employés'''
    if request.method == 'GET':  
        bdd = get_db_connection()  
        cursor = bdd.cursor()
        cursor.execute(f'''SELECT id_employé, nom, prénom, âge, profession FROM employés;''')
        employes = cursor.fetchall()
    
        music_list = []
        for employe in employes:
            music_list.append({'id_employé': employe[0], 'nom':employe[1], 'prénom': employe[2], 'âge': employe[3], 'profession': employe[4]})

        cursor.close()
        bdd.close()
        return jsonify(music_list)

@app.route('/employés/', methods=['POST'])
def post_employé():
    '''insertion de nouveau employé'''
    if request.method == 'POST':  
        bdd = get_db_connection()
        data= request.get_json()

        cursor = bdd.cursor()
        cursor.execute(
            f'''INSERT INTO employés (nom, prénom, âge, profession)
            VALUES("{data['nom']}", "{data['prénom']}", "{data['âge']}", "{data['profession']}");''')
        bdd.commit()
        cursor.close()
        bdd.close()  

        return jsonify({'message': 'Nouvel(le) employé-e ajouté !'})

@app.route('/employés/', methods=['PUT'])
def put_employés():
    if request.method == 'PUT':
        '''modification de la profession d'un employé à partir de son id'''
        bdd = get_db_connection()
        data= request.get_json()        

        cursor = bdd.cursor()
        cursor.execute(f'''UPDATE employés SET profession = "{data['profession']}" WHERE id_employé = {data['id']};''')
        bdd.commit()
        cursor.close()
        bdd.close()

        return jsonify({'message': 'Modification réalisée !'})

@app.route('/employés/', methods=['DELETE'])
def delete_employé():
    '''suppression d'un employé à partir de son id'''
    if request.method == 'DELETE':
        bdd = get_db_connection()
        data= request.get_json()

        cursor = bdd.cursor()
        cursor.execute(f'''DELETE FROM employés WHERE id_employé = {data['id']};''')
        bdd.commit()
        cursor.close()
        bdd.close()

        return jsonify({'message': 'Suppression réalisée !'})

if __name__ == '__main__':
    app.run(debug=True)