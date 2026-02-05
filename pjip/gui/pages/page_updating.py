from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class PageUpdating(QWidget):
    def __init__(self):
        super().__init__()
        self.updating_label = None

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3, 3, 3, 3)
        main_layout.setSpacing(5)

        self.updating_label = QLabel()
        self.updating_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.updating_label.setText('Page Updating')
        self.updating_label.setStyleSheet("""
                                        background-color: #efefef; 
                                        /* border-radius: 10px; */
                                        font-size: 24px;
                                        /* border: 3px solid #cccccc; */
                                        /* border: 1px solid #bbbbbb; */
                                        color: green; 
                                        font-weight: bold; 
                                        """)

        main_layout.addWidget(self.updating_label)
        self.setLayout(main_layout)