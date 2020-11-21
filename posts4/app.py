import time
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts", methods=["POST"])
def posts():

    #para traer objetos en un POST siempre tengo que importar request
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    time.sleep(1)

    #cuando una route da como resultado un jsonify se entiende que es una API en la ruta /posts que devuelve las publicaciones y que puedo acceder a ella con un AJAX request
    return jsonify(data)
