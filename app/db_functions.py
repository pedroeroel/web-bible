import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'RoelNotetaker'
DB_PASSWORD = 'notesaccess16as2'
DB_DATABASE = 'RoelTemplate'

class DB:
    def connect():
        cnt = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_DATABASE
        )
        cursor = cnt.cursor(dictionary=True)
        
        return cnt, cursor
    
    def stop(cnt, cursor):
        cursor.close()
        cnt.close()