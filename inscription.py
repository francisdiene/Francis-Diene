import sqlite3

# Connexion à la base de données (crée un fichier inscription.db s'il n'existe pas)
conn = sqlite3.connect('inscription.db')
cursor = conn.cursor()

# Création de la table participants
cursor.execute('''CREATE TABLE IF NOT EXISTS participants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom_complet TEXT,
                    date_naissance TEXT,
                    email TEXT UNIQUE,
                    telephone TEXT
                )''')

# Exemple d'insertion de données
cursor.execute("INSERT INTO participants (nom_complet, date_naissance, email, telephone) VALUES (?, ?, ?, ?)",
               ('John Doe', '1990-05-15', 'john@example.com', '123456789'))

# Validation des changements et fermeture de la connexion
conn.commit()
conn.close()
