from flask import Flask, jsonify, request
import pymysql
app = Flask(__name__)

menus = [
    {'id':1, 'name':'Espresso', 'price':4000},
    {'id':2, 'name':'Americano', 'price':3800},
    {'id':3, 'name':'Cafelatte', 'price':4100}
]

@app.route('/')
def hello_flask():
    return 'Hello world'

#GET /menus 자료를 가지고 온다.
@app.route('/menus')
def get_munus():
    return jsonify({'menus':menus}) # list자료형은 json으로 변경할 수 없으므로 딕셔너리를 선언해 jsonify

#POST /menus 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST']) #method는 list의 형태로 넣어준다.
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # "{"name": ..., "price": ...}"
    menus.sort(key = lambda x:x['id'])
    next_id = menus[-1]['id']
    new_menu = {
        'id':next_id+1,
        'name': request_data['name'],
        'price': request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menu/<id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json() # "{"name": ..., "price": ...}"
    for menu in menus:
        if menu['id'] == int(id):
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            return jsonify(menu)

@app.route('/menu/<id>', methods=['DELETE'])
def delete_menu(id):
    id = int(id)
    idx = -1
    for menu in menus:
        if menu['id'] == id:
            idx = menus.index(menu)
            break
    if idx != -1:
        return jsonify(menus.pop(idx))
    else:
        return jsonify("nothing matched")

if __name__ == '__main__':
    app.run()