import sqlite3

class Database:
    def __init__(self):
        # Connect to SQLite database (will create a new one if it doesn't exist)
        self.conn = sqlite3.connect('game_data.db')
        self.cursor = self.conn.cursor()
        
        # Create table for players if it doesn't already exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                wins INTEGER DEFAULT 0,
                losses INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_player(self, name, age):
        """Add a new player to the database."""
        # Check if the player already exists based on the name
        self.cursor.execute("SELECT * FROM players WHERE name = ?", (name,))
        result = self.cursor.fetchone()

        if result:
            # If player exists, update their info (optional)
            print(f"Player {name} already exists.")
        else:
            # Insert new player into the database
            self.cursor.execute("INSERT INTO players (name, age) VALUES (?, ?)", (name, age))
            self.conn.commit()
            print(f"Player {name} added to the database.")

    def update_stats(self, name, wins, losses):
        """Update the player's wins and losses."""
        self.cursor.execute("UPDATE players SET wins = ?, losses = ? WHERE name = ?", (wins, losses, name))
        self.conn.commit()

    def get_player_stats(self, name):
        """Retrieve a player's stats based on their name."""
        self.cursor.execute("SELECT name, age, wins, losses FROM players WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        if result:
            return {
                "name": result[0],
                "age": result[1],
                "wins": result[2],
                "losses": result[3]
            }
        else:
            return None

    def close(self):
        """Close the database connection."""
        self.conn.close()
