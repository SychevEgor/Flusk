from flask import Flask, render_template

app = Flask(__name__)

cats = [
    {"title": "Куртки", "func_name": 'jacket'},
    {"title": "Головные уборы", "func_name": 'hats'},
    {"title": "Обувь", "func_name": 'shoes'},
]


@app.route('/')
@app.route('/index/')
def index ():
    return render_template('index.html', category=cats)


@app.route('/info/')
def info ():
    return render_template('info.html')


@app.route('/contacts/')
def contacts ():
    return render_template('contacts.html')


@app.route('/jacket/')
def jacket ():
    return render_template('jacket.html')


@app.route('/shoes/')
def shoes ():
    return render_template('shoes.html')


@app.route('/hats/')
def hats ():
    return render_template('hats.html')


if __name__ == "__main__":
    app.run(debug=True)
