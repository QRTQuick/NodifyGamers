"""
Modern Settings Panel with categorized options
Enhanced UI/UX with toggle switches and organized sections
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, 
    QPushButton, QScrollArea, QGridLayout, QComboBox,
    QSlider, QFileDialog, QGraphicsDropShadowEffect
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor


class ToggleSwitch(QFrame):
    """Modern toggle switch component"""
    
    def __init__(self, enabled=False, callback=None):
        super().__init__()
        self.enabled = enabled
        self.callback = callback
        
        self.setObjectName("toggleSwitch")
        self.setFixedSize(50, 28)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(shadow)
        
        self.update_style()
        
    def update_style(self):
        """Update toggle appearance based on state"""
        if self.enabled:
            self.setStyleSheet("""
                #toggleSwitch {
                    background-color: #10b981;
                    border-radius: 14px;
                }
            """)
        else:
            self.setStyleSheet("""
                #toggleSwitch {
                    background-color: #4b5563;
                    border-radius: 14px;
                }
            """)
            
    def mousePressEvent(self, event):
        """Handle click to toggle"""
        self.enabled = not self.enabled
        self.update_style()
        if self.callback:
            self.callback(self.enabled)


class SettingRow(QFrame):
    """Single setting row with label and control"""
    
    def __init__(self, title, description, control_widget):
        super().__init__()
        self.setObjectName("settingRow")
        self.setFixedHeight(80)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 15, 0, 15)
        layout.setSpacing(20)
        
        # Text info
        text_layout = QVBoxLayout()
        text_layout.setSpacing(3)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("color: #f9fafb; font-weight: 600; font-size: 15px;")
        text_layout.addWidget(title_label)
        
        desc_label = QLabel(description)
        desc_label.setStyleSheet("color: #9ca3af; font-size: 13px;")
        text_layout.addWidget(desc_label)
        
        layout.addLayout(text_layout)
        layout.addStretch()
        layout.addWidget(control_widget)


class SettingsPanel(QWidget):
    """Settings panel with organized categories"""
    
    def __init__(self, parent=None):
        super().__init__()
        self.setObjectName("settingsPanel")
        self.parent_window = parent
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup settings UI"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(25)
        
        # Header
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Settings content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(25)
        
        # Setting sections
        content_layout.addWidget(self.create_general_section())
        content_layout.addWidget(self.create_appearance_section())
        content_layout.addWidget(self.create_downloads_section())
        content_layout.addWidget(self.create_notifications_section())
        content_layout.addStretch()
        
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)
        
    def create_header(self):
        """Create settings header"""
        header_frame = QFrame()
        header_frame.setObjectName("settingsHeader")
        
        layout = QHBoxLayout(header_frame)
        layout.setContentsMargins(0, 0, 0, 15)
        
        title = QLabel("Settings")
        title.setStyleSheet("color: #f9fafb; font-size: 28px; font-weight: bold;")
        layout.addWidget(title)
        layout.addStretch()
        
        # Save button
        save_btn = QPushButton("💾 Save Changes")
        save_btn.setObjectName("saveBtn")
        save_btn.setFixedWidth(130)
        save_btn.clicked.connect(self.save_settings)
        layout.addWidget(save_btn)
        
        return header_frame
        
    def create_general_section(self):
        """Create general settings section"""
        section = QFrame()
        section.setObjectName("settingsSection")
        
        layout = QVBoxLayout(section)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Section title
        title = QLabel("⚙️ General")
        title.setStyleSheet("color: #6366f1; font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Language selector
        lang_combo = QComboBox()
        lang_combo.setObjectName("settingCombo")
        lang_combo.addItems(["English", "Spanish", "French", "German", "Japanese"])
        lang_combo.setFixedWidth(200)
        lang_row = SettingRow("Language", "Select your preferred language", lang_combo)
        layout.addWidget(lang_row)
        
        # Launch on startup toggle
        startup_toggle = ToggleSwitch(False)
        startup_row = SettingRow("Launch on Startup", "Start NodifyGamers when Windows starts", startup_toggle)
        layout.addWidget(startup_row)
        
        # Run in background toggle
        bg_toggle = ToggleSwitch(True)
        bg_row = SettingRow("Run in Background", "Keep app running when closed", bg_toggle)
        layout.addWidget(bg_row)
        
        return section
        
    def create_appearance_section(self):
        """Create appearance settings section"""
        section = QFrame()
        section.setObjectName("settingsSection")
        
        layout = QVBoxLayout(section)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Section title
        title = QLabel("🎨 Appearance")
        title.setStyleSheet("color: #6366f1; font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Theme selector
        theme_combo = QComboBox()
        theme_combo.setObjectName("settingCombo")
        theme_combo.addItems(["Dark Mode", "Light Mode", "Auto"])
        theme_combo.setFixedWidth(200)
        theme_row = SettingRow("Theme", "Choose application theme", theme_combo)
        layout.addWidget(theme_row)
        
        # Accent color selector
        accent_combo = QComboBox()
        accent_combo.setObjectName("settingCombo")
        accent_combo.addItems(["Purple", "Blue", "Green", "Orange", "Pink"])
        accent_combo.setFixedWidth(200)
        accent_row = SettingRow("Accent Color", "Customize accent color", accent_combo)
        layout.addWidget(accent_row)
        
        # Animation toggle
        anim_toggle = ToggleSwitch(True)
        anim_row = SettingRow("Enable Animations", "Smooth transitions and effects", anim_toggle)
        layout.addWidget(anim_row)
        
        return section
        
    def create_downloads_section(self):
        """Create download settings section"""
        section = QFrame()
        section.setObjectName("settingsSection")
        
        layout = QVBoxLayout(section)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Section title
        title = QLabel("⬇️ Downloads")
        title.setStyleSheet("color: #6366f1; font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Download location
        location_btn = QPushButton("📁 Browse...")
        location_btn.setObjectName("browseBtn")
        location_btn.setFixedWidth(120)
        location_btn.clicked.connect(self.browse_download_location)
        location_row = SettingRow("Download Location", "C:\\Games\\NodifyGamers", location_btn)
        layout.addWidget(location_row)
        
        # Auto-update toggle
        auto_update_toggle = ToggleSwitch(True)
        auto_update_row = SettingRow("Auto-Update Games", "Automatically download updates", auto_update_toggle)
        layout.addWidget(auto_update_row)
        
        # Download limit slider
        limit_slider = QSlider(Qt.Orientation.Horizontal)
        limit_slider.setObjectName("settingSlider")
        limit_slider.setRange(0, 100)
        limit_slider.setValue(80)
        limit_slider.setFixedWidth(200)
        limit_row = SettingRow("Download Speed Limit", f"Current: 80%", limit_slider)
        layout.addWidget(limit_row)
        
        return section
        
    def create_notifications_section(self):
        """Create notifications settings section"""
        section = QFrame()
        section.setObjectName("settingsSection")
        
        layout = QVBoxLayout(section)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Section title
        title = QLabel("🔔 Notifications")
        title.setStyleSheet("color: #6366f1; font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Update notifications
        update_notif_toggle = ToggleSwitch(True)
        update_notif_row = SettingRow("Update Notifications", "Get notified when updates are available", update_notif_toggle)
        layout.addWidget(update_notif_row)
        
        # News notifications
        news_notif_toggle = ToggleSwitch(False)
        news_notif_row = SettingRow("News & Promotions", "Receive news and promotional content", news_notif_toggle)
        layout.addWidget(news_notif_row)
        
        # Desktop notifications
        desktop_notif_toggle = ToggleSwitch(True)
        desktop_notif_row = SettingRow("Desktop Notifications", "Show popup notifications", desktop_notif_toggle)
        layout.addWidget(desktop_notif_row)
        
        return section
        
    def browse_download_location(self):
        """Open file dialog to select download location"""
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Download Location",
            "",
            QFileDialog.Option.ShowDirsOnly
        )
        if directory:
            print(f"Download location set to: {directory}")
            
    def save_settings(self):
        """Save all settings"""
        print("Saving settings...")
        # Add settings persistence logic here
        
    def load_settings(self):
        """Load saved settings"""
        # Add settings loading logic here
        pass
