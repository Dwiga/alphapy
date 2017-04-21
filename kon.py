import sqlite3
import pymysql

con = sqlite3.connect("alpha.db")
exe = con.cursor()
    
db = pymysql.connect(host="localhost", user="root", passwd="itmatrix", db="movie")
kusi = db.cursor()