from flask import Flask

app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = "secret-ket"

from routes import *

if __name__ == '__main__':
    app.run(debug=True)