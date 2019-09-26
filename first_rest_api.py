from flask import Flask, jsonify, request, json
import requests

app = Flask(__name__)
student_data = [{"name": "surya", "age": 28, "id": 11234, "salary": 56000, "loc": "blr"},
               {"name": "suraj", "age": 25, "id": 12134, "salary": 34000, "loc": "kolkata"},
               {"name": "khirod", "age": 27, "id": 16753, "salary": 42000, "loc": "delhi"},
               {"name": "piyush", "age": 29, "id": 12345, "salary": 35000, "loc": "pune"}]


@app.route('/student_info', methods=['GET'])
def get_students_info():
    return jsonify(student_data)


@app.route('/getbyid/<int:id>', methods=['GET'])
def get_students_info_by_id(id):
    data=None
    for i in student_data:
        if i["id"] == id:
            data = i
    return jsonify(data)


@app.route('/deletebyname/<string:name>', methods=['DELETE'])
def delete_student_info_by_id(name):
    for i in student_data:
        if i["name"] == name:
            student_data.remove(i)
    return jsonify(student_data)

@app.route('/addstudent',methods=['POST'])
def add_new_student():
    name = request.form.get("name")
    age = request.form.get("age")
    id = request.form.get("id")
    salary = request.form.get("salary")
    loc = request.form.get("loc")
    d={"name": name, "age": age, "id": id, "salary": salary, "loc": loc}
    data=request.get_json(d)
    student_data.append(data)
    return jsonify(student_data)

if __name__ == '__main__':
    app.run()

