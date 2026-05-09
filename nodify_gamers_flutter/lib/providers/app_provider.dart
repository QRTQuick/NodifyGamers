import 'package:flutter/foundation.dart';

/// Main application state provider
class AppProvider extends ChangeNotifier {
  int _currentIndex = 0;
  bool _isLoading = false;
  String? _errorMessage;

  int get currentIndex => _currentIndex;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  void navigateTo(int index) {
    _currentIndex = index;
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

  Future<void> loadData() async {
    setLoading(true);
    try {
      // Simulate async data loading
      await Future.delayed(const Duration(seconds: 1));
      setError(null);
    } catch (e) {
      setError(e.toString());
    } finally {
      setLoading(false);
    }
  }
}
