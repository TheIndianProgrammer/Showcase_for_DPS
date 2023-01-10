import sqlite3
conn = sqlite3.connect("Database\database.sqlite")

conn.execute('''CREATE TABLE twitch_data(
                Streamer_name char(1000),
                Streamer_raw_link char(1000),
                IDE_name char(1000),
	            IDE_raw_link char(1000))
                ''')
"""
| Streamer Name | Streamer Link | IDE_Name | IDE_Link

"""
conn.close()
#smax dedo guys
#WidgetID int identity(1,1) not null