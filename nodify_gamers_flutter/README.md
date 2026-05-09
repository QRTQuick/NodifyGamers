# NodifyGamers Flutter - Next-Gen Gaming Platform

A modern, cross-platform game launcher and management application built with Flutter. This is a complete rewrite of the original PyQt6 application with enhanced UI/UX and performance optimizations.

## 🎮 Features

### Dashboard
- Real-time statistics (Total Games, Playing Now, Updates Available, Achievements)
- Quick action buttons for common tasks
- Recent activity feed with game history
- Smooth animations and transitions

### Game Library
- Grid and List view modes
- Advanced search functionality
- Filter by status (All, Installed, Not Installed, Favorites)
- Sort by Name, Last Played, Install Date, or Play Time
- Beautiful game cards with hover effects
- Status indicators for each game

### News & Updates
- Latest news from the gaming world
- Game update notifications with download buttons
- Events tab for upcoming gaming events
- Refresh functionality

### Settings
- **General**: Language, startup options, background running
- **Appearance**: Theme selection, accent colors, animations toggle
- **Downloads**: Location settings, auto-update, speed limits
- **Notifications**: Update alerts, news, desktop notifications

## 🏗️ Architecture

### Project Structure
```
nodify_gamers_flutter/
├── lib/
│   ├── main.dart              # App entry point
│   ├── models/                # Data models
│   │   └── game.dart
│   ├── providers/             # State management
│   │   ├── app_provider.dart
│   │   ├── games_provider.dart
│   │   └── settings_provider.dart
│   ├── screens/               # Main screens
│   │   ├── main_screen.dart
│   │   ├── dashboard_screen.dart
│   │   ├── game_library_screen.dart
│   │   ├── news_screen.dart
│   │   └── settings_screen.dart
│   ├── utils/                 # Utilities
│   │   └── theme.dart
│   └── widgets/               # Reusable widgets
├── assets/                    # Images, fonts, etc.
└── test/                      # Unit tests
```

### State Management
- **Provider** pattern for state management
- Separate providers for different concerns:
  - `AppProvider`: Navigation and global app state
  - `GamesProvider`: Game library operations
  - `SettingsProvider`: User preferences

### Key Dependencies
- `provider`: State management
- `google_fonts`: Typography
- `flutter_animate`: Animations
- `sqflite`: Local database (ready for implementation)
- `shared_preferences`: Settings persistence
- `cached_network_image`: Image caching

## 🎨 Design System

### Color Palette
- **Background**: `#0F172A` (Deep navy)
- **Surface**: `#1E293B` (Card background)
- **Primary**: `#6366F1` (Indigo)
- **Secondary**: `#10B981` (Emerald green)
- **Accent**: `#F59E0B` (Amber)

### Typography
- Font Family: Inter (via Google Fonts)
- Consistent sizing and weights across all screens

### Components
- Custom stat cards with gradients
- Animated navigation sidebar
- Toggle switches for settings
- Dropdown selectors
- Hover effects on interactive elements

## 🚀 Getting Started

### Prerequisites
- Flutter SDK 3.5.0 or higher
- Dart SDK 3.5.0 or higher
- IDE (VS Code, Android Studio, etc.)

### Installation

1. **Clone the repository**
```bash
cd nodify_gamers_flutter
```

2. **Install dependencies**
```bash
flutter pub get
```

3. **Run the app**
```bash
flutter run
```

### Building for Production

#### Windows
```bash
flutter build windows
```

#### macOS
```bash
flutter build macos
```

#### Linux
```bash
flutter build linux
```

#### Web
```bash
flutter build web
```

## 📱 Supported Platforms

- ✅ Windows
- ✅ macOS
- ✅ Linux
- ✅ Web
- ✅ Android (future)
- ✅ iOS (future)

## 🔧 Future Enhancements

- [ ] SQLite database integration for persistent storage
- [ ] Steam/Epic Games integration
- [ ] Cloud save synchronization
- [ ] Achievement tracking system
- [ ] Social features (friends, chat)
- [ ] Mod manager
- [ ] Screenshot manager
- [ ] Performance monitoring
- [ ] Custom themes support
- [ ] Plugin system

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

RealRed Studios

---

**NodifyGamers** - Your ultimate gaming companion! 🎮
