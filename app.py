from flask import Flask, redirect, request, render_template, make_response
from func import *

app = Flask('__main__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addquote', methods=['POST'])
def addq():
    if auth():
        categ = request.form['categ']
        quote = request.form['quote']
        person = request.form['person']

        add_quote(categ, quote, person)

    return redirect('/admin')

@app.route('/addcateg', methods=['POST'])
def addc():
    if auth():
        _id = request.form['id']
        name = request.form['name']

        add_categ(_id, name)

    return redirect('/admin')

@app.route('/signout')
def signout():
    resp = make_response(redirect('/admin'))
    resp.set_cookie('1bvui', '', expires=0)

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    if is_correct(password):
        resp = make_response(redirect('/admin'))
        resp.set_cookie('1bvui', cipher(password))

        return resp
    
    return redirect('/admin')

