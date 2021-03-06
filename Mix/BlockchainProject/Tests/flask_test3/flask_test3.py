#flask_test2.py
import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn
	
def get_post(post_id):
	conn = get_db_connection()
	post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
	conn.close()
	if post is None:
		abort(404)
	return post

app = Flask(__name__)

@app.route("/")
def index():
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts').fetchall()
	conn.close()
	return render_template('index.html', posts=posts)
	
@app.route("/page")
def page():
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts').fetchall()
	conn.close()
	return render_template('page.html', posts=posts)
	
@app.route("/edu")
def edu():
	return render_template('education.html')

if __name__ == "__main__":
    app.run()
