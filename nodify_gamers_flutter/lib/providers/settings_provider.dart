import 'package:flutter/foundation.dart';

/// Settings state provider - manages app settings
class SettingsProvider extends ChangeNotifier {
  // General Settings
  String _language = 'English';
  bool _launchOnStartup = false;
  bool _runInBackground = true;

  // Appearance Settings
  String _theme = 'Dark Mode';
  String _accentColor = 'Purple';
  bool _enableAnimations = true;

  // Download Settings
  String _downloadLocation = 'C:\\Games\\NodifyGamers';
  bool _autoUpdateGames = true;
  int _downloadSpeedLimit = 80;

  // Notification Settings
  bool _updateNotifications = true;
  bool _newsNotifications = false;
  bool _desktopNotifications = true;

  // Getters
  String get language => _language;
  bool get launchOnStartup => _launchOnStartup;
  bool get runInBackground => _runInBackground;
  String get theme => _theme;
  String get accentColor => _accentColor;
  bool get enableAnimations => _enableAnimations;
  String get downloadLocation => _downloadLocation;
  bool get autoUpdateGames => _autoUpdateGames;
  int get downloadSpeedLimit => _downloadSpeedLimit;
  bool get updateNotifications => _updateNotifications;
  bool get newsNotifications => _newsNotifications;
  bool get desktopNotifications => _desktopNotifications;

  // Setters
  void setLanguage(String value) {
    _language = value;
    notifyListeners();
  }

  void setLaunchOnStartup(bool value) {
    _launchOnStartup = value;
    notifyListeners();
  }

  void setRunInBackground(bool value) {
    _runInBackground = value;
    notifyListeners();
  }

  void setTheme(String value) {
    _theme = value;
    notifyListeners();
  }

  void setAccentColor(String value) {
    _accentColor = value;
    notifyListeners();
  }

  void setEnableAnimations(bool value) {
    _enableAnimations = value;
    notifyListeners();
  }

  void setDownloadLocation(String value) {
    _downloadLocation = value;
    notifyListeners();
  }

  void setAutoUpdateGames(bool value) {
    _autoUpdateGames = value;
    notifyListeners();
  }

  void setDownloadSpeedLimit(int value) {
    _downloadSpeedLimit = value;
    notifyListeners();
  }

  void setUpdateNotifications(bool value) {
    _updateNotifications = value;
    notifyListeners();
  }

  void setNewsNotifications(bool value) {
    _newsNotifications = value;
    notifyListeners();
  }

  void setDesktopNotifications(bool value) {
    _desktopNotifications = value;
    notifyListeners();
  }

  Map<String, dynamic> getAllSettings() {
    return {
      'language': _language,
      'launch_on_startup': _launchOnStartup,
      'run_in_background': _runInBackground,
      'theme': _theme,
      'accent_color': _accentColor,
      'enable_animations': _enableAnimations,
      'download_location': _downloadLocation,
      'auto_update_games': _autoUpdateGames,
      'download_speed_limit': _downloadSpeedLimit,
      'update_notifications': _updateNotifications,
      'news_notifications': _newsNotifications,
      'desktop_notifications': _desktopNotifications,
    };
  }

  void loadFromMap(Map<String, dynamic> settings) {
    if (settings.containsKey('language')) _language = settings['language'];
    if (settings.containsKey('launch_on_startup')) _launchOnStartup = settings['launch_on_startup'];
    if (settings.containsKey('run_in_background')) _runInBackground = settings['run_in_background'];
    if (settings.containsKey('theme')) _theme = settings['theme'];
    if (settings.containsKey('accent_color')) _accentColor = settings['accent_color'];
    if (settings.containsKey('enable_animations')) _enableAnimations = settings['enable_animations'];
    if (settings.containsKey('download_location')) _downloadLocation = settings['download_location'];
    if (settings.containsKey('auto_update_games')) _autoUpdateGames = settings['auto_update_games'];
    if (settings.containsKey('download_speed_limit')) _downloadSpeedLimit = settings['download_speed_limit'];
    if (settings.containsKey('update_notifications')) _updateNotifications = settings['update_notifications'];
    if (settings.containsKey('news_notifications')) _newsNotifications = settings['news_notifications'];
    if (settings.containsKey('desktop_notifications')) _desktopNotifications = settings['desktop_notifications'];
    
    notifyListeners();
  }
}
