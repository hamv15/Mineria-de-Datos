# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 426)
        MainWindow.setStyleSheet("#menu_widget, #toolBox {\n"
"    background-color: #3333FF;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.menu_widget = QtWidgets.QWidget(self.splitter)
        self.menu_widget.setMinimumSize(QtCore.QSize(220, 0))
        self.menu_widget.setStyleSheet("background-color: #06162d;\n"
"color: #fff;\n"
"border: none;")
        self.menu_widget.setObjectName("menu_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.menu_widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.toolBox = QtWidgets.QToolBox(self.menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolBox.setFont(font)
        self.toolBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolBox.setMouseTracking(False)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet("#toolBox {\n"
"    color: #fff;\n"
"}\n"
"\n"
"#toolBox::tab {\n"
"    padding-left:5px;\n"
"    text-align:left;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"#toolBox::tab:selected {\n"
"    background-color: #2d9cdb;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#toolBox QPushButton {\n"
"    padding:5px 0px 5px 20px;\n"
"    text-align:left;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton:hover {\n"
"    background-color: #85C1E9;\n"
"}\n"
"\n"
"#toolBox QPushButton:checked {\n"
"    background-color: #3498DB;\n"
"}\n"
"\n"
"")
        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName("toolBox")
        self.general_page = QtWidgets.QWidget()
        self.general_page.setGeometry(QtCore.QRect(0, 0, 196, 109))
        self.general_page.setObjectName("general_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.general_page)
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.general_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.general_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/archivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.general_page, icon, "")
        self.cars_page = QtWidgets.QWidget()
        self.cars_page.setGeometry(QtCore.QRect(0, 0, 186, 109))
        self.cars_page.setObjectName("cars_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cars_page)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.cars_page)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.cars_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/navegador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.cars_page, icon1, "")
        self.social_media_page = QtWidgets.QWidget()
        self.social_media_page.setGeometry(QtCore.QRect(0, 0, 213, 248))
        self.social_media_page.setObjectName("social_media_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.social_media_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.social_media_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.social_media_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.social_media_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_12 = QtWidgets.QPushButton(self.social_media_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_4.addWidget(self.pushButton_12)
        self.pushButton_9 = QtWidgets.QPushButton(self.social_media_page)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_11 = QtWidgets.QPushButton(self.social_media_page)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_4.addWidget(self.pushButton_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/codificacion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.social_media_page, icon2, "")
        self.validacion_page = QtWidgets.QWidget()
        self.validacion_page.setGeometry(QtCore.QRect(0, 0, 186, 100))
        self.validacion_page.setAutoFillBackground(False)
        self.validacion_page.setObjectName("validacion_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.validacion_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.validacion_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_6.addWidget(self.pushButton_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.validacion_page, icon3, "")
        self.verticalLayout_7.addWidget(self.toolBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.main_widget = QtWidgets.QWidget(self.splitter)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.search_widget = QtWidgets.QWidget(self.main_widget)
        self.search_widget.setStyleSheet("#search_widget {background-color: #ABB2B9;}")
        self.search_widget.setObjectName("search_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.search_widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-96-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-31-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.search_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem6 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.user_label = QtWidgets.QLabel(self.search_widget)
        self.user_label.setMinimumSize(QtCore.QSize(30, 30))
        self.user_label.setMaximumSize(QtCore.QSize(30, 30))
        self.user_label.setStyleSheet("#user_label {\n"
"    background-color: #fff;\n"
"    border: 1px solid #F2F4F4;\n"
"    padding: 5px 5px;\n"
"    border-radius: 15%;\n"
"}")
        self.user_label.setText("")
        self.user_label.setPixmap(QtGui.QPixmap(":/icon/icon/user-48.ico"))
        self.user_label.setScaledContents(True)
        self.user_label.setObjectName("user_label")
        self.horizontalLayout.addWidget(self.user_label)
        self.gridLayout_4.addWidget(self.search_widget, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("#tabWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"    margin-left: 3px;\n"
"    image: url(:/icon/icon/x-mark-4-32.ico)\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    \n"
"    image: url(:/icon/icon/x-mark-4-48.ico);\n"
"}")
        self.tabWidget.setIconSize(QtCore.QSize(10, 10))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(-1)
        self.tabWidget.setCurrentIndex(-1)
        self.pushButton_8.toggled['bool'].connect(self.menu_widget.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HM Data Mining"))
        self.pushButton.setText(_translate("MainWindow", "Importar Datos"))
        self.pushButton_2.setText(_translate("MainWindow", "Descripción de Datos"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.general_page), _translate("MainWindow", "Origen de los Datos"))
        self.pushButton_3.setText(_translate("MainWindow", "Análisis Exploratorio de Datos"))
        self.pushButton_5.setText(_translate("MainWindow", "ACP"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.cars_page), _translate("MainWindow", "Preparación de Datos"))
        self.pushButton_6.setText(_translate("MainWindow", "Arboles de Decisión (Pronóstico))"))
        self.pushButton_4.setText(_translate("MainWindow", "Árboles de Decisión (Clasificación)"))
        self.pushButton_7.setText(_translate("MainWindow", "Bosques Aelatorios (Pronóstico)"))
        self.pushButton_12.setText(_translate("MainWindow", "Bosques Aelatorios (Clasificación)"))
        self.pushButton_9.setText(_translate("MainWindow", "K-means (Clasificación)"))
        self.pushButton_11.setText(_translate("MainWindow", "SVM (Clasificación)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.social_media_page), _translate("MainWindow", "Minería de Datos"))
        self.pushButton_10.setText(_translate("MainWindow", "Matriz de Resultados"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.validacion_page), _translate("MainWindow", "Validación"))
        self.label.setText(_translate("MainWindow", "HM-DATA MINING"))
from . import resource_rc
