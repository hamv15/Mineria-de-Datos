from PyQt5.QtWidgets import QWidget

from ui.pages.selVar_window_ui import Ui_Form


class selVar(QWidget):
    def __init__(self):
        super(selVar, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
