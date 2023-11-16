from flask import Flask, render_template, request, url_for, redirect, jsonify
import random
import string

app = Flask(__name__, template_folder='frontend/templates',
            static_folder='frontend/static')

'''
Utilizamos como base de datos a un dict en el cual la key es el 'id' del estudiante
y el value es otro dict con datos del estudiante (incluido tambien el 'id'). Inicializamos el
dict con algunos estudiantes. Este dict 'students' podría ser persistido en un archivo json
si quisieramos que cada vez frenemos la app, al volver a correrla los datos se mantengan
'''
students = {
    "FsWfhScq": {
        "id": "FsWfhScq",
        "nombre": "Arturo",
        "apellido": "Chari",
        "edad": 34,
        "curso": "SISTOP"
    },
    "EvrGoNkf": {
        "id": "EvrGoNkf",
        "nombre": "Carlos",
        "apellido": "Perez",
        "edad": 24,
        "curso": "LABAPPS"
    }
}

# En lugar de un 'id' numerico utilizamos un 'id' string que se genera de forma automatica en esta funcion
def get_new_student_id():
    return ''.join(random.choices(string.ascii_letters, k=8))

# Esta funcion retorna el dict como una lista, para poder manejar los datos en el frontend de forma mas sencilla
def students_as_list():
    return [student for student in students.values()]

# Cuando se llama a la url del frontend 'http://localhost:5000' se muestra nuestro template 'index.html'
@app.route('/')
def index():
    return render_template('index.html', students=students_as_list())

# Endpoint para obtener todos los estudiantes como lista
@app.route('/estudiantes', methods=['GET'])
def get_students():
    return students_as_list()

# Endpoint para obtener un estudiante especifico por 'id'
@app.route('/estudiantes/<id>', methods=['GET'])
def get_student(id):
    if id not in students.keys():
        return jsonify({'error': 'Estudiante no encontrado'}), 404

    return jsonify(students[id]), 200

# Endpoint que recibe un body en formato "json" o "form" con el estudiante a agregar y lo agrega al dict 'students'
@app.route('/estudiantes', methods=['POST'])
def add_student():
    print(request.form)
    is_content_type_json = False
    # Consulto si el body es json. Si lo es, quiere decir que no se llamó a este endpoint desde el frontend (form)
    if request.headers['Content-Type'] == 'application/json':
        new_student = request.json
        is_content_type_json = True
    else:
        name = request.form.get('name')
        surname = request.form.get('surname')
        age = request.form.get('age')
        course = request.form.get('course')
        new_student = {
            "nombre": name,
            "apellido": surname,
            "edad": age,
            "curso": course
        }

    # Obtengo nuevo id autogenerado para el nuevo estudiante
    new_student_id = get_new_student_id()
    # Agrego ese id al usuario antes de agregarlo al dict 'students'
    new_student["id"] = new_student_id
    # Finalmente lo agrego al dict 'students' indicando que su key es su 'id'
    students[new_student_id] = new_student

    '''
    Si el body era json, retorno un json de respuesta con el nuevo estudiante creado.
    Si el body no era json, entonces recargo la pagina principal para que se vea en la lista el nuevo estudiante creado.
    '''
    if is_content_type_json:
        return jsonify(new_student), 201
    else:
        return render_template('index.html', students=students_as_list())

'''
Esta funcion agrupa los endpoints de nuestra api que siguen la url: '/estudiantes/<id>'
Esta agrupacion en una sola funcion se hizo debido a que a traves de un form html no se puede
utilizar los verbos PUT o DELETE. Hay que utilizar si o si el verbo POST para elimiar o modificar.
En una API RestFul esto no seria necesario, pero aqui consumimos el API tanto desde el frontend como
desde fuera (con Postman u otro cliente)
'''
@app.route('/estudiantes/<id>', methods=['PUT', 'DELETE', 'POST'])
def update_or_delete_student(id):
    if id not in students.keys():
        return jsonify({'error': 'Estudiante no encontrado'}), 404

    # Si llame a este endpoint con verbo DELETE, vine por API, elimino y retorno mensaje en un json
    if request.method == 'DELETE':
        students.pop(id)
        return jsonify({'mensaje': 'Estudiante eliminado'}), 200
    
    # Si llame a este endpoint con verbo PUT, vine por API, actualizo desde el json body y retorno el student actualizado en un json
    if request.method == 'PUT':
        updated_student = request.json
        updated_student["id"] = id
        students[id] = updated_student
        return jsonify(updated_student), 200
    
    '''
    Si estoy en este punto, quiere decir que se llego a este endpoint desde el frontend. Pudo haber entrado por el form de Eliminar
    o el form de Actualizar. Chequeo si el formulario no tiene inputs, entonces llegué aquí por el boton Eliminar, caso contrario llegué
    por el boton de Actualizar.
    '''
    if not len(request.form) == 0:
        name = request.form.get('name')
        surname = request.form.get('surname')
        age = request.form.get('age')
        course = request.form.get('course')
        updated_student = {
            "id": id,
            "nombre": name,
            "apellido": surname,
            "edad": age,
            "curso": course
        }

        students[id] = updated_student
    else:
        students.pop(id)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
