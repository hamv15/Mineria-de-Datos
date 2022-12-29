from PyQt5.QtWidgets import QWidget

from ui.pages.BAPro_window_ui import Ui_Form


class BAPro(QWidget):
    def __init__(self):
        super(BAPro, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
