# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'descDat.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(655, 398)
        Form.setMinimumSize(QtCore.QSize(400, 398))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.dnullTextEdit = QtWidgets.QTextEdit(self.frame)
        self.dnullTextEdit.setMinimumSize(QtCore.QSize(0, 150))
        self.dnullTextEdit.setAcceptDrops(False)
        self.dnullTextEdit.setReadOnly(True)
        self.dnullTextEdit.setObjectName("dnullTextEdit")
        self.gridLayout.addWidget(self.dnullTextEdit, 2, 1, 1, 1)
        self.dtypesTextEdit = QtWidgets.QTextEdit(self.frame)
        self.dtypesTextEdit.setMinimumSize(QtCore.QSize(0, 150))
        self.dtypesTextEdit.setAcceptDrops(False)
        self.dtypesTextEdit.setReadOnly(True)
        self.dtypesTextEdit.setObjectName("dtypesTextEdit")
        self.gridLayout.addWidget(self.dtypesTextEdit, 2, 0, 1, 1)
        self.eliminarButton = QtWidgets.QPushButton(self.frame)
        self.eliminarButton.setObjectName("eliminarButton")
        self.gridLayout.addWidget(self.eliminarButton, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.actualizarButton = QtWidgets.QPushButton(self.frame)
        self.actualizarButton.setObjectName("actualizarButton")
        self.horizontalLayout_2.addWidget(self.actualizarButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Datos faltantes"))
        self.label_2.setText(_translate("Form", "Variables y sus tipos de datos"))
        self.eliminarButton.setText(_translate("Form", "Eliminar Nulos"))
        self.label.setText(_translate("Form", "Descripción de datos"))
        self.actualizarButton.setText(_translate("Form", "ACTUALIZAR"))