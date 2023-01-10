import sqlite3
conn = sqlite3.connect("Database\database.sqlite")
database = conn.execute('''SELECT * FROM twitch_data''').fetchall()
query = database[0]

query_list = []
for character in query:
    query_list.append(character)

print(query_list[0])

"""
Link to IDE
        <script>
            var link1 = '{{IDE_link_web}}';
            document.write('<a href="' + link1 + '">IDE</a>');
"""