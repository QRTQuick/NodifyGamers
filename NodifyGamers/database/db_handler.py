"""
Database handler for NodifyGamers
Manages game library, user data, and settings with SQLite
"""

import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Optional


class DatabaseHandler:
    """SQLite database handler with connection pooling and optimized queries"""
    
    def __init__(self, db_path: str = "database/nodify.db"):
        self.db_path = db_path
        self.ensure_database_exists()
        
    def ensure_database_exists(self):
        """Create database and tables if they don't exist"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Games table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                path TEXT,
                size REAL,
                install_date TIMESTAMP,
                last_played TIMESTAMP,
                play_time INTEGER DEFAULT 0,
                status TEXT DEFAULT 'Not Installed',
                genre TEXT,
                rating REAL,
                cover_url TEXT,
                is_favorite BOOLEAN DEFAULT 0
            )
        """)
        
        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT,
                avatar_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Settings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Activity log table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS activity_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                game_id INTEGER,
                activity_type TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (game_id) REFERENCES games(id)
            )
        """)
        
        # Updates table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS updates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_id INTEGER,
                version TEXT,
                size REAL,
                release_date TIMESTAMP,
                downloaded BOOLEAN DEFAULT 0,
                installed BOOLEAN DEFAULT 0,
                FOREIGN KEY (game_id) REFERENCES games(id)
            )
        """)
        
        # Achievements table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS achievements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_id INTEGER,
                name TEXT,
                description TEXT,
                unlocked BOOLEAN DEFAULT 0,
                unlock_date TIMESTAMP,
                icon_url TEXT,
                FOREIGN KEY (game_id) REFERENCES games(id)
            )
        """)
        
        conn.commit()
        conn.close()
        
    def get_connection(self):
        """Get database connection with optimizations"""
        conn = sqlite3.connect(self.db_path, timeout=30)
        conn.row_factory = sqlite3.Row
        # Enable WAL mode for better performance
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA cache_size=10000")
        return conn
    
    # Game operations
    def add_game(self, game_data: Dict) -> int:
        """Add a new game to the library"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO games (name, path, size, install_date, status, genre, cover_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            game_data.get('name'),
            game_data.get('path'),
            game_data.get('size', 0),
            game_data.get('install_date', datetime.now()),
            game_data.get('status', 'Not Installed'),
            game_data.get('genre'),
            game_data.get('cover_url')
        ))
        
        game_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return game_id
    
    def get_all_games(self) -> List[Dict]:
        """Retrieve all games from database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM games ORDER BY name")
        rows = cursor.fetchall()
        
        games = [dict(row) for row in rows]
        conn.close()
        
        return games
    
    def update_game(self, game_id: int, updates: Dict):
        """Update game information"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values()) + [game_id]
        
        cursor.execute(f"""
            UPDATE games SET {set_clause}, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, values)
        
        conn.commit()
        conn.close()
    
    def delete_game(self, game_id: int):
        """Remove game from database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM games WHERE id = ?", (game_id,))
        
        conn.commit()
        conn.close()
    
    # User operations
    def get_user(self, username: str) -> Optional[Dict]:
        """Get user by username"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        
        conn.close()
        return dict(row) if row else None
    
    def create_user(self, username: str, email: str) -> int:
        """Create a new user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO users (username, email)
            VALUES (?, ?)
        """, (username, email))
        
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return user_id
    
    # Settings operations
    def get_setting(self, key: str) -> Optional[str]:
        """Get a setting value"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = cursor.fetchone()
        
        conn.close()
        return row['value'] if row else None
    
    def set_setting(self, key: str, value: str):
        """Set a setting value"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO settings (key, value, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
        """, (key, value))
        
        conn.commit()
        conn.close()
    
    # Activity logging
    def log_activity(self, user_id: int, game_id: int, activity_type: str):
        """Log user activity"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO activity_log (user_id, game_id, activity_type)
            VALUES (?, ?, ?)
        """, (user_id, game_id, activity_type))
        
        conn.commit()
        conn.close()
    
    def get_recent_activity(self, limit: int = 10) -> List[Dict]:
        """Get recent activity log"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT a.*, g.name as game_name
            FROM activity_log a
            JOIN games g ON a.game_id = g.id
            ORDER BY a.timestamp DESC
            LIMIT ?
        """, (limit,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    # Statistics
    def get_statistics(self) -> Dict:
        """Get library statistics"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        stats = {}
        
        # Total games
        cursor.execute("SELECT COUNT(*) as count FROM games")
        stats['total_games'] = cursor.fetchone()['count']
        
        # Installed games
        cursor.execute("SELECT COUNT(*) as count FROM games WHERE status = 'Installed'")
        stats['installed_games'] = cursor.fetchone()['count']
        
        # Total play time
        cursor.execute("SELECT SUM(play_time) as total FROM games")
        result = cursor.fetchone()
        stats['total_play_time'] = result['total'] or 0
        
        # Favorites
        cursor.execute("SELECT COUNT(*) as count FROM games WHERE is_favorite = 1")
        stats['favorites'] = cursor.fetchone()['count']
        
        conn.close()
        return stats
