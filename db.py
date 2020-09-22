import sqlite3

class FansDb:
    def __init__(self, db_name):
        self.name = db_name
        self.conn = None
        self.curs = None
        self.connect_db()

    def connect_db(self):
        self.conn = sqlite3.connect(self.name)
        self.curs = self.conn.cursor()

    def is_nickname_new(self, nickname):
        self.curs.execute("SELECT * FROM Fan WHERE nickname = ?", [nickname])
        rows = self.curs.fetchall()
        return len(rows)==0

    def add_fan_account(self, fan_nickname, fan_name):
        self.curs.execute("INSERT INTO Fan(name, nickname) VALUES ('"+fan_nickname+"','"+fan_name+"')")
        self.conn.commit()
        id_fan = self.curs.lastrowid
        return id_fan

    def add_artist(self, artist_name):
        self.curs.execute("INSERT INTO Artist(name) VALUES ('"+artist_name+"')")
        self.conn.commit()
        id_artist = self.curs.lastrowid
        return id_artist

    def add_genre(self, genre_label):
        self.curs.execute("INSERT INTO Genre(label) VALUES ('"+genre_label+"')")
        self.conn.commit()
        id_genre = self.curs.lastrowid
        return id_genre

    def add_artist_genre(self, artist_id, genre_id):
        self.curs.execute("INSERT INTO Artist_Genre(artist_id, genre_id) VALUES ("+artist_id+", "+genre_id+")")
        self.conn.commit()

    def add_artist_fan(self, artist_id, fan_id):
        self.curs.execute("INSERT INTO Artist_Fan(artist_id, fan_id) VALUES ("+artist_id+", "+fan_id+")")
        self.conn.commit()

    def genres(self):
        self.curs.execute("SELECT * FROM Genre")
        rows = self.curs.fetchall()
        list_genres = []
        for row in rows:
            (id,label) = row
            list_genres.append({'id':id,'label':label})
        return list_genres

    def artists(self):
        self.curs.execute("SELECT * FROM Artist")
        rows = self.curs.fetchall()
        list_artists = []
        for row in rows:
            (id,name) = row
            list_artists.append({'id':id,'name':name})
        return list_artists

    def fans(self):
        self.curs.execute("SELECT * FROM Fan")
        rows = self.curs.fetchall()
        list_fans = []
        for row in rows:
            (id,name,nickname) = row
            list_fans.append({'id':id,'name':name,'nickname':nickname})
        return list_fans

    def artist_fans(self, artist_id):
        self.curs.execute("SELECT id, name, nickname FROM Artist_Fan LEFT JOIN Fan ON fan_id=Fan.id WHERE artist_id=?", [artist_id])
        rows = self.curs.fetchall()
        list_fans = []
        for row in rows:
            (id,name,nickname) = row
            list_fans.append({'id':id,'name':name,'nickname':nickname})
        return list_fans

    def artists_fan_numbers(self):
        self.curs.execute("SELECT id, name, COUNT(fan_id) nb FROM Artist LEFT JOIN Artist_Fan ON artist_id=Artist.id GROUP BY id, name")
        rows = self.curs.fetchall()
        list_artists = []
        for row in rows:
            (id,name,nb) = row
            list_artists.append({'id':id,'name':name,'nb':nb})
        return list_artists


