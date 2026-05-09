"""
Utility helpers for NodifyGamers
Includes styling, formatting, and common helper functions
"""

from typing import Dict, Any


def apply_modern_styles() -> str:
    """
    Apply modern dark theme stylesheet with smooth animations
    Returns comprehensive Qt stylesheet string
    """
    return """
    /* ===== GLOBAL STYLES ===== */
    QMainWindow {
        background-color: #0f172a;
    }
    
    QWidget {
        background-color: transparent;
        color: #e5e7eb;
        font-family: "Segoe UI", "Roboto", sans-serif;
    }
    
    /* ===== NAVIGATION FRAME ===== */
    #navFrame {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }
    
    /* ===== BRAND BUTTON ===== */
    #brandButton {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #6366f1, stop:1 #8b5cf6);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        text-align: left;
        padding-left: 20px;
    }
    
    #brandButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #4f46e5, stop:1 #7c3aed);
    }
    
    /* ===== NAVIGATION BUTTONS ===== */
    QPushButton#navButton_dashboard,
    QPushButton#navButton_library,
    QPushButton#navButton_news,
    QPushButton#navButton_settings {
        background-color: transparent;
        color: #9ca3af;
        font-size: 15px;
        font-weight: 500;
        border-radius: 10px;
        text-align: left;
        padding-left: 20px;
    }
    
    QPushButton#navButton_dashboard:hover,
    QPushButton#navButton_library:hover,
    QPushButton#navButton_news:hover,
    QPushButton#navButton_settings:hover {
        background-color: #334155;
        color: #f9fafb;
    }
    
    QPushButton#navButton_dashboard[active="true"],
    QPushButton#navButton_library[active="true"],
    QPushButton#navButton_news[active="true"],
    QPushButton#navButton_settings[active="true"] {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #6366f1, stop:1 #8b5cf6);
        color: white;
    }
    
    /* ===== CONTENT AREA ===== */
    #contentStack {
        background-color: #0f172a;
    }
    
    /* ===== PANELS ===== */
    #dashboardPanel,
    #gameLibraryPanel,
    #newsPanel,
    #settingsPanel {
        background-color: #0f172a;
    }
    
    /* ===== CARDS & FRAMES ===== */
    #statCard,
    #actionsFrame,
    #activityFrame,
    #libraryHeader,
    #toolbarFrame,
    #gameCard,
    #newsCard,
    #updateItem,
    #settingsSection {
        background-color: #1e293b;
        border-radius: 12px;
    }
    
    #statsFrame {
        background-color: transparent;
    }
    
    #headerFrame {
        background-color: transparent;
        border-bottom: 1px solid #334155;
    }
    
    #newsHeader,
    #settingsHeader {
        background-color: transparent;
        border-bottom: 1px solid #334155;
    }
    
    /* ===== GAME CARDS ===== */
    #gameCard {
        background-color: #1e293b;
        border-radius: 8px;
    }
    
    #gameCover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #374151, stop:1 #1f2937);
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
    }
    
    #gameInfo {
        background-color: #1e293b;
        border-bottom-left-radius: 8px;
        border-bottom-right-radius: 8px;
    }
    
    /* ===== LIST ITEMS ===== */
    #gameListItem {
        background-color: #1e293b;
        border-radius: 8px;
    }
    
    #gameListItem:hover {
        background-color: #334151;
    }
    
    #activityItem {
        background-color: #1e293b;
        border-radius: 8px;
        border-left: 3px solid #6366f1;
    }
    
    /* ===== SCROLL AREAS ===== */
    QScrollArea {
        background-color: transparent;
        border: none;
    }
    
    QScrollBar:vertical {
        background-color: #1e293b;
        width: 10px;
        border-radius: 5px;
    }
    
    QScrollBar::handle:vertical {
        background-color: #475569;
        min-height: 30px;
        border-radius: 5px;
    }
    
    QScrollBar::handle:vertical:hover {
        background-color: #6366f1;
    }
    
    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {
        height: 0px;
    }
    
    QScrollBar:horizontal {
        background-color: #1e293b;
        height: 10px;
        border-radius: 5px;
    }
    
    QScrollBar::handle:horizontal {
        background-color: #475569;
        min-width: 30px;
        border-radius: 5px;
    }
    
    QScrollBar::handle:horizontal:hover {
        background-color: #6366f1;
    }
    
    QScrollBar::add-line:horizontal,
    QScrollBar::sub-line:horizontal {
        width: 0px;
    }
    
    /* ===== BUTTONS ===== */
    QPushButton {
        background-color: #334155;
        color: #e5e7eb;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 500;
    }
    
    QPushButton:hover {
        background-color: #475569;
    }
    
    QPushButton:pressed {
        background-color: #6366f1;
    }
    
    #quickActionBtn {
        background-color: #1e293b;
        border: 2px solid #334155;
        border-radius: 12px;
    }
    
    #quickActionBtn:hover {
        background-color: #334155;
        border-color: #6366f1;
    }
    
    #playButton {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #10b981, stop:1 #059669);
        color: white;
        font-weight: bold;
    }
    
    #playButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #059669, stop:1 #047857);
    }
    
    #updateButton {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #6366f1, stop:1 #4f46e5);
        color: white;
        font-weight: 600;
    }
    
    #updateButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #4f46e5, stop:1 #4338ca);
    }
    
    #refreshBtn,
    #saveBtn {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #6366f1, stop:1 #8b5cf6);
        color: white;
        font-weight: 600;
    }
    
    #refreshBtn:hover,
    #saveBtn:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #4f46e5, stop:1 #7c3aed);
    }
    
    #browseBtn {
        background-color: #334155;
    }
    
    #viewToggleBtn {
        background-color: #334155;
    }
    
    #viewToggleBtn:hover {
        background-color: #6366f1;
    }
    
    /* ===== INPUT FIELDS ===== */
    QLineEdit {
        background-color: #1e293b;
        color: #f9fafb;
        border: 2px solid #334155;
        border-radius: 10px;
        padding: 10px 15px;
        font-size: 14px;
    }
    
    QLineEdit:focus {
        border-color: #6366f1;
    }
    
    QLineEdit::placeholder {
        color: #6b7280;
    }
    
    /* ===== COMBO BOXES ===== */
    QComboBox {
        background-color: #1e293b;
        color: #f9fafb;
        border: 2px solid #334155;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 14px;
    }
    
    QComboBox:hover {
        border-color: #6366f1;
    }
    
    QComboBox::drop-down {
        border: none;
        width: 30px;
    }
    
    QComboBox QAbstractItemView {
        background-color: #1e293b;
        border: 2px solid #334155;
        border-radius: 8px;
        selection-background-color: #6366f1;
    }
    
    /* ===== TAB WIDGET ===== */
    QTabWidget::pane {
        background-color: #1e293b;
        border-radius: 12px;
        border: none;
    }
    
    QTabBar::tab {
        background-color: #334155;
        color: #9ca3af;
        padding: 12px 24px;
        margin-right: 4px;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
        font-weight: 500;
    }
    
    QTabBar::tab:selected {
        background-color: #6366f1;
        color: white;
    }
    
    QTabBar::tab:hover:!selected {
        background-color: #475569;
    }
    
    /* ===== SLIDERS ===== */
    QSlider::groove:horizontal {
        background-color: #334155;
        height: 8px;
        border-radius: 4px;
    }
    
    QSlider::handle:horizontal {
        background-color: #6366f1;
        width: 20px;
        margin: -6px 0;
        border-radius: 10px;
    }
    
    QSlider::handle:horizontal:hover {
        background-color: #4f46e5;
    }
    
    /* ===== LABELS ===== */
    QLabel {
        color: #e5e7eb;
    }
    
    /* ===== CHECKBOXES ===== */
    QCheckBox {
        color: #e5e7eb;
        spacing: 10px;
    }
    
    QCheckBox::indicator {
        width: 20px;
        height: 20px;
        border-radius: 5px;
        border: 2px solid #475569;
        background-color: #1e293b;
    }
    
    QCheckBox::indicator:checked {
        background-color: #6366f1;
        border-color: #6366f1;
    }
    
    /* ===== PROGRESS BARS ===== */
    QProgressBar {
        background-color: #334155;
        border-radius: 8px;
        height: 10px;
        text-align: center;
    }
    
    QProgressBar::chunk {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #6366f1, stop:1 #8b5cf6);
        border-radius: 8px;
    }
    
    /* ===== TOOLTIPS ===== */
    QToolTip {
        background-color: #1e293b;
        color: #f9fafb;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 8px 12px;
    }
    
    /* ===== MENU BAR ===== */
    QMenuBar {
        background-color: #1e293b;
        color: #e5e7eb;
        padding: 5px;
    }
    
    QMenuBar::item:selected {
        background-color: #334155;
        border-radius: 6px;
    }
    
    QMenu {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 8px;
    }
    
    QMenu::item:selected {
        background-color: #6366f1;
        border-radius: 6px;
    }
    
    /* ===== DIALOGS ===== */
    QDialog {
        background-color: #0f172a;
    }
    
    QMessageBox {
        background-color: #1e293b;
    }
    """


def format_file_size(size_bytes: float) -> str:
    """Format file size in human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def format_play_time(minutes: int) -> str:
    """Format play time in hours and minutes"""
    hours = minutes // 60
    mins = minutes % 60
    
    if hours > 0:
        return f"{hours}h {mins}m"
    return f"{mins}m"


def format_date(date_str: str) -> str:
    """Format date string to readable format"""
    # Implementation for date formatting
    return date_str


def truncate_text(text: str, max_length: int = 50) -> str:
    """Truncate text with ellipsis"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def get_color_for_status(status: str) -> str:
    """Get color code for game status"""
    colors = {
        "Installed": "#10b981",
        "Not Installed": "#6b7280",
        "Updating": "#f59e0b",
        "Downloading": "#3b82f6",
        "Error": "#ef4444"
    }
    return colors.get(status, "#6b7280")
