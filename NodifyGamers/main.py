"""
NodifyGamers - Modern Game Launcher & Management Platform
Main entry point with enhanced UI/UX and performance optimizations
"""

import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon

# Import UI components
from ui.dashboard import DashboardPanel
from ui.game_library import GameLibraryPanel
from ui.news_panel import NewsPanel
from ui.settings_panel import SettingsPanel

# Import modules
from modules.game_manager import GameManager
from modules.update_manager import UpdateManager
from database.db_handler import DatabaseHandler
from utils.helpers import apply_modern_styles


class MainWindow(QMainWindow):
    """Main application window with modern navigation and layout"""
    
    def __init__(self):
        super().__init__()
        
        # Initialize core systems
        self.db = DatabaseHandler()
        self.game_manager = GameManager()
        self.update_manager = UpdateManager()
        
        # Setup UI
        self.setup_window()
        self.setup_navigation()
        self.setup_content_area()
        self.apply_modern_theme()
        
        # Load initial data asynchronously
        self.load_data_async()
        
    def setup_window(self):
        """Configure main window properties"""
        self.setWindowTitle("NodifyGamers - Next-Gen Gaming Platform")
        self.setMinimumSize(1280, 720)
        self.resize(1400, 900)
        
        # Enable modern window features
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowSystemMenuHint |
            Qt.WindowType.WindowMinMaxButtonsHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)
        
    def setup_navigation(self):
        """Create modern sidebar navigation"""
        from PyQt6.QtWidgets import QFrame, QPushButton, QHBoxLayout
        
        self.nav_frame = QFrame()
        self.nav_frame.setObjectName("navFrame")
        self.nav_frame.setFixedWidth(250)
        
        nav_layout = QVBoxLayout(self.nav_frame)
        nav_layout.setSpacing(10)
        nav_layout.setContentsMargins(15, 30, 15, 15)
        
        # Logo/Brand section
        brand_label = QPushButton("🎮 NodifyGamers")
        brand_label.setObjectName("brandButton")
        brand_label.setFixedHeight(60)
        brand_label.setCursor(Qt.CursorShape.PointingHandCursor)
        nav_layout.addWidget(brand_label)
        
        nav_layout.addSpacing(20)
        
        # Navigation buttons
        self.nav_buttons = {}
        nav_items = [
            ("dashboard", "📊 Dashboard"),
            ("library", "🎯 Game Library"),
            ("news", "📰 News & Updates"),
            ("settings", "⚙️ Settings")
        ]
        
        for nav_id, nav_text in nav_items:
            btn = QPushButton(nav_text)
            btn.setObjectName(f"navButton_{nav_id}")
            btn.setFixedHeight(50)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, nid=nav_id: self.navigate_to(nid))
            self.nav_buttons[nav_id] = btn
            nav_layout.addWidget(btn)
        
        nav_layout.addStretch()
        
    def setup_content_area(self):
        """Setup main content area with stacked widgets"""
        self.content_stack = QStackedWidget()
        self.content_stack.setObjectName("contentStack")
        
        # Initialize panels
        self.dashboard = DashboardPanel(self)
        self.library = GameLibraryPanel(self)
        self.news = NewsPanel(self)
        self.settings = SettingsPanel(self)
        
        self.content_stack.addWidget(self.dashboard)
        self.content_stack.addWidget(self.library)
        self.content_stack.addWidget(self.news)
        self.content_stack.addWidget(self.settings)
        
        # Main layout
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        main_layout.addWidget(self.nav_frame)
        main_layout.addWidget(self.content_stack)
        
        self.setCentralWidget(central_widget)
        
    def navigate_to(self, page_id):
        """Navigate to specified page with smooth transition"""
        page_map = {
            "dashboard": 0,
            "library": 1,
            "news": 2,
            "settings": 3
        }
        
        if page_id in page_map:
            # Update button states
            for btn_id, btn in self.nav_buttons.items():
                if btn_id == page_id:
                    btn.setProperty("active", True)
                else:
                    btn.setProperty("active", False)
                btn.style().unpolish(btn)
                btn.style().polish(btn)
            
            # Navigate with fade effect
            self.content_stack.setCurrentIndex(page_map[page_id])
            
    def apply_modern_theme(self):
        """Apply modern dark theme with smooth animations"""
        stylesheet = apply_modern_styles()
        self.setStyleSheet(stylesheet)
        
    def load_data_async(self):
        """Load data in background thread for better performance"""
        class DataLoader(QThread):
            data_loaded = pyqtSignal(dict)
            
            def run(self):
                # Simulate async data loading
                data = {
                    "games": [],
                    "news": [],
                    "updates": []
                }
                self.data_loaded.emit(data)
        
        self.loader = DataLoader()
        self.loader.data_loaded.connect(self.on_data_loaded)
        self.loader.start()
        
    def on_data_loaded(self, data):
        """Handle loaded data"""
        self.dashboard.update_stats(data)
        self.library.load_games(data.get("games", []))
        self.news.load_news(data.get("news", []))


def main():
    """Application entry point with performance optimizations"""
    # Enable high DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    app = QApplication(sys.argv)
    app.setApplicationName("NodifyGamers")
    app.setOrganizationName("RealRed Studios")
    
    # Set application-wide font
    font = QFont("Segoe UI", 10)
    font.setStyleHint(QFont.StyleHint.SansSerif)
    app.setFont(font)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Auto-check for updates on startup
    QTimer.singleShot(2000, lambda: window.update_manager.check_for_updates())
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
