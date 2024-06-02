from flask import Flask, request, jsonify

app = Flask(__name__)

# Пример данных, которые могут быть хранимы на сервере
students = [
    {"id": 1, "name": "Иванов Иван", "age": 20, "major": "Информатика"},
    {"id": 2, "name": "Петров Петр", "age": 21, "major": "Математика"},
    {"id": 3, "name": "Сидорова Анна", "age": 19, "major": "Физика"}
]

# Метод GET для получения списка всех студентов


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Метод GET для получения данных конкретного студента по его идентификатору


@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"message": "Студент с указанным идентификатором не найден"}), 404

# Метод POST для добавления нового студента


@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.json
    students.append(new_student)
    return jsonify({"message": "Студент успешно добавлен", "student": new_student}), 201

# Метод PUT для обновления данных студента


@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if student:
        data = request.json
        student.update(data)
        return jsonify({"message": "Данные студента успешно обновлены", "student": student})
    else:
        return jsonify({"message": "Студент с указанным идентификатором не найден"}), 404

# Метод DELETE для удаления студента по его идентификатору


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return jsonify({"message": "Студент успешно удален"})


if __name__ == '__main__':
    app.run(port=80, host="0.0.0.0", debug=False)