"""
Game Manager Module
Handles game installation, launching, and management
"""

import os
import subprocess
from typing import Dict, List, Optional
from datetime import datetime


class GameManager:
    """Manages game library operations with performance optimizations"""
    
    def __init__(self):
        self.games = {}
        self.running_games = {}
        
    def add_game(self, game_data: Dict) -> bool:
        """Add game to library"""
        game_id = game_data.get('id')
        if game_id:
            self.games[game_id] = {
                **game_data,
                'added_date': datetime.now(),
                'status': 'Not Installed'
            }
            return True
        return False
    
    def remove_game(self, game_id: str) -> bool:
        """Remove game from library"""
        if game_id in self.games:
            del self.games[game_id]
            return True
        return False
    
    def install_game(self, game_id: str, install_path: str) -> bool:
        """Install a game"""
        if game_id not in self.games:
            return False
        
        game = self.games[game_id]
        game['path'] = install_path
        game['status'] = 'Installed'
        game['install_date'] = datetime.now()
        
        return True
    
    def uninstall_game(self, game_id: str) -> bool:
        """Uninstall a game"""
        if game_id not in self.games:
            return False
        
        game = self.games[game_id]
        game['status'] = 'Not Installed'
        game['path'] = None
        
        return True
    
    def launch_game(self, game_id: str) -> bool:
        """Launch a game"""
        if game_id not in self.games:
            return False
        
        game = self.games[game_id]
        
        if game.get('status') != 'Installed':
            return False
        
        try:
            # Launch game executable
            process = subprocess.Popen(
                game['path'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            self.running_games[game_id] = {
                'process': process,
                'start_time': datetime.now()
            }
            
            # Update last played
            game['last_played'] = datetime.now()
            
            return True
            
        except Exception as e:
            print(f"Error launching game: {e}")
            return False
    
    def close_game(self, game_id: str) -> bool:
        """Close a running game"""
        if game_id not in self.running_games:
            return False
        
        game_session = self.running_games[game_id]
        process = game_session['process']
        
        # Calculate play time
        end_time = datetime.now()
        start_time = game_session['start_time']
        play_duration = (end_time - start_time).total_seconds() / 60  # minutes
        
        # Update total play time
        if game_id in self.games:
            current_play_time = self.games[game_id].get('play_time', 0)
            self.games[game_id]['play_time'] = current_play_time + play_duration
        
        # Terminate process
        process.terminate()
        del self.running_games[game_id]
        
        return True
    
    def get_game(self, game_id: str) -> Optional[Dict]:
        """Get game by ID"""
        return self.games.get(game_id)
    
    def get_all_games(self) -> List[Dict]:
        """Get all games"""
        return list(self.games.values())
    
    def get_installed_games(self) -> List[Dict]:
        """Get only installed games"""
        return [g for g in self.games.values() if g.get('status') == 'Installed']
    
    def search_games(self, query: str) -> List[Dict]:
        """Search games by name"""
        query = query.lower()
        return [
            g for g in self.games.values()
            if query in g.get('name', '').lower()
        ]
    
    def update_play_time(self, game_id: str, minutes: int):
        """Update play time for a game"""
        if game_id in self.games:
            current = self.games[game_id].get('play_time', 0)
            self.games[game_id]['play_time'] = current + minutes
    
    def set_favorite(self, game_id: str, is_favorite: bool):
        """Set game as favorite"""
        if game_id in self.games:
            self.games[game_id]['is_favorite'] = is_favorite
    
    def get_statistics(self) -> Dict:
        """Get library statistics"""
        total_games = len(self.games)
        installed = sum(1 for g in self.games.values() if g.get('status') == 'Installed')
        total_play_time = sum(g.get('play_time', 0) for g in self.games.values())
        favorites = sum(1 for g in self.games.values() if g.get('is_favorite', False))
        
        return {
            'total_games': total_games,
            'installed_games': installed,
            'total_play_time': total_play_time,
            'favorites': favorites
        }
