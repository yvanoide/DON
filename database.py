import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="root",
            password="example",
            database="bdd_info"
        )
        self.cursor = self.db.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def insert_donation(self, nom, prenom, adresse, email, somme_promise, conditions):
        sql = "INSERT INTO donations (nom, prenom, adresse, email, somme_promise, conditions) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, adresse, email, somme_promise, conditions)
        self.cursor.execute(sql, values)
        self.db.commit()

    def get_donations(self):
        self.cursor.execute("SELECT * FROM donations")
        return self.cursor.fetchall()

    def get_total_recolte(self):
        self.cursor.execute("SELECT SUM(somme_promise) FROM donations")
        total_recolte = self.cursor.fetchone()[0]
        return total_recolte if total_recolte else 0

    def get_recent_donations(self, limit):
        
        self.cursor.execute("SELECT * FROM donations ORDER BY id DESC LIMIT %s", (limit,))
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.db.close()
