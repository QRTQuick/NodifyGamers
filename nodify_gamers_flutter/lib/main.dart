/// NodifyGamers - Next-Gen Gaming Platform (Flutter Edition)
/// Main entry point with modern UI/UX and performance optimizations

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:google_fonts/google_fonts.dart';

import 'providers/app_provider.dart';
import 'providers/games_provider.dart';
import 'providers/settings_provider.dart';
import 'screens/main_screen.dart';
import 'utils/theme.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  
  runApp(const NodifyGamersApp());
}

class NodifyGamersApp extends StatelessWidget {
  const NodifyGamersApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AppProvider()),
        ChangeNotifierProvider(create: (_) => GamesProvider()),
        ChangeNotifierProvider(create: (_) => SettingsProvider()),
      ],
      child: MaterialApp(
        title: 'NodifyGamers',
        debugShowCheckedModeBanner: false,
        theme: AppTheme.darkTheme,
        home: const MainScreen(),
      ),
    );
  }
}
