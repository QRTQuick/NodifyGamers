"""
Modern Dashboard Panel with statistics, quick actions, and activity feed
Enhanced UI/UX with smooth animations and responsive layout
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, 
    QPushButton, QScrollArea, QGridLayout, QGraphicsDropShadowEffect
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QFont, QColor


class StatCard(QFrame):
    """Modern statistic card with hover effects"""
    
    def __init__(self, title, value, icon, color="#6366f1"):
        super().__init__()
        self.setObjectName("statCard")
        self.setFixedHeight(140)
        self.setMinimumWidth(200)
        
        # Apply shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)
        
        # Layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(8)
        
        # Icon
        icon_label = QLabel(icon)
        icon_label.setFont(QFont("Segoe UI Emoji", 24))
        icon_label.setStyleSheet(f"color: {color};")
        layout.addWidget(icon_label)
        
        # Value
        value_label = QLabel(str(value))
        value_label.setObjectName("statValue")
        value_label.setStyleSheet(f"color: {color}; font-size: 32px; font-weight: bold;")
        layout.addWidget(value_label)
        
        # Title
        title_label = QLabel(title)
        title_label.setObjectName("statTitle")
        title_label.setStyleSheet("color: #9ca3af; font-size: 14px;")
        layout.addWidget(title_label)


class QuickActionBtn(QPushButton):
    """Modern quick action button with hover animation"""
    
    def __init__(self, icon, text, callback=None):
        super().__init__()
        self.setObjectName("quickActionBtn")
        self.setFixedSize(120, 120)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        if callback:
            self.clicked.connect(callback)
        
        # Layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 20, 10, 10)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Icon
        icon_label = QLabel(icon)
        icon_label.setFont(QFont("Segoe UI Emoji", 28))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icon_label)
        
        # Text
        text_label = QLabel(text)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setStyleSheet("color: #e5e7eb; font-size: 13px;")
        text_label.setWordWrap(True)
        layout.addWidget(text_label)


class ActivityItem(QFrame):
    """Activity feed item with modern styling"""
    
    def __init__(self, game_name, activity_type, time_ago):
        super().__init__()
        self.setObjectName("activityItem")
        self.setFixedHeight(70)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(15)
        
        # Game icon placeholder
        icon = QLabel("🎮")
        icon.setFont(QFont("Segoe UI Emoji", 20))
        layout.addWidget(icon)
        
        # Activity info
        info_layout = QVBoxLayout()
        info_layout.setSpacing(3)
        
        game_label = QLabel(game_name)
        game_label.setStyleSheet("color: #f9fafb; font-weight: 600; font-size: 14px;")
        info_layout.addWidget(game_label)
        
        activity_label = QLabel(f"{activity_type} • {time_ago}")
        activity_label.setStyleSheet("color: #9ca3af; font-size: 12px;")
        info_layout.addWidget(activity_label)
        
        layout.addLayout(info_layout)
        layout.addStretch()


class DashboardPanel(QWidget):
    """Main dashboard with stats, quick actions, and activity feed"""
    
    def __init__(self, parent=None):
        super().__init__()
        self.setObjectName("dashboardPanel")
        self.parent_window = parent
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup dashboard UI components"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(25)
        
        # Header
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Stats grid
        stats_section = self.create_stats_section()
        main_layout.addWidget(stats_section)
        
        # Content area (quick actions + activity)
        content_layout = QHBoxLayout()
        content_layout.setSpacing(25)
        
        # Quick actions
        quick_actions = self.create_quick_actions()
        content_layout.addWidget(quick_actions, 1)
        
        # Activity feed
        activity_feed = self.create_activity_feed()
        content_layout.addWidget(activity_feed, 2)
        
        main_layout.addLayout(content_layout)
        main_layout.addStretch()
        
    def create_header(self):
        """Create dashboard header with welcome message"""
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        
        layout = QHBoxLayout(header_frame)
        layout.setContentsMargins(0, 0, 0, 15)
        
        # Welcome text
        welcome_layout = QVBoxLayout()
        welcome_layout.setSpacing(5)
        
        title = QLabel("Welcome back, Gamer! 👋")
        title.setStyleSheet("color: #f9fafb; font-size: 28px; font-weight: bold;")
        welcome_layout.addWidget(title)
        
        subtitle = QLabel("Here's what's happening with your games")
        subtitle.setStyleSheet("color: #9ca3af; font-size: 14px;")
        welcome_layout.addWidget(subtitle)
        
        layout.addLayout(welcome_layout)
        layout.addStretch()
        
        return header_frame
        
    def create_stats_section(self):
        """Create statistics cards grid"""
        stats_frame = QFrame()
        stats_frame.setObjectName("statsFrame")
        
        layout = QGridLayout(stats_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        
        # Stat cards
        stats = [
            ("Total Games", "24", "🎯", "#6366f1"),
            ("Playing Now", "3", "🎮", "#10b981"),
            ("Updates Available", "5", "⬇️", "#f59e0b"),
            ("Achievements", "142", "🏆", "#ec4899")
        ]
        
        for i, (title, value, icon, color) in enumerate(stats):
            card = StatCard(title, value, icon, color)
            row = i // 2
            col = i % 2
            layout.addWidget(card, row, col)
        
        return stats_frame
        
    def create_quick_actions(self):
        """Create quick action buttons panel"""
        actions_frame = QFrame()
        actions_frame.setObjectName("actionsFrame")
        
        layout = QVBoxLayout(actions_frame)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Title
        title = QLabel("Quick Actions")
        title.setStyleSheet("color: #f9fafb; font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Buttons grid
        buttons_grid = QGridLayout()
        buttons_grid.setSpacing(15)
        
        actions = [
            ("➕", "Add Game", self.on_add_game),
            ("🔍", "Check Updates", self.on_check_updates),
            ("⚙️", "Settings", self.on_settings),
            ("❓", "Help", self.on_help)
        ]
        
        for i, (icon, text, callback) in enumerate(actions):
            btn = QuickActionBtn(icon, text, callback)
            row = i // 2
            col = i % 2
            buttons_grid.addWidget(btn, row, col)
        
        layout.addLayout(buttons_grid)
        layout.addStretch()
        
        return actions_frame
        
    def create_activity_feed(self):
        """Create recent activity feed"""
        activity_frame = QFrame()
        activity_frame.setObjectName("activityFrame")
        
        layout = QVBoxLayout(activity_frame)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Title
        title = QLabel("Recent Activity")
        title.setStyleSheet("color: #f9fafb; font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Scrollable activity list
        scroll = QScrollArea()
        scroll.setObjectName("activityScroll")
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(10)
        
        # Sample activities
        activities = [
            ("Cyberpunk 2077", "Played for 2h", "2 hours ago"),
            ("Elden Ring", "Achievement unlocked", "5 hours ago"),
            ("Steam Deck", "Game installed", "1 day ago"),
            ("The Witcher 3", "Update downloaded", "2 days ago"),
            ("Red Dead Redemption 2", "Played for 4h", "3 days ago")
        ]
        
        for game, activity, time in activities:
            item = ActivityItem(game, activity, time)
            content_layout.addWidget(item)
        
        content_layout.addStretch()
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        
        return activity_frame
    
    def update_stats(self, data):
        """Update statistics with loaded data"""
        # Implementation for dynamic stats update
        pass
        
    # Event handlers
    def on_add_game(self):
        """Handle add game action"""
        if self.parent_window:
            self.parent_window.navigate_to("library")
            
    def on_check_updates(self):
        """Handle check updates action"""
        print("Checking for updates...")
        
    def on_settings(self):
        """Handle settings action"""
        if self.parent_window:
            self.parent_window.navigate_to("settings")
            
    def on_help(self):
        """Handle help action"""
        print("Opening help documentation...")
