from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def show_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    return render_template("index.html", students=data)

if __name__ == "__main__":
    app.run(debug=True)