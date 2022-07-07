from flask import Flask, redirect, render_template, request, url_for
from models import *
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods = ['POST', 'GET'] )

def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    return render_template('index.html', posts=get_posts())

if __name__ == '__main__':
    app.run(debug=True)