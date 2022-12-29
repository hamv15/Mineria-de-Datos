from PyQt5.QtWidgets import QWidget

from ui.pages.ADPro_window_ui import Ui_Form


class ADPro(QWidget):
    def __init__(self):
        super(ADPro, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
