from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    nama = "kampung"
    huruf = list(nama)
    dictionary = {"nama_kucing": "oren"}
    return render_template('basic.html', nama=nama, huruf=huruf, dictionary=dictionary)


@app.route("/informasi")
def info():
    return "<h3>Info tentang si Menk</h3>"


@app.route("/kucing/<name>")
def menk(name):
    return f"<h3>Ini adalah halaman untuk {name} si kucing</h3>"


if __name__ == '__main__':
    app.run(debug=True)
