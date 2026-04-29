import sqlite3

DATABASE_PATH = 'app.db'
IMAGE_PATH = './images'


def db_init():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS image (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            credit TEXT NOT NULL,
            lat REAL NOT NULL CHECK (lat >= -90 AND lat <= 90),
            long REAL NOT NULL CHECK (long >= -180 AND long <= 180)
        );
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS landmark (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            names TEXT NOT NULL,
            lat REAL NOT NULL CHECK (lat >= -90 AND lat <= 90),
            long REAL NOT NULL CHECK (long >= -180 AND long <= 180)
        );
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS image_landmark (
            image_id INTEGER NOT NULL REFERENCES image (id) ON DELETE CASCADE,
            landmark_id INTEGER NOT NULL REFERENCES landmark (id) ON DELETE CASCADE,
            PRIMARY KEY (image_id, landmark_id)
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_init()