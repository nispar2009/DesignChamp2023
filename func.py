import pyodbc
from random import randint
from flask import request

conn = pyodbc.connect('Driver={SQL Server}; Server=NISANTH_PC\\SQLEXPRESS; Database=idealogic; Trusted_Connection=yes;')
cursor = conn.cursor()

class Quote:
    def __init__(self, _id, categ, quote, person):
        self.id = _id
        self.categ = categ
        self.quote = quote
        self.person = person

class Categ:
    def __init__(self, _id, name):
        self.id = _id
        self.name = name

def categ_name(categ):
    query = 'SELECT _name FROM categs WHERE id = ?'
    result = cursor.execute(query, (categ,))
    result = (list(result)[0])[0]\
    
    return result

def quotes():
    query = 'SELECT * FROM quotes'
    quotes = []

    for quote in list(cursor.execute(query)):
        quotes.append(Quote(*quote))
    
    return quotes

def categs():
    query = 'SELECT * FROM categs'
    db_categs = list(cursor.execute(query))
    ret_categs = []

    for categ in db_categs:
        ret_categs.append(Categ(*categ))

    return ret_categs

def add_quote(categ, quote, person):
    query = 'INSERT INTO quotes (categ, quote, person) VALUES (?, ?, ?)'
    # inject = (args)
    cursor.execute(query, categ, quote, person)

    conn.commit()

def add_categ(name):
    query = 'INSERT INTO categs (_name) VALUES (?)'
    cursor.execute(query, name)

    conn.commit()

def cipher(text):
    increment = randint(1, 9)
    ciphered = str(increment)

    for letter in text:
        ciphered += chr(ord(letter) + increment)

    return ciphered

def decipher(text):
    decrement = int(text[0])
    deciphered = ''

    for letter in text:
        deciphered += chr(ord(letter) - decrement)

    deciphered = deciphered[1:]

    return deciphered

def auth():
    try:
        query = 'SELECT _password FROM _admin'
        actual_pw = ((list(cursor.execute(query)))[0])[0]
        cookie_pw = request.cookies['1bvui']

        if decipher(actual_pw) == decipher(cookie_pw):
            return True

        return False
    
    except:
        return False

def change_pw(new_pw):
    query = 'UPDATE _admin SET _password = ?'
    cursor.execute(query, cipher(new_pw))
    conn.commit()

def del_quote(quote):
    query = 'DELETE quotes WHERE id = ?'
    cursor.execute(query, quote)
    conn.commit()

def is_correct(password):
    try:
        query = 'SELECT _password FROM _admin'
        actual_pw = ((list(cursor.execute(query)))[0])[0]

        if decipher(actual_pw) == password:
            return True

        return False
    
    except:
        return False
