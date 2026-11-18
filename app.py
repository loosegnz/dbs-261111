from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    q = request.form.get("q")
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    return render_template("main.html")

@app.route("/dbs", methods=["GET", "POST"])
def dbs():
    return render_template("dbs.html")

@app.route("/dbsPred", methods=["GET", "POST"])
def dbsPred():
    q = float(request.form.get("q"))
    model = pickle.load(open("DBS_SGD.pkl", "rb"))
    r = model.predict([[q]])[0]
    return render_template("dbsPred.html", r=round(r, 2))

if __name__ == "__main__":
    app.run()