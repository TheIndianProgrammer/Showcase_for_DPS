import sqlite3

conn = sqlite3.connect("Database\database.sqlite")

"""
#paste here
create table twitch_data (
	IDE_name varchar(1000),
	IDE_raw_link varchar(1000),
	);
	
INSERT INTO twitch_data
SELECT 'Visual Studio Code','https://code.visualstudio.com/';

GO
 
SELECT
IDE_name,
CAST(IDE_name AS XML) AS IDE_link 
FROM twitch_data;
GO

"""

conn.execute('''INSERT INTO twitch_data(Streamer_name, Streamer_raw_link, IDE_name, IDE_raw_link) 
                VALUES("Coding Hunt", "https://www.youtube.com/watch?v=AryxxsifvjQ", "Visual Studio Code", "https://code.visualstudio.com/")''')
conn.commit()
conn.close()

print("Table created successfully")
