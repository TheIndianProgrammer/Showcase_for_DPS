import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # this sets the route to this page
def home():
	return render_template("index.html")

@app.route("/results")
def results():
	conn = sqlite3.connect("Database\database.sqlite")

	database_raw = conn.execute('''SELECT * FROM twitch_data''').fetchall()
	database = []

	for character in database_raw[0]:
		database.append(character)

	Streamer_name = database[0]
	Streamer_link = database[1]
	IDE_name = database[2]
	IDE_link = database[3]

	return render_template("result.html", name = Streamer_name, link = Streamer_link, IDE = IDE_name, IDE_link_web = IDE_link)

"""conn = sqlite3.connect("Database\database.sqlite")
	database = conn.execute('''SELECT * FROM twitch_data''').fetchall()
	Streamer_name = database[1]
	Streamer_link = database[2]
	IDE_name = database[3]
	IDE_link = database[4]
	"""

def data_insert(Streamer_name,Streamer_link,IDE_name, IDE_link):
		#Variable assignment
		conn = sqlite3.connect("Database\database.sqlite")

		conn.execute('''INSERT INTO twitch_data(Streamer_name, Streamer_raw_link, IDE_name, IDE_raw_link) 
                VALUES("Gouthy", "https://www.youtube.com/watch?v=AryxxsifvjQ", "Gouthy Studio Code", "https://code.visualstudio.com/")''')
		conn.commit()
		conn.close()

app.run()	