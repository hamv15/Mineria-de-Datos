
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QAbstractItemView,
                             QFileDialog, QWidget)
from PyQt5 import QtWidgets
from ui.pages.home_ui import Ui_Form


import pandas as pd

#Global variable
ruta_buf="buf/"
ruta_archivo=ruta_buf+"datos.csv"

class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        #Instancia de la clase importar datos
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Define window objects
        self.open_button = self.ui.abrirButton
        self.select_button = self.ui.seleccionarButton
        self.file_name_line_edit = self.ui.rutaArchivoLineEdit
        self.tabla = self.ui.datosTableWidget
        #Configuración de la tabla
         # Deshabilitar edición
        #self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.tabla.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.tabla.setWordWrap(False)
        # Deshabilitar clasificación
        self.tabla.setSortingEnabled(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupe todo el espacio disponible
        #self.tabla.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)

        # Set global variable name
        self.file_name = ""
        self.file_path = ""
        self.dataOriginal=pd.DataFrame()
        # Associated open file event
        self.select_button.clicked.connect(self.open_file)
        self.open_button.clicked.connect(self.show_info_file)
        

    # Create open file method
    def open_file(self):
        self.file_path = QFileDialog.getOpenFileName(caption='Seleccionar Archivo', directory='',
                                                     filter='Excel files(*.xlsx , *.xls, *.csv)', initialFilter='')
        self.file_name = self.file_path[0].split('/')[-1]
        # Call the display file name method
        self.show_file_path()

    # Create a display file name method
    def show_file_path(self):
        file_name = self.file_name
        if file_name:
            # Set QLineEdit to display text
            self.file_name_line_edit.setText(self.file_path[0])
            #Genera archivo en el buf 
            file=open(ruta_buf+"ruta_archivo.txt","w")
            file.write(self.file_path[0])
            file.close()
            


        else:
            pass

    def show_info_file(self):
        try:
            if self.file_path[0]!='':
                self.dataOriginal=pd.read_csv(str(self.file_path[0]))
                #Se abre y cargan los datos a la tabla
                # Definición de renglones y columnas totales
                self.tabla.setColumnCount(len(self.dataOriginal.columns))
                self.tabla.setRowCount(len(self.dataOriginal))
                self.tabla.setHorizontalHeaderLabels(self.dataOriginal.columns)
                #Llenado de datos en tabla
                for i in range(len(self.dataOriginal)):
                    for j in range(len(self.dataOriginal.columns)):
                        self.tabla.setItem(i,j,QtWidgets.QTableWidgetItem(str(self.dataOriginal.iat[i,j])))
                self.dataOriginal.to_csv(ruta_archivo, index=False)
                
            
        except IndexError:
            print("No hay ruta de archivo")
            


