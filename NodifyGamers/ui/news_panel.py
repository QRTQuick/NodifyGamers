"""
Modern News & Updates Panel with categorized feeds
Enhanced UI/UX with rich content display
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, 
    QPushButton, QScrollArea, QGridLayout, QGraphicsDropShadowEffect,
    QTabWidget
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor


class NewsCard(QFrame):
    """News article card with image and content"""
    
    def __init__(self, news_data):
        super().__init__()
        self.setObjectName("newsCard")
        self.setFixedHeight(180)
        
        # Shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Image section
        image_label = QLabel()
        image_label.setObjectName("newsImage")
        image_label.setMinimumWidth(200)
        image_label.setText("📰")
        image_label.setFont(QFont("Segoe UI Emoji", 48))
        image_label.setStyleSheet("""
            #newsImage {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #6366f1, stop:1 #8b5cf6);
                border-radius: 0;
            }
        """)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        # Content section
        content_frame = QFrame()
        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(20, 15, 20, 15)
        content_layout.setSpacing(10)
        
        # Title
        title = QLabel(news_data.get('title', 'News Title'))
        title.setStyleSheet("color: #f9fafb; font-size: 18px; font-weight: bold;")
        title.setWordWrap(True)
        content_layout.addWidget(title)
        
        # Excerpt
        excerpt = QLabel(news_data.get('excerpt', 'News excerpt...'))
        excerpt.setStyleSheet("color: #9ca3af; font-size: 14px;")
        excerpt.setWordWrap(True)
        content_layout.addWidget(excerpt)
        
        # Meta info
        meta_layout = QHBoxLayout()
        meta_layout.setSpacing(15)
        
        date_label = QLabel(f"📅 {news_data.get('date', 'Today')}")
        date_label.setStyleSheet("color: #6b7280; font-size: 12px;")
        meta_layout.addWidget(date_label)
        
        category_label = QLabel(f"🏷️ {news_data.get('category', 'General')}")
        category_label.setStyleSheet("color: #6366f1; font-size: 12px;")
        meta_layout.addWidget(category_label)
        
        meta_layout.addStretch()
        content_layout.addLayout(meta_layout)
        
        layout.addWidget(content_frame)


class UpdateItem(QFrame):
    """Game update notification item"""
    
    def __init__(self, game_name, version, size, date):
        super().__init__()
        self.setObjectName("updateItem")
        self.setFixedHeight(90)
        
        # Shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(shadow)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(20)
        
        # Game icon
        icon = QLabel("⬇️")
        icon.setFont(QFont("Segoe UI Emoji", 32))
        layout.addWidget(icon)
        
        # Info
        info_layout = QVBoxLayout()
        info_layout.setSpacing(5)
        
        game_label = QLabel(game_name)
        game_label.setStyleSheet("color: #f9fafb; font-weight: bold; font-size: 16px;")
        info_layout.addWidget(game_label)
        
        details = f"Version {version} • {size} • {date}"
        details_label = QLabel(details)
        details_label.setStyleSheet("color: #9ca3af; font-size: 13px;")
        info_layout.addWidget(details_label)
        
        layout.addLayout(info_layout)
        layout.addStretch()
        
        # Update button
        update_btn = QPushButton("Update Now")
        update_btn.setObjectName("updateButton")
        update_btn.setFixedSize(120, 35)
        update_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(update_btn)


class NewsPanel(QWidget):
    """News and updates panel with tabs"""
    
    def __init__(self, parent=None):
        super().__init__()
        self.setObjectName("newsPanel")
        self.parent_window = parent
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup news panel UI"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)
        
        # Header
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Tab widget for different content types
        self.tabs = QTabWidget()
        self.tabs.setObjectName("newsTabs")
        self.tabs.addTab(self.create_news_tab(), "📰 Latest News")
        self.tabs.addTab(self.create_updates_tab(), "🔄 Game Updates")
        self.tabs.addTab(self.create_events_tab(), "🎉 Events")
        
        main_layout.addWidget(self.tabs)
        
    def create_header(self):
        """Create panel header"""
        header_frame = QFrame()
        header_frame.setObjectName("newsHeader")
        
        layout = QHBoxLayout(header_frame)
        layout.setContentsMargins(0, 0, 0, 15)
        
        title = QLabel("News & Updates")
        title.setStyleSheet("color: #f9fafb; font-size: 28px; font-weight: bold;")
        layout.addWidget(title)
        layout.addStretch()
        
        # Refresh button
        refresh_btn = QPushButton("⟳ Refresh")
        refresh_btn.setObjectName("refreshBtn")
        refresh_btn.setFixedWidth(100)
        refresh_btn.clicked.connect(self.refresh_content)
        layout.addWidget(refresh_btn)
        
        return header_frame
        
    def create_news_tab(self):
        """Create news feed tab"""
        news_widget = QWidget()
        layout = QVBoxLayout(news_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(15)
        
        # Sample news items
        news_items = [
            {
                "title": "Major Platform Update Released",
                "excerpt": "Discover the new features and improvements in our latest platform update including performance boosts and UI enhancements.",
                "date": "Today",
                "category": "Platform"
            },
            {
                "title": "Summer Sale Event Starting Soon",
                "excerpt": "Get ready for massive discounts on hundreds of games. The summer sale starts next week with deals up to 80% off.",
                "date": "Yesterday",
                "category": "Events"
            },
            {
                "title": "New Achievement System Launched",
                "excerpt": "Track your gaming accomplishments with our revamped achievement system featuring global leaderboards.",
                "date": "2 days ago",
                "category": "Features"
            }
        ]
        
        for news in news_items:
            card = NewsCard(news)
            content_layout.addWidget(card)
        
        content_layout.addStretch()
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        
        return news_widget
        
    def create_updates_tab(self):
        """Create game updates tab"""
        updates_widget = QWidget()
        layout = QVBoxLayout(updates_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(10)
        
        # Sample updates
        updates = [
            ("Cyberpunk 2077", "2.1", "45 GB", "Today"),
            ("Elden Ring", "1.10", "12 GB", "Yesterday"),
            ("The Witcher 3", "4.04", "8 GB", "3 days ago"),
            ("Red Dead Redemption 2", "1.28", "15 GB", "1 week ago")
        ]
        
        for game, version, size, date in updates:
            item = UpdateItem(game, version, size, date)
            content_layout.addWidget(item)
        
        content_layout.addStretch()
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        
        return updates_widget
        
    def create_events_tab(self):
        """Create events tab"""
        events_widget = QWidget()
        layout = QVBoxLayout(events_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Placeholder for events
        placeholder = QLabel("🎉 Upcoming Events\n\nNo events scheduled at the moment.\nCheck back soon for exciting gaming events!")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder.setStyleSheet("color: #9ca3af; font-size: 16px;")
        layout.addWidget(placeholder)
        
        return events_widget
        
    def load_news(self, news_data):
        """Load news articles"""
        # Implementation for dynamic news loading
        pass
        
    def refresh_content(self):
        """Refresh news and updates content"""
        print("Refreshing content...")
        # Add refresh logic here
