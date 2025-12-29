# Uniguessur Server

A Flask-based backend server for the Uniguessur game - a geography guessing game where players identify locations from visual clues.

## Overview

Uniguessur challenges players to identify landmarks and locations from images. The server manages game sessions, serves random clues with images, tracks player guesses, and validates answers using fuzzy string matching.

## Features

- **Random Clue Generation**: Serves random location clues with images
- **Session Management**: Tracks player progress and prevents duplicate clues
- **Image Handling**: Base64-encoded images with automatic processing
- **SQLite Database**: Stores clues, subjects, landmarks, and guess history
- **Fuzzy Matching**: Uses Damerau-Levenshtein distance algorithm for answer validation
- **CORS Support**: Ready for frontend integration

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd uniguessur-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
python update_db.py
```

4. (Optional) Create a `config.py` file for custom settings:
```python
import os

# Flask settings
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

# Database
DATABASE_PATH = 'uniguessur.db'

# Images
IMAGE_DIR = 'images/'
MAX_IMAGE_SIZE = 2000  # Max pixels per side

# Game settings
MAX_GUESSES = 5
POINTS_PER_CORRECT = 100

# CORS settings (if needed for frontend)
CORS_ORIGINS = ['http://localhost:3000']
```

## Project Structure

```
uniguessur-server/
├── app.py              # Main Flask application
├── config.py           # Configuration settings (optional)
├── db_helpers.py       # Database query helpers
├── update_db.py        # Database setup and initialization
├── dl.py               # Damerau-Levenshtein string similarity
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not tracked)
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── uniguessur.db       # SQLite database (auto-created)
├── clues.yml           # Legacy data file (being phased out)
├── images/             # Clue images (local storage)
│   ├── image1.png
│   └── image2.jpg
└── documentation.md    # Development notes
```

## Database Schema

### Clues Table
- `id` (Primary Key, Auto-increment)
- `image` (Base64 encoded)
- `photo_credit` (Attribution)
- `latitude` (Location coordinate)
- `longitude` (Location coordinate)
- `subject_id` (Foreign Key)

### Subjects Table
- `clue_id` (Foreign Key)
- `x` (Coordinate)
- `y` (Coordinate)
- `official_name` (Landmark name)

### Landmarks Table
- `official_name` (Primary Key)
- `alternative_names` (CSV of aliases)

### Guess History Table
- `id` (Primary Key, Auto-increment)
- `clue_id` (Foreign Key)
- `longitude` (Player's guess)
- `latitude` (Player's guess)

## Usage

### Running the Server

Development mode:
```bash
python app.py
```

The server will start on `http://localhost:4000`

### API Endpoints

#### `GET /`
Health check endpoint.

**Response:**
```html
<p>Hello there!</p>
```

#### `GET /new_session`
Initialize a new game session.

**Response:**
```html
<p>Ready!</p>
```

**Side Effects:**
- Clears session results
- Resets image history

#### `GET /uniguessur/random_clue`
Get a random clue for the game.

**Response:**
```json
{
  "image": "data:image/jpeg;base64,...",
  "credit": "Photo by ...",
  "subject_x": 40.7128,
  "subject_y": -74.0060
}
```

**Behavior:**
- Returns a clue not previously seen in the session
- Tracks clue history to avoid duplicates
- Includes base64-encoded image

## Development

### Database Helpers

The `db_helpers.py` file provides utility functions for:
1. `get_random_clue()` - Fetch random clue from database
2. Get subjects for a clue ID
3. Get alternative names for landmarks
4. Check guess history
5. Save player guesses

### String Matching

The `dl.py` module implements the Damerau-Levenshtein distance algorithm for fuzzy string matching, allowing approximate matches for player answers (handles typos, alternative spellings, etc.).

**Limitations:**
- Maximum string length: 100 characters
- Alphabet size: 26 (default)

### Image Processing

Images should be:
- Stripped of metadata
- Center-cropped to max aspect ratio 2:1 or 1:2
- Scaled to max 2000px per side
- Stored in the `images/` directory

## Environment Variables

Create a `.env` file for sensitive configuration:
```
SECRET_KEY=your-secret-key-here
DATABASE_PATH=uniguessur.db
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Notes

- The `clues.yml` file is legacy and will be replaced by the database
- Images are stored locally and not pushed to Git
- Session secret key is generated at runtime for development
- Consider using cryptographically secure random for production

## Security Considerations

- Set a proper `SECRET_KEY` in production
- Consider replacing `random` with `secrets` module for security-sensitive operations
- Implement rate limiting for API endpoints
- Add input validation for user guesses
- Use environment variables for sensitive configuration

## License

[Add your license here]
