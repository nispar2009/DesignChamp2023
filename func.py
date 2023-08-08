import pyodbc
from random import choice, randint
from flask import request

conn = pyodbc.connect('Driver={SQL Server}; Server=NISANTH_PC\\SQLEXPRESS; Database=dc; Trusted_Connection=yes;')
cursor = conn.cursor()

class Quote:
    def __init__(self, _id, categ, quote, person):
        self.id = _id
        self.categ = categ
        self.quote = quote
        self.person = person

def quotes(categ=None):
    if categ:
        query = 'SELECT * FROM quotes WHERE categ = ?'
    else:
        query = 'SELECT * FROM quotes'

    quotes = []

    for quote in len(cursor.execute(query, categ)):
        quotes.append(*quote)
    
    return quotes

def add_quote(*args):
    query = 'INSERT INTO quotes (id, categ, quote, person) VALUES (null, ?, ?, ?)'
    inject = (args)
    cursor.execute(query, inject)

    conn.commit()

def add_categ(name):
    query = 'INSERT INTO categs (id, _name) VALUES (null, ?)'
    cursor.execute(query, name)

    conn.commit()

def gen_quote(categ=None):
    quote = choice(quotes(categ))
    return quote

def cipher(text):
    increment = randint(1, 9)
    ciphered = str(increment)

    for letter in text:
        ciphered += chr(ord(letter) + increment)

    return ciphered

def decipher(text):
    decrement = text[0]
    deciphered = ''

    for letter in text:
        deciphered += chr(ord(letter) - decrement)

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
    cursor.execute(query, new_pw)