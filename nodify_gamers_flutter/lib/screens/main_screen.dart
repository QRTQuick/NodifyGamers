import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/app_provider.dart';
import '../providers/games_provider.dart';
import 'dashboard_screen.dart';
import 'game_library_screen.dart';
import 'news_screen.dart';
import 'settings_screen.dart';

/// Main screen with navigation sidebar
class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  final List<String> _navItems = [
    'Dashboard',
    'Library',
    'News',
    'Settings',
  ];

  final List<Widget> _screens = const [
    DashboardScreen(),
    GameLibraryScreen(),
    NewsScreen(),
    SettingsScreen(),
  ];

  @override
  void initState() {
    super.initState();
    // Load initial data
    WidgetsBinding.instance.addPostFrameCallback((_) {
      context.read<GamesProvider>().loadGames();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          // Navigation Sidebar
          _buildSidebar(),
          // Content Area
          Expanded(
            child: Consumer<AppProvider>(
              builder: (context, appProvider, child) {
                return AnimatedSwitcher(
                  duration: const Duration(milliseconds: 300),
                  child: _screens[appProvider.currentIndex],
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSidebar() {
    return Container(
      width: 250,
      decoration: BoxDecoration(
        color: const Color(0xFF1E293B),
        border: Border(
          right: BorderSide(
            color: const Color(0xFF334155),
            width: 1,
          ),
        ),
      ),
      child: Column(
        children: [
          // Logo/Brand
          Padding(
            padding: const EdgeInsets.all(20.0),
            child: Container(
              width: double.infinity,
              height: 60,
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFF6366F1), Color(0xFF8B5CF6)],
                ),
                borderRadius: BorderRadius.circular(12),
              ),
              child: const Center(
                child: Text(
                  '🎮 NodifyGamers',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ),
          ),
          const SizedBox(height: 20),
          
          // Navigation Items
          ...List.generate(
            _navItems.length,
            (index) => _buildNavItem(index),
          ),
          
          const Spacer(),
          
          // Version info
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Text(
              'v1.0.0',
              style: TextStyle(
                color: Colors.grey[600],
                fontSize: 12,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildNavItem(int index) {
    return Consumer<AppProvider>(
      builder: (context, appProvider, child) {
        final isActive = appProvider.currentIndex == index;
        final icons = ['📊', '🎯', '📰', '⚙️'];
        
        return Padding(
          padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 5),
          child: GestureDetector(
            onTap: () => appProvider.navigateTo(index),
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 200),
              height: 50,
              decoration: BoxDecoration(
                gradient: isActive
                    ? const LinearGradient(
                        colors: [Color(0xFF6366F1), Color(0xFF8B5CF6)],
                      )
                    : null,
                color: isActive ? null : Colors.transparent,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Row(
                children: [
                  const SizedBox(width: 20),
                  Text(
                    icons[index],
                    style: const TextStyle(fontSize: 18),
                  ),
                  const SizedBox(width: 15),
                  Text(
                    _navItems[index],
                    style: TextStyle(
                      color: isActive ? Colors.white : Colors.grey[400],
                      fontSize: 15,
                      fontWeight: isActive ? FontWeight.w600 : FontWeight.normal,
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}
