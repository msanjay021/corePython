from flask import Flask, jsonify

app = Flask(__name__)

todoItems = [
    {"id": 1, "content": "go through flask documentation"},
    {"id": 2, "content": "drink hot water"},
    {"id": 3, "content": "write a flask application"}
]

@app.route('/todo/', methods = ['GET'])
def getTodoList():
    return jsonify(todoItems)

@app.route('/todo/<int:key>', methods = ['GET'])
def getTodoListID(key):
    for items in todoItems:
        if items['id'] == key:
            return jsonify(items['content']) 
    else:
        return ("Task not found", 404)

@app.route('/todo/<int:key>/<string:val>', methods = ['POST'])
def createTodoList(key, val):
    for items in todoItems:
        if items['id'] == key:
            return ("Task already exists", 400)
    todoItems.append({"id": key, "content": val})
    return jsonify(todoItems), 201 

@app.route('/todo/<int:key>/<string:val>', methods = ['PUT'])
def updateTodoList(key, val):
    for item in todoItems:
        if item['id'] == key:
            item['content'] = val
            return jsonify(item), 200
    return "Task not found", 404     

@app.route('/todo/<int:key>', methods = ['DELETE'])
def deleteTodoList(key):
    for items in todoItems:
        if items['id'] == key:
            todoItems.remove(items)
            return '', 204
    return "Task not found", 404

if __name__ =='__main__':
    app.run()
