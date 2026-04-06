from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Stephen Enriquez in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://latencies_database_user:rDYr0nRGIeTKrQA1dnhEYyH35oiW2ME1@dpg-d79k70khg0os73e7ev00-a/latencies_database")
    conn.close()
    return "Database Connection Successful"



