# -------------------------------
#
# BY: NATÃ ALMEIDA GAGO
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# -------------------------------

# IMPORT QT CORE
from qt_core import * 

# IMPORT PAGES
from interface.pages.ui_pages import Ui_application_pages

# MAIN WINDOW
class UI_MainWindow():
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            
        # SET INITIAL PARAMETERS
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)
        
        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        
        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMinimumWidth(50)
        self.left_menu.setMaximumWidth(50)
        
        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)
        
        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setStyleSheet("background-color: red")
        
        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setStyleSheet("background-color: red")
        
        # LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")
        
        # ADD TO LEFT MENU LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addSpacerItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        
        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        
        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        
        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)
        
        # Left label
        self.top_label_left = QLabel("Minha aplicação com PySide6")
        
        # Top spacer
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # Right label
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")
        
        # Add to top bar layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addSpacerItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)
        
        # Application pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)
        
        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)
        
        # Left label
        self.bottom_label_left = QLabel("Criado por: Natã A. Gago")
        
        # Bottom spacer
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # Right label
        self.bottom_label_right = QLabel(u"\u00A9 2021")
        
        # Add to bottom bar layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addSpacerItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)
        
        # Add to content layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
        
        
        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)