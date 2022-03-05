from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# DB연결
db = pymysql.connect(host='localhost', user='root', password='921292', charset='utf8')

# cursor설정
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute('USE mysql;')

@app.route('/whoami', methods=['GET'])
def get_git_id():
    git = {'name': 'cyan9212'}
    return jsonify(git)

@app.route('/echo', methods=['GET'])
def echo_string():
    a=request.args.get('string')
    return jsonify(a)

@app.route('/weapon', methods=['GET'])
def get_weapon():
    sql = "SELECT * FROM WEAPON"
    cursor.execute(sql)
    values = cursor.fetchall()
    return jsonify(values)

@app.route('/weapon', methods=['POST'])
def create_weapon():
    request_data = request.get_json()

    # db에 존재하는 가장 높은 id를 추출
    sql1 = "SELECT MAX(id) from WEAPON"
    cursor.execute(sql1)
    value = cursor.fetchall()
    next_id = value[0]['MAX(id)']+1

    # 새로운 데이터를 db에 insert
    sql2 = "INSERT INTO WEAPON(id, name, stock) VALUES (%s, %s, %s)"
    data = (next_id, request_data['name'], request_data['stock'])
    cursor.execute(sql2, data)

    # db 변경사항을 commit
    db.commit()

    new_weapon = {'id': next_id, 'name': request_data['name'], 'stock': request_data['stock']}
    return jsonify(new_weapon)

@app.route('/weapon/<id>', methods=['DELETE'])
def delete_weapon(id):
    sql1 = "SELECT * FROM WEAPON WHERE id=%s"
    cursor.execute(sql1, id)
    value = cursor.fetchone()

    sql2 = "DELETE FROM WEAPON WHERE id=%s"
    cursor.execute(sql2, id)

    db.commit()

    return jsonify(value)

@app.route('/weapon/<id>', methods=['PUT'])
def update_weapon(id):
    request_data = request.get_json()

    sql1 = "UPDATE WEAPON SET name=%s, stock=%s WHERE id=%s"
    data = (request_data['name'], request_data['stock'], id)
    cursor.execute(sql1, data)

    sql2 = "SELECT * FROM WEAPON WHERE id=%s"
    cursor.execute(sql2, id)
    value = cursor.fetchall()

    db.commit()
    return jsonify(value)

if __name__ == '__main__':
    app.run()