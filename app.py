from flask import Flask, redirect, request, render_template, make_response
from func import *

app = Flask('__main__')

@app.route('/')
def index():
    return render_template('index.html', quotes=quotes(), categs=categs(), auth=auth())

@app.route('/admin')
def admin():
    if auth():
        return render_template('admin.html', quotes=quotes(), categs=categs(), len=len, categ_name=categ_name)
    return 'You do not have admin permissions'

@app.route('/add-quote', methods=['POST'])
def addq():
    if auth():
        categ = request.form['categ']
        quote = request.form['quote']
        person = request.form['person']

        add_quote(categ, quote, person)
        return redirect('/admin')
    return redirect('/admin')

@app.route('/del-quote-<int:quote>')
def delq(quote):
    if auth():
        del_quote(quote)
        return redirect('/admin')
    return redirect('/admin')

@app.route('/add-categ', methods=['POST'])
def addc():
    if auth():
        name = request.form['name']

        add_categ(name)
        return redirect('/admin')
    return redirect('/admin')

@app.route('/signout')
def signout():
    resp = make_response(redirect('/'))
    resp.set_cookie('1bvui', '', expires=0)

    return resp

@app.route('/login')
def login():
    if not auth():
        return render_template('login.html')
    return redirect('/admin')

@app.route('/auth', methods=['POST'])
def login_auth():
    password = request.form['password']
    if is_correct(password):
        resp = make_response(redirect('/admin'))
        resp.set_cookie('1bvui', cipher(password))

        return resp
    return redirect('/admin')

@app.route('/change-pw', methods=['POST'])
def app_change_pw():
    if auth():
        new_pw = request.form['pw']

        change_pw(new_pw)
        resp = make_response(redirect('/admin'))
        resp.set_cookie('1bvui', cipher(new_pw))

        return resp

    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)