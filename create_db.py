import sqlite3

conn = sqlite3.connect('link_clicks.db')

cursor = conn.cursor()

create_table_query = '''CREATE TABLE IF NOT EXISTS Link (
                        id INTEGER PRIMARY KEY,
                        url TEXT NOT NULL,
                        prof_clicks INTEGER DEFAULT 0,
                        wimi_clicks INTEGER DEFAULT 0,
                        stud_clicks INTEGER DEFAULT 0
                    );'''

cursor.execute(create_table_query)
conn.commit()
conn.close()

print("Die Datenbank link_clicks.db wurde erfolgreich erstellt.")
