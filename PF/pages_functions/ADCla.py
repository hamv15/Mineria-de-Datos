from PyQt5.QtWidgets import QWidget

from ui.pages.ADCla_window_ui import Ui_Form


class ADCla(QWidget):
    def __init__(self):
        super(ADCla, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
