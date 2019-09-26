from flask import Flask, request,jsonify
app=Flask(__name__)
import json
with open("C:/Users/Ranjitha/PycharmProject/rest_api_prj/student_data.py", "r") as fp:
    content = fp.read()
    d = content.split("\n")
    # print(d)
    res=[json.loads(i) for i in d]
    # print(res)

@app.route('/', methods=['GET'])
def get_student_info():
    return jsonify(res)

@app.route('/getstudentbyid/<int:id>', methods=['GET'])
def get_student_info_by_id(id):
    data = None
    for i in res:
        if i["id"] == id:
            data = i
    return jsonify(data)

@app.route('/deletebyid/<int:id>', methods=['DELETE'])
def delete_by_student_by_id(id):
    for i in res:
        if i["id"] == id:
            res.remove(i)
    return jsonify(res)

@app.route('/add_new_student', methods=['POST'])
def add_new_student():
    name = request.form.get("name")
    age = request.form.get("age")
    id = request.form.get("id")
    salary = request.form.get("salary")
    loc = request.form.get("loc")
    d = {"name": name, "age": age, "id": id, "salary": salary, "loc": loc}
    data = request.get_json(d)
    res.append(data)
    return jsonify(res)


if __name__ =='__main__':
    app.run()








