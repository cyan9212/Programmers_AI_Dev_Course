from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# 데이터베이스에 연결
db = pymysql.connect(host="localhost", user="root", password="921292", charset="utf8")

# cursor 설정
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute("USE mysql;")

@app.route('/')
def hello_flask():
    return 'Hello world'

#GET /menus 자료를 가지고 온다.
@app.route('/menus')
def get_munus():
    cursor.execute('SELECT * from CAFE_MENU')
    value = cursor.fetchall()
    return jsonify({'menus':value}) # list자료형은 json으로 변경할 수 없으므로 딕셔너리를 선언해 jsonify

#POST /menus 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST']) #method는 list의 형태로 넣어준다.
def create_menu(): # request가 JSON이라고 가정
    # request data 받아오기
    request_data = request.get_json() # "{"name": ..., "price": ...}"

    # select 구문을 실행
    cursor.execute('SELECT * FROM CAFE_MENU')
    value = cursor.fetchall()

    # 다음 id를 설정
    value.sort(key = lambda x:x['id'])
    next_id = value[-1]['id'] + 1

    # 데이터를 INSERT
    data = (next_id, request_data['name'], request_data['price'])
    sql = "INSERT INTO CAFE_MENU (id, name, price) VALUES (%s, %s, %s);"
    cursor.execute(sql, data)

    db.commit()

    new_menu = {
        'id':next_id,
        'name': request_data['name'],
        'price': request_data['price']
    }
    return jsonify(new_menu)

@app.route('/menu/<id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json() # "{"name": ..., "price": ...}"

    sql1  = 'SELECT name FROM CAFE_MENU WHERE id=%s'
    cursor.execute(sql1, id)
    value = cursor.fetchone()

    sql2 = 'UPDATE CAFE_MENU SET name=%s, price=%s WHERE id=%s'
    data = (request_data['name'], request_data['price'], id)
    cursor.execute(sql2, data)
    db.commit()
    return jsonify("update "+value['name']+" to "+request_data['name'])

@app.route('/menu/<id>', methods=['DELETE'])
def delete_menu(id):
    sql1 = 'SELECT name FROM CAFE_MENU WHERE id = %s'
    sql2 = 'DELETE FROM CAFE_MENU WHERE id = %s'

    cursor.execute(sql1, id)
    value = cursor.fetchone()

    cursor.execute(sql2, id)

    db.commit()

    if value: #제거할 데이터가 존재하는 경우
        return jsonify("delete "+value['name'])
    else: #제거할 데이터가 없는 경우
        return jsonify("nothing matched")

if __name__ == '__main__':
    app.run()