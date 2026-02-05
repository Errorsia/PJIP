from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout

from .page_updating import PageUpdating


class AboutPage(QWidget):
    ui_change = Signal(str, object)

    def __init__(self):
        super().__init__()
        self.page_name = 'About'

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        # main_layout.setContentsMargins(3, 3, 3, 3)
        # main_layout.setSpacing(5)

        page_updating = PageUpdating()

        main_layout.addWidget(page_updating)

        self.setLayout(main_layout)