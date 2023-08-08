import pyodbc
from random import choice

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

def add_categ(name):
    query = 'INSERT INTO categs (id, _name) VALUES (null, ?)'
    cursor.execute(query, name)

def gen_quote(categ=None):
    quote = choice(quotes(categ))
    return quote

