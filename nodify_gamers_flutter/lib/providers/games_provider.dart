import 'package:flutter/foundation.dart';
import '../models/game.dart';

/// Games state provider - manages game library operations
class GamesProvider extends ChangeNotifier {
  final List<Game> _games = [];
  bool _isLoading = false;
  String? _errorMessage;
  
  // Filter and sort state
  String _searchQuery = '';
  String _filterType = 'All Games';
  String _sortBy = 'Name';
  bool _isGridView = true;

  List<Game> get games => _games;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;
  String get searchQuery => _searchQuery;
  String get filterType => _filterType;
  String get sortBy => _sortBy;
  bool get isGridView => _isGridView;

  // Get filtered and sorted games
  List<Game> get filteredGames {
    var result = _games;

    // Apply search filter
    if (_searchQuery.isNotEmpty) {
      result = result
          .where((g) => g.name.toLowerCase().contains(_searchQuery.toLowerCase()))
          .toList();
    }

    // Apply type filter
    if (_filterType == 'Installed') {
      result = result.where((g) => g.status == 'Installed').toList();
    } else if (_filterType == 'Not Installed') {
      result = result.where((g) => g.status != 'Installed').toList();
    } else if (_filterType == 'Favorites') {
      result = result.where((g) => g.isFavorite).toList();
    }

    // Apply sorting
    if (_sortBy == 'Name') {
      result.sort((a, b) => a.name.compareTo(b.name));
    } else if (_sortBy == 'Last Played') {
      result.sort((a, b) {
        if (a.lastPlayed == null && b.lastPlayed == null) return 0;
        if (a.lastPlayed == null) return 1;
        if (b.lastPlayed == null) return -1;
        return b.lastPlayed!.compareTo(a.lastPlayed!);
      });
    } else if (_sortBy == 'Play Time') {
      result.sort((a, b) => b.playTime.compareTo(a.playTime));
    }

    return result;
  }

  // Statistics
  int get totalGames => _games.length;
  int get installedGames => _games.where((g) => g.status == 'Installed').length;
  int get favoriteGames => _games.where((g) => g.isFavorite).length;
  int get totalPlayTime => _games.fold(0, (sum, g) => sum + g.playTime);
  int get updatesAvailable => _games.where((g) => g.status == 'Updating').length;

  void setSearchQuery(String query) {
    _searchQuery = query;
    notifyListeners();
  }

  void setFilterType(String type) {
    _filterType = type;
    notifyListeners();
  }

  void setSortBy(String sortBy) {
    _sortBy = sortBy;
    notifyListeners();
  }

  void toggleViewMode() {
    _isGridView = !_isGridView;
    notifyListeners();
  }

  void setLoading(bool value) {
    _isLoading = value;
    notifyListeners();
  }

  void setError(String? error) {
    _errorMessage = error;
    notifyListeners();
  }

  void addGame(Game game) {
    _games.add(game);
    notifyListeners();
  }

  void updateGame(String id, Game updatedGame) {
    final index = _games.indexWhere((g) => g.id == id);
    if (index != -1) {
      _games[index] = updatedGame;
      notifyListeners();
    }
  }

  void removeGame(String id) {
    _games.removeWhere((g) => g.id == id);
    notifyListeners();
  }

  void installGame(String id, String path) {
    final index = _games.indexWhere((g) => g.id == id);
    if (index != -1) {
      final game = _games[index];
      _games[index] = game.copyWith(
        path: path,
        status: 'Installed',
        installDate: DateTime.now(),
      );
      notifyListeners();
    }
  }

  void uninstallGame(String id) {
    final index = _games.indexWhere((g) => g.id == id);
    if (index != -1) {
      final game = _games[index];
      _games[index] = game.copyWith(
        path: null,
        status: 'Not Installed',
      );
      notifyListeners();
    }
  }

  void launchGame(String id) {
    final index = _games.indexWhere((g) => g.id == id);
    if (index != -1) {
      final game = _games[index];
      _games[index] = game.copyWith(
        lastPlayed: DateTime.now(),
      );
      notifyListeners();
    }
  }

  void toggleFavorite(String id) {
    final index = _games.indexWhere((g) => g.id == id);
    if (index != -1) {
      final game = _games[index];
      _games[index] = game.copyWith(isFavorite: !game.isFavorite);
      notifyListeners();
    }
  }

  void updatePlayTime(String id, int minutes) {
    final index = _games.indexWhere((g) => g.id == id);
    if (index != -1) {
      final game = _games[index];
      _games[index] = game.copyWith(playTime: game.playTime + minutes);
      notifyListeners();
    }
  }

  Future<void> loadGames() async {
    setLoading(true);
    try {
      // Simulate loading games from database/API
      await Future.delayed(const Duration(seconds: 1));
      
      // Sample data (replace with actual data source)
      _games.clear();
      _games.addAll([
        Game(
          id: '1',
          name: 'Cyberpunk 2077',
          status: 'Installed',
          genre: 'RPG',
          playTime: 120,
          lastPlayed: DateTime.now().subtract(const Duration(hours: 2)),
          size: 70.5,
          rating: 4.5,
          isFavorite: true,
        ),
        Game(
          id: '2',
          name: 'Elden Ring',
          status: 'Installed',
          genre: 'Action RPG',
          playTime: 85,
          lastPlayed: DateTime.now().subtract(const Duration(hours: 5)),
          size: 60.0,
          rating: 5.0,
          isFavorite: true,
        ),
        Game(
          id: '3',
          name: 'The Witcher 3',
          status: 'Installed',
          genre: 'RPG',
          playTime: 240,
          size: 50.0,
          rating: 5.0,
        ),
        Game(
          id: '4',
          name: 'Red Dead Redemption 2',
          status: 'Not Installed',
          genre: 'Action Adventure',
          playTime: 60,
          size: 120.0,
          rating: 4.8,
        ),
        Game(
          id: '5',
          name: 'Steam Deck',
          status: 'Installed',
          genre: 'Platform',
          playTime: 30,
          size: 5.0,
        ),
      ]);
      
      setError(null);
    } catch (e) {
      setError(e.toString());
    } finally {
      setLoading(false);
    }
  }
}
