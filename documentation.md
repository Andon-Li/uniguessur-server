current files

app.py -
update_db.py
dl.py
clues.yml - data file now, will be replaced by database
requirements.txt

needed files

1. database file
2. uniguessur.db - autocreated when update_db.py is run
   gonna be added to .gitignore

3. images folder - 'idk if its needed but this folder will store all the clue images here\

images/
├── image1.png
├── image2.jpg
└── image3.jpg

4. ~~.gitignore ~~

5. config.py - configuration settings

- example

  # Flask settings

  SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

  # Database

  DATABASE_PATH = 'uniguessur.db'

  # Images

  IMAGE_DIR = 'images/'
  MAX_IMAGE_SIZE = 2000 # Max pixels per side

  # Game settings

  MAX_GUESSES = 5
  POINTS_PER_CORRECT = 100

  # CORS settings (if needed for frontend)

  CORS_ORIGINS = ['http://localhost:3000']

  -
