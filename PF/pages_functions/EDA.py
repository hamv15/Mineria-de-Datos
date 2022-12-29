from PyQt5.QtWidgets import (QAbstractItemView, QMenu,
                             QAction, QWidget)
from PyQt5.QtCore import Qt
from PyQt5 import  QtWidgets
from ui.pages.EDA_window_ui import Ui_Form
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import math
import random
from matplotlib.ticker import ScalarFormatter


#Global variable
ruta_buf="buf/"
ruta_dfObject=ruta_buf+"datosObject.csv"
ruta_dfNumericos=ruta_buf+"datosNumericos.csv"
ruta_dfCompleto=ruta_buf+"datos.csv"

varBox=[]
varBox2=[]
class EDA(QWidget):
    def __init__(self):
        super(EDA, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ##Variables 
        self.datos=pd.DataFrame()
        
        # =================== WIDGETS QVBOXLAYOUT & QPUSHBUTTON ==================
        
        #       *** QvBoxLayout ***
        self.box=self.ui.box
        self.box2=self.ui.box2
        self.box3=self.ui.box3
        self.box4=self.ui.box4
        self.menu=QMenu()

            
        #       *** QPushButton ***
        self.actualizarBoton=self.ui.actualizarButton
        self.limpiarBoton=self.ui.limpiarButton 
        self.botonSelecVariables=self.ui.varCajas
        self.botonSelecVariables.setMenu(self.menu)
        
        # ================== WIDGET  QTableWidget ==================
        #       *** Tabla para resumen estadístico de variables numéricas
        self.describeTable= self.ui.describeTable
        #   Configuración de tabla
        #self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.describeTable.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.describeTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.describeTable.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.describeTable.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.describeTable.setWordWrap(False)
        # Deshabilitar clasificación
        self.describeTable.setSortingEnabled(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.describeTable.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupe todo el espacio disponible
        #self.describeTable.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.describeTable.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.describeTable.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.describeTable.verticalHeader().setDefaultSectionSize(20)
        
        #          *** Tabla para resumen estadístico de variables categóricas
        self.describeTable2= self.ui.describeTable2
        #   Configuración de tabla
        #self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.describeTable2.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.describeTable2.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.describeTable2.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.describeTable2.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.describeTable2.setWordWrap(False)
        # Deshabilitar clasificación
        self.describeTable2.setSortingEnabled(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.describeTable2.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupe todo el espacio disponible
        #self.describeTable.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.describeTable2.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.describeTable2.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.describeTable2.verticalHeader().setDefaultSectionSize(20)
        
        #          *** Tabla para matriz de correlaciones
        self.describeTable3= self.ui.describeTable3
        #   Configuración de tabla
        #self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.describeTable3.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.describeTable3.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.describeTable3.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.describeTable3.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.describeTable3.setWordWrap(False)
        # Deshabilitar clasificación
        self.describeTable3.setSortingEnabled(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.describeTable3.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupe todo el espacio disponible
        #self.describeTable.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.describeTable3.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.describeTable3.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.describeTable3.verticalHeader().setDefaultSectionSize(20)
        
        
        
        # =================== VARIABLES PROPÓSITO GENERAL ==================
        
        self.datosPuros=pd.DataFrame()
        self.describeDatos=pd.DataFrame()
        self.describeDatosObj=pd.DataFrame()
        self.matrizCorr=pd.DataFrame()
        self.estadisticos=pd.DataFrame({"Estadisticos" : ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']})
        self.estadisticos.index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
        self.estadisticos2=pd.DataFrame({"Estadisticos" : ['count', 'unique', 'top', 'freq']})
        self.estadisticos2.index=['count', 'unique', 'top', 'freq']

         # ======================== EVENTOS =========================
        self.actualizarBoton.clicked.connect(self.generarGrafica)
        self.limpiarBoton.clicked.connect(self.limpiar)
        self.menu.triggered.connect(self.mostrarBigotes)
        
        
    # ======================= FUNCIONES ============================    
    
    def generarGrafica(self):
        self.limpiar()
        self.datos=pd.read_csv(ruta_dfNumericos)
        
        self.datosCompletos=pd.read_csv(ruta_dfCompleto)
        #Histogramas Variables numericas
        self.Histograma=Histograma()
        self.box.addWidget(self.Histograma)
        #Resumen estadístico variables numéricas
        self.showDescribe()
        
         
        
        #Operaciones con variables categóricas
        if len(self.datosCompletos.select_dtypes(include='object').columns.to_list())>0:
            self.datosObj=pd.read_csv(ruta_dfObject)
            #Resumen estadístico variables categóricas
            self.showDescribeObj()
            #Histograma de variables categóricas
            self.HistogramaCat=HistogramaCat()
            self.box3.addWidget(self.HistogramaCat)
        #Mostrar matriz de correlaciones
        self.showCorr()
        #Mapa de calor
        self.heatMap=heatMap()
        self.box4.addWidget(self.heatMap)
        
        #Botón menú variables
        #self.botonSelecVariables.setFixedWidth(140)
        for indice, columna in enumerate(tuple(self.datos.columns), start=0):
            accion = QAction(columna, self.menu)
            accion.setCheckable(True)
            accion.setChecked(False)
            accion.setData(columna)
            self.menu.addAction(accion)
            
            
        
        
        
        
    def mostrarBigotes(self, accion):
        columna = accion.data()
        if accion.isChecked():
            print("Si genero grafica de caja {}".format(str(columna)))
            
            varBox.append(str(columna))
        else:
            print("No genero grafica de caja {}".format(str(columna)))
            varBox.remove(str(columna))
        print(varBox)
        self.Bigotes=Bigotes()
        
        for i in reversed(range(self.box2.count())):
            self.box2.itemAt(i).widget().setParent(None)
        self.box2.addWidget(self.Bigotes)
        
    def showDescribe(self):
        self.describeDatos=pd.concat([self.estadisticos,self.datos.describe()], axis=1) #axis=1 une un df a lado del otro
        self.describeDatos["Estadisticos"]=self.describeDatos.index.to_list()
        self.describeTable.setColumnCount(len(self.describeDatos.columns))
        self.describeTable.setRowCount(len(self.describeDatos))
        self.describeTable.setHorizontalHeaderLabels(self.describeDatos.columns)
        #Llenado de datos en tabla
        for i in range(len(self.describeDatos)):
            for j in range(len(self.describeDatos.columns)):
                self.describeTable.setItem(i,j,QtWidgets.QTableWidgetItem(str(self.describeDatos.iat[i,j])))
    def showDescribeObj(self):
        self.describeDatosObj=pd.concat([self.estadisticos2,self.datosObj.describe()], axis=1) #axis=1 une un df a lado del otro
        self.describeDatosObj["Estadisticos"]=self.describeDatosObj.index.to_list()
        self.describeTable2.setColumnCount(len(self.describeDatosObj.columns))
        self.describeTable2.setRowCount(len(self.describeDatosObj))
        self.describeTable2.setHorizontalHeaderLabels(self.describeDatosObj.columns)
        #Llenado de datos en tabla
        for i in range(len(self.describeDatosObj)):
            for j in range(len(self.describeDatosObj.columns)):
                self.describeTable2.setItem(i,j,QtWidgets.QTableWidgetItem(str(self.describeDatosObj.iat[i,j])))
    
    def showCorr(self):
        dfAux=pd.DataFrame({"Variables" : self.datos .columns.to_list() })
        dfAux.index=self.datos.columns.to_list()
        self.matrizCorr=pd.concat([dfAux,self.datos.corr()], axis=1) #axis=1 une un df a lado del otro
        self.matrizCorr["Variables"]=list(self.datos.columns)
        self.describeTable3.setColumnCount(len(self.matrizCorr.columns))
        self.describeTable3.setRowCount(len(self.matrizCorr))
        self.describeTable3.setHorizontalHeaderLabels(self.matrizCorr.columns)
        #Llenado de datos en tabla
        for i in range(len(self.matrizCorr)):
            for j in range(len(self.matrizCorr.columns)):
                self.describeTable3.setItem(i,j,QtWidgets.QTableWidgetItem(str(self.matrizCorr.iat[i,j])))
        
        
    
    def limpiar(self):
        for i in reversed(range(self.box.count())):
            self.box.itemAt(i).widget().setParent(None)
        self.describeTable.clearContents()
        self.describeTable.setRowCount(0)
        self.describeTable2.clearContents()
        self.describeTable2.setRowCount(0)
        self.describeTable3.clearContents()
        self.describeTable3.setRowCount(0)
        for i in reversed(range(self.box2.count())):
            self.box2.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.box3.count())):
            self.box3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.box4.count())):
            self.box4.itemAt(i).widget().setParent(None)
        #Limpiando el menú de selección de variables
        self.menu.clear()
        #Vaciar lista de variables
        varBox.clear()
        
        
# ======================= CLASES PARA GRÁFICACIÓN ============================   

class heatMap(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.axs=plt.subplots(nrows=1, ncols=1, sharey=False, figsize=[14,14], clear=True) 
        super().__init__(self.fig)
        self.datos=pd.read_csv(ruta_dfNumericos)
        self.matrizCorr=self.datos.corr()
        matrizInf=np.triu(self.matrizCorr)
        sns.heatmap(ax=self.axs,data=self.datos.corr(), cmap='RdBu_r', annot=True, mask=matrizInf)
        self.fig.suptitle("Mapa de Calor - Matriz de Correlaciones")
        
class Bigotes(FigureCanvas):
    def __init__(self, parent=None):
        self.datos=pd.read_csv(ruta_dfNumericos)
        copy_df=pd.DataFrame()
        variables=len(varBox)
        for i in varBox:
            copy_df=pd.concat([copy_df,self.datos[i]], axis=1)
        if variables%3 != 0:
            #Numero de variables no es multiplo de 3
            renglones=math.ceil(variables/3)
        else:
            #El número de variables si es multiplo de 3
            renglones=variables//3
       
        if variables>0:
            self.fig, self.axs = plt.subplots(nrows=renglones, ncols=3, sharey=False, tight_layout=True, clear=True) 
            super().__init__(self.fig)
            self.fig.subplots_adjust(hspace=0.3, wspace=0.3)
        #Generación de histogramas
        aux=0
        if 0< variables <= 3:
            for i in range(variables):
                self.axs[i].boxplot(x=varBox[aux],data=self.datos)
                self.axs[i].set_title(varBox[aux])
                self.axs[i].yaxis.set_major_formatter(ScalarFormatter())
                aux+=1
        elif variables == 0:
            print("Se limpia el box")
            self.fig, self.axs = plt.subplots(nrows=1, ncols=3, sharey=False, tight_layout=True, clear=True) 
            super().__init__(self.fig)
            self.fig.subplots_adjust(hspace=0.3, wspace=0.3)
        else:
            for i in range(renglones):
                for j in range(3):
                    if aux <= len(varBox)-1:
                        self.axs[i,j].boxplot(x=varBox[aux],data=self.datos)
                        self.axs[i,j].set_title(varBox[aux])
                        self.axs[i,j].yaxis.set_major_formatter(ScalarFormatter())
                        aux+=1
                    else:
                        break
        
class Histograma(FigureCanvas):
    def __init__(self, parent=None):
        self.datos=pd.read_csv(ruta_dfNumericos)
        variables=len(self.datos.columns)
        columnas=list(self.datos.columns)
        if variables%3 != 0:
            #Numero de variables no es multiplo de 3
            renglones=math.ceil(variables/3)
        else:
            #El número de variables si es multiplo de 3
            renglones=variables//3
       
        self.fig, self.axs = plt.subplots(nrows=renglones, ncols=3, sharey=False, tight_layout=True, clear=True) 
        super().__init__(self.fig)
        self.fig.subplots_adjust(hspace=0.3, wspace=0.3)
        
        #Generación de histogramas
        aux=0
        for i in range(renglones):
            for j in range(3):
                if aux <= len(columnas)-1:
                    self.axs[i,j].hist(self.datos[columnas[aux]])
                    self.axs[i,j].set_title(columnas[aux])
                    self.axs[i,j].yaxis.set_major_formatter(ScalarFormatter())
                    aux+=1
                else:
                    break
                
class HistogramaCat(FigureCanvas):
    def __init__(self, parent=None):
        self.datos=pd.read_csv(ruta_dfObject)
        variables=len(self.datos.columns)
        columnas=[]
        #Encontrar variables 
        for col in self.datos.select_dtypes(include='object'):
            if self.datos[col].nunique()<10:
                columnas.append(col)
        variables=len(columnas)
        copy_df=pd.DataFrame()
        for i in columnas:
            copy_df=pd.concat([copy_df,self.datos[i]], axis=1)
        if variables%3 != 0:
            #Numero de variables no es multiplo de 3
            renglones=math.ceil(variables/3)
        else:
            #El número de variables si es multiplo de 3
            renglones=variables//3
        if renglones>0:
            self.fig, self.axs = plt.subplots(nrows=renglones, ncols=3, sharey=False, tight_layout=True, clear=True)
        else:
            self.fig, self.axs = plt.subplots(nrows=1, ncols=3, sharey=False, tight_layout=True, clear=True)
        super().__init__(self.fig)
        self.fig.subplots_adjust(hspace=2, wspace=2)
        clases=[]
        counts=[]
        colores=[]
        aux=0
        if 0<variables<=3:
            for i in range(variables):
                clases=list(self.datos[columnas[aux]].unique())
                counts=list(self.datos[columnas[aux]].value_counts(sort=False))
                for w in range(len(clases)):
                    color = [round(random.uniform(0.0,1.0),2) for i in range(0,3)]
                    colores.append(color)
                y_pos=list(range(len(clases)))
                self.axs[i].barh(y_pos, counts, align='center', color=colores)
                self.axs[i].set_yticks(y_pos, labels=clases)
                self.axs[i].set_title(columnas[aux])
                self.axs[i].invert_yaxis()
                self.axs[i].xaxis.set_major_formatter(ScalarFormatter())
                colores=[]
                aux+=1
        elif variables == 0:
            print("Se limpia el box")
            self.fig, self.axs = plt.subplots(nrows=1, ncols=3, sharey=False, tight_layout=True, clear=True) 
            self.fig.subplots_adjust(hspace=0.3, wspace=0.3)
        else:
            for i in range(renglones):
                for j in range(3):
                    if aux <= len(columnas)-1:
                        sns.countplot(ax=self.axs[i,j],y=columnas[aux], data=self.datos)
                        self.axs[i,j].set_title(columnas[aux])
                        colores=[]
                        aux+=1    
        
