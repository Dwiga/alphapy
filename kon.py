import sqlite3
import pymysql

def mylyt():
    con = sqlite3.connect("alpha.db")
    exe = con.cursor()
def oursql():
    db = pymysql.connect(host="localhost", user="root", passwd="itmatrix", db="matrix_db")
    exe = db.cursor()