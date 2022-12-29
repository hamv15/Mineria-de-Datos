from PyQt5.QtWidgets import QWidget

from ui.pages.resultados_window_ui import Ui_Form


class resultados(QWidget):
    def __init__(self):
        super(resultados, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
