"""
Modern Game Library Panel with grid/list views, search, and filtering
Enhanced UI/UX with smooth animations and responsive design
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, 
    QPushButton, QScrollArea, QGridLayout, QLineEdit, 
    QComboBox, QStackedWidget, QGraphicsDropShadowEffect
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QSize
from PyQt6.QtGui import QFont, QColor, QIcon


class GameCard(QFrame):
    """Modern game card with hover effects and actions"""
    
    def __init__(self, game_data, on_launch=None, on_manage=None):
        super().__init__()
        self.game_data = game_data
        self.setObjectName("gameCard")
        self.setFixedSize(200, 280)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Apply shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.setGraphicsEffect(shadow)
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Cover image placeholder
        self.cover_label = QLabel()
        self.cover_label.setObjectName("gameCover")
        self.cover_label.setMinimumHeight(200)
        self.cover_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover_label.setText(f"🎮\n{game_data.get('name', 'Game')}")
        self.cover_label.setStyleSheet("""
            #gameCover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #374151, stop:1 #1f2937);
                color: #e5e7eb;
                font-size: 40px;
                border-radius: 8px;
            }
        """)
        layout.addWidget(self.cover_label)
        
        # Info section
        info_frame = QFrame()
        info_frame.setObjectName("gameInfo")
        info_layout = QVBoxLayout(info_frame)
        info_layout.setContentsMargins(12, 10, 12, 10)
        info_layout.setSpacing(5)
        
        # Game name
        name_label = QLabel(game_data.get('name', 'Unknown Game'))
        name_label.setStyleSheet("color: #f9fafb; font-weight: bold; font-size: 14px;")
        name_label.setWordWrap(True)
        info_layout.addWidget(name_label)
        
        # Status
        status = game_data.get('status', 'Not Installed')
        status_color = "#10b981" if status == "Installed" else "#6b7280"
        status_label = QLabel(f"● {status}")
        status_label.setStyleSheet(f"color: {status_color}; font-size: 12px;")
        info_layout.addWidget(status_label)
        
        layout.addWidget(info_frame)
        
        self.on_launch = on_launch
        self.on_manage = on_manage
        
    def enterEvent(self, event):
        """Hover effect on mouse enter"""
        self.setStyleSheet("""
            #gameCard {
                background-color: #374151;
                border-radius: 8px;
            }
        """)
        
    def leaveEvent(self, event):
        """Remove hover effect on mouse leave"""
        self.setStyleSheet("""
            #gameCard {
                background-color: transparent;
                border-radius: 8px;
            }
        """)


class GameListItem(QFrame):
    """List view item for games"""
    
    def __init__(self, game_data):
        super().__init__()
        self.setObjectName("gameListItem")
        self.setFixedHeight(80)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(15)
        
        # Cover thumbnail
        cover = QLabel("🎮")
        cover.setFont(QFont("Segoe UI Emoji", 30))
        cover.setFixedSize(60, 60)
        cover.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #374151, stop:1 #1f2937);
            border-radius: 8px;
        """)
        cover.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(cover)
        
        # Game info
        info_layout = QVBoxLayout()
        info_layout.setSpacing(5)
        
        name_label = QLabel(game_data.get('name', 'Unknown Game'))
        name_label.setStyleSheet("color: #f9fafb; font-weight: bold; font-size: 15px;")
        info_layout.addWidget(name_label)
        
        details = f"{game_data.get('genre', 'N/A')} • {game_data.get('last_played', 'Never')}"
        details_label = QLabel(details)
        details_label.setStyleSheet("color: #9ca3af; font-size: 13px;")
        info_layout.addWidget(details_label)
        
        layout.addLayout(info_layout)
        layout.addStretch()
        
        # Play button
        play_btn = QPushButton("▶ Play")
        play_btn.setObjectName("playButton")
        play_btn.setFixedSize(100, 35)
        play_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(play_btn)


class GameLibraryPanel(QWidget):
    """Game library with grid/list views, search, and filters"""
    
    def __init__(self, parent=None):
        super().__init__()
        self.setObjectName("gameLibraryPanel")
        self.parent_window = parent
        self.games = []
        self.view_mode = "grid"  # grid or list
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup library UI components"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)
        
        # Header with search and filters
        header = self.create_header()
        main_layout.addWidget(header)
        
        # View toggle and sort
        toolbar = self.create_toolbar()
        main_layout.addWidget(toolbar)
        
        # Games container with stacked views
        self.views_stack = QStackedWidget()
        
        # Grid view
        grid_widget = self.create_grid_view()
        self.views_stack.addWidget(grid_widget)
        
        # List view
        list_widget = self.create_list_view()
        self.views_stack.addWidget(list_widget)
        
        main_layout.addWidget(self.views_stack)
        
    def create_header(self):
        """Create header with search"""
        header_frame = QFrame()
        header_frame.setObjectName("libraryHeader")
        
        layout = QHBoxLayout(header_frame)
        layout.setContentsMargins(0, 0, 0, 15)
        
        # Title
        title = QLabel("My Game Library")
        title.setStyleSheet("color: #f9fafb; font-size: 28px; font-weight: bold;")
        layout.addWidget(title)
        layout.addStretch()
        
        # Search box
        self.search_input = QLineEdit()
        self.search_input.setObjectName("searchBox")
        self.search_input.setPlaceholderText("🔍 Search games...")
        self.search_input.setFixedWidth(300)
        self.search_input.textChanged.connect(self.filter_games)
        layout.addWidget(self.search_input)
        
        return header_frame
        
    def create_toolbar(self):
        """Create toolbar with view toggle and filters"""
        toolbar_frame = QFrame()
        toolbar_frame.setObjectName("toolbarFrame")
        
        layout = QHBoxLayout(toolbar_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Filter dropdown
        filter_label = QLabel("Filter:")
        filter_label.setStyleSheet("color: #9ca3af; font-size: 14px;")
        layout.addWidget(filter_label)
        
        self.filter_combo = QComboBox()
        self.filter_combo.setObjectName("filterCombo")
        self.filter_combo.addItems(["All Games", "Installed", "Not Installed", "Favorites"])
        self.filter_combo.setFixedWidth(150)
        self.filter_combo.currentTextChanged.connect(self.filter_games)
        layout.addWidget(self.filter_combo)
        
        layout.addSpacing(30)
        
        # Sort dropdown
        sort_label = QLabel("Sort by:")
        sort_label.setStyleSheet("color: #9ca3af; font-size: 14px;")
        layout.addWidget(sort_label)
        
        self.sort_combo = QComboBox()
        self.sort_combo.setObjectName("sortCombo")
        self.sort_combo.addItems(["Name", "Last Played", "Install Date", "Play Time"])
        self.sort_combo.setFixedWidth(150)
        self.sort_combo.currentTextChanged.connect(self.sort_games)
        layout.addWidget(self.sort_combo)
        
        layout.addStretch()
        
        # View toggle buttons
        grid_btn = QPushButton("▦ Grid")
        grid_btn.setObjectName("viewToggleBtn")
        grid_btn.setFixedWidth(80)
        grid_btn.clicked.connect(lambda: self.switch_view("grid"))
        layout.addWidget(grid_btn)
        
        list_btn = QPushButton("☰ List")
        list_btn.setObjectName("viewToggleBtn")
        list_btn.setFixedWidth(80)
        list_btn.clicked.connect(lambda: self.switch_view("list"))
        layout.addWidget(list_btn)
        
        return toolbar_frame
        
    def create_grid_view(self):
        """Create grid view for games"""
        grid_frame = QFrame()
        layout = QGridLayout(grid_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        
        # Scroll area for grid
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        content_widget = QWidget()
        self.grid_layout = QGridLayout(content_widget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(20)
        
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        
        return grid_frame
        
    def create_list_view(self):
        """Create list view for games"""
        list_frame = QFrame()
        layout = QVBoxLayout(list_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        content_widget = QWidget()
        self.list_layout = QVBoxLayout(content_widget)
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setSpacing(10)
        
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        
        return list_frame
        
    def switch_view(self, mode):
        """Switch between grid and list views"""
        self.view_mode = mode
        if mode == "grid":
            self.views_stack.setCurrentIndex(0)
        else:
            self.views_stack.setCurrentIndex(1)
        self.render_games()
        
    def load_games(self, games):
        """Load games into library"""
        self.games = games
        self.render_games()
        
    def render_games(self):
        """Render games in current view"""
        # Clear existing items
        if hasattr(self, 'grid_layout'):
            while self.grid_layout.count():
                item = self.grid_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
                    
        if hasattr(self, 'list_layout'):
            while self.list_layout.count():
                item = self.list_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
        
        # Render based on view mode
        if self.view_mode == "grid":
            for i, game in enumerate(self.games):
                card = GameCard(game)
                row = i // 4
                col = i % 4
                self.grid_layout.addWidget(card, row, col)
        else:
            for game in self.games:
                item = GameListItem(game)
                self.list_layout.addWidget(item)
                
    def filter_games(self):
        """Filter games based on search and filter criteria"""
        search_text = self.search_input.text().lower()
        filter_type = self.filter_combo.currentText()
        
        filtered = self.games
        
        # Apply search filter
        if search_text:
            filtered = [g for g in filtered if search_text in g.get('name', '').lower()]
            
        # Apply type filter
        if filter_type == "Installed":
            filtered = [g for g in filtered if g.get('status') == 'Installed']
        elif filter_type == "Not Installed":
            filtered = [g for g in filtered if g.get('status') != 'Installed']
            
        self.games = filtered
        self.render_games()
        
    def sort_games(self):
        """Sort games based on selected criteria"""
        sort_by = self.sort_combo.currentText()
        
        if sort_by == "Name":
            self.games.sort(key=lambda x: x.get('name', ''))
        elif sort_by == "Last Played":
            self.games.sort(key=lambda x: x.get('last_played', ''), reverse=True)
            
        self.render_games()
