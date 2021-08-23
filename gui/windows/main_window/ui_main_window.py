from qt_core import *


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)
        
        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #282a36")

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        # self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        # self.left_menu.setMaximumHeight(50)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)

        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)

        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")

        # ADD TO CONTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WINGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)