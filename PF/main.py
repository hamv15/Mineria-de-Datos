from PyQt5.QtWidgets import QApplication, QMainWindow


from ui.main_window_ui import Ui_MainWindow

from pages_functions.home import Home
#from ui.pages.home_ui import Ui_Form as Ui_Form1
#from ui.pages.descDat_window_ui import Ui_Form as Ui_Form2
from pages_functions.descDat import descDat
from pages_functions.EDA import EDA
from pages_functions.selVar import selVar
from pages_functions.ACP import ACP
from pages_functions.ADPro import ADPro
from pages_functions.ADCla import ADCla
from pages_functions.BAPro import BAPro
from pages_functions.BACla import BACla
from pages_functions.KMeans import KMeans
from pages_functions.SVM import SVM
from pages_functions.resultados import resultados

import sys


ruta_buf="buf/"


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##Global Variables
        
        ## =======================================================================================================
        ## Get all the objects in windows
        ## =======================================================================================================
        self.home_btn = self.ui.pushButton
        self.descDat_btn = self.ui.pushButton_2
        self.EDA_btn = self.ui.pushButton_3
        self.ACP_btn = self.ui.pushButton_5
        self.ADPro_btn = self.ui.pushButton_6
        self.ADCla_btn = self.ui.pushButton_4
        self.BAPro_btn = self.ui.pushButton_7
        self.BACla_btn = self.ui.pushButton_12
        self.KMeans_btn = self.ui.pushButton_9
        self.SVM_btn = self.ui.pushButton_11
        self.resultados_btn = self.ui.pushButton_10

        ## =======================================================================================================
        ## Create dict for menu buttons and tab windows
        ## =======================================================================================================
        self.menu_btns_list = {
            self.home_btn: Home(),
            self.descDat_btn: descDat(),
            self.EDA_btn: EDA(),
            self.ACP_btn: ACP(),
            self.ADPro_btn : ADPro(),
            self.ADCla_btn : ADCla(),
            self.BAPro_btn : BAPro(),
            self.BACla_btn : BACla(),
            self.KMeans_btn : KMeans(),
            self.SVM_btn : SVM(),
            self.resultados_btn: resultados(),
        }

        ## =======================================================================================================
        ## Show home window when start app
        ## =======================================================================================================
        self.show_home_window()

        ## =======================================================================================================
        ## Connect signal and slot
        ## =======================================================================================================
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.home_btn.clicked.connect(self.show_selected_window)
        self.descDat_btn.clicked.connect(self.show_selected_window)
        self.EDA_btn.clicked.connect(self.show_selected_window)
        self.ACP_btn.clicked.connect(self.show_selected_window)
        self.ADPro_btn.clicked.connect(self.show_selected_window)
        self.ADCla_btn.clicked.connect(self.show_selected_window)
        self.BAPro_btn.clicked.connect(self.show_selected_window)
        self.BACla_btn.clicked.connect(self.show_selected_window)
        self.KMeans_btn.clicked.connect(self.show_selected_window)
        self.SVM_btn.clicked.connect(self.show_selected_window)
        self.resultados_btn.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        """
        Function for showing home window
        :return:
        """
        result = self.open_tab_flag(self.home_btn.text())
        self.set_btn_checked(self.home_btn)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = self.home_btn.text()
            curIndex = self.ui.tabWidget.addTab(Home(), title)
            
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def show_selected_window(self):
        """
        Function for showing selected window
        :return:
        """
        button = self.sender()

        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_list[button], title)
            #Sospecho que en esta parte se ejecuta la ventana
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)
            #if button == self.descDat_btn:
            #    print("Estoy en la ventana de descripción de datos")
                
                
    def close_tab(self, index):
        """
        Function for close tab in tabWidget
        :param index: index of tab
        :return:
        """
        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count() == 0:
            self.ui.toolBox.setCurrentIndex(0)
            self.show_home_window()

    def open_tab_flag(self, tab):
        """
        Check if selected window showed or not
        :param tab: tab title
        :return: bool and index
        """
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_name = self.ui.tabWidget.tabText(i)
            if tab_name == tab:
                return True, i
            else:
                continue

        return False,

    def set_btn_checked(self, btn):
        """
        Set the status of selected button checked and set other buttons' status unchecked
        :param btn: button object
        :return:
        """
        for button in self.menu_btns_list.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)

        

if __name__ == '__main__':
    file=open(ruta_buf+"ruta_archivo.txt","w")
    file.write("")
    file.close()
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
    
