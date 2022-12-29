from PyQt5.QtWidgets import (QAbstractItemView, QMenu,
                             QAction, QWidget)
from PyQt5.QtCore import Qt
from PyQt5 import  QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import math
from matplotlib.ticker import ScalarFormatter
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler 

from ui.pages.ACP_window_ui import Ui_Form

#Global variable
ruta_buf="buf/"
ruta_dfObject=ruta_buf+"datosObject.csv"
ruta_dfNumericos=ruta_buf+"datosNumericos.csv"
ruta_dfCompleto=ruta_buf+"datos.csv"
ruta_dfEstandarizado=ruta_buf+"datosNumericosTratados.csv"
ruta_dfEstandarizadoCopy=ruta_buf+"datosNumericosTratadosCopy.csv"
varBox=[]
varBox2=[]

#Modelo
pca = PCA(n_components=None)     # pca=PCA(n_components=None), pca=PCA(.85)

#Tabla de datos final
datosNumericosTratados=pd.DataFrame()
datosNumericosTratadosCopy=pd.DataFrame() #para la parte de eliminación de datos
matrizCovarianzas=pd.DataFrame()
class ACP(QWidget):
    def __init__(self):
        super(ACP, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ##Variables 
        self.datos=pd.DataFrame()
        
        # =================== WIDGETS QVBOXLAYOUT & QPUSHBUTTON ==================
        
        #       *** QvBoxLayout ***
        self.box=self.ui.box
        self.box2=self.ui.box2
        self.propVartextEdit=self.ui.propVartextEdit
        self.numCP=self.ui.numCP
        self.relevancia=self.ui.relevancia
        self.menu=QMenu()
            
        #       *** QPushButton ***
        self.actualizarBoton=self.ui.actualizarButton
        self.limpiarBoton=self.ui.limpiarButton 
        self.varAcButton=self.ui.varAcButton
        self.eliminarVarBotons=self.ui.eliminarVarBoton
        self.eliminarVarBotons.setMenu(self.menu)
        
        # ================== WIDGET  QTableWidget ==================
        #       *** Tabla para resumen estadístico de variables numéricas
        self.estandarTable= self.ui.estandarTable
        #   Configuración de tabla
        #self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.estandarTable.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.estandarTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.estandarTable.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.estandarTable.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.estandarTable.setWordWrap(False)
        # Deshabilitar clasificación
        self.estandarTable.setSortingEnabled(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.estandarTable.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupe todo el espacio disponible
        #self.estandarTable.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.estandarTable.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.estandarTable.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.estandarTable.verticalHeader().setDefaultSectionSize(20)
        
        #          *** Tabla para resumen estadístico de variables categóricas
        self.covTable= self.ui.covTable
        #   Configuración de tabla
        #self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.covTable.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.covTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.covTable.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.covTable.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.covTable.setWordWrap(False)
        # Deshabilitar clasificación
        self.covTable.setSortingEnabled(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.covTable.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupe todo el espacio disponible
        #self.describeTable.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.covTable.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.covTable.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.covTable.verticalHeader().setDefaultSectionSize(20)
        
        #          *** Tabla para matriz de correlaciones
        self.relevanciasTable= self.ui.relevanciasTable
        #   Configuración de tabla
        #self.relevanciasTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.relevanciasTable.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.relevanciasTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.relevanciasTable.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.relevanciasTable.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.relevanciasTable.setWordWrap(False)
        # Deshabilitar clasificación
        self.relevanciasTable.setSortingEnabled(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.relevanciasTable.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupe todo el espacio disponible
        #self.relevanciasTable.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.relevanciasTable.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.relevanciasTable.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.relevanciasTable.verticalHeader().setDefaultSectionSize(20)
        
        #          *** Tabla para datos finales
        self.datosFinalTable= self.ui.datosFinalTable
        #   Configuración de tabla
        #self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Deshabilitar el comportamiento de arrastrar y soltar
        self.datosFinalTable.setDragDropOverwriteMode(False)
        # Seleccionar toda la fila
        self.datosFinalTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.datosFinalTable.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.datosFinalTable.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabras del texto 
        self.datosFinalTable.setWordWrap(False)
        # Deshabilitar clasificación
        self.datosFinalTable.setSortingEnabled(False)
        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.datosFinalTable.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupe todo el espacio disponible
        #self.describeTable.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        self.datosFinalTable.verticalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.datosFinalTable.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.datosFinalTable.verticalHeader().setDefaultSectionSize(20)
        
        # =================== VARIABLES PROPÓSITO GENERAL ==================
        
        self.datosPuros=pd.DataFrame()
        self.datosEstandarizados=pd.DataFrame()
        self.describeDatosObj=pd.DataFrame()
        self.matrizCorr=pd.DataFrame()
        self.datosEstandarizados=pd.DataFrame()
        self.matrizCovarianzas=pd.DataFrame()
        self.estadisticos=pd.DataFrame({"Estadisticos" : ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']})
        self.estadisticos.index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
        self.estadisticos2=pd.DataFrame({"Estadisticos" : ['count', 'unique', 'top', 'freq']})
        self.estadisticos2.index=['count', 'unique', 'top', 'freq']

         # ======================== EVENTOS =========================
        self.actualizarBoton.clicked.connect(self.generarGrafica)
        self.varAcButton.clicked.connect(self.calculaVarAc)
        self.limpiarBoton.clicked.connect(self.limpiar)
        self.menu.triggered.connect(self.eliminarVariables)
        
        
    # ======================= FUNCIONES ============================    
    
    def generarGrafica(self):
        self.limpiar()
        self.datos=pd.read_csv(ruta_dfNumericos)
        self.datosCompletos=pd.read_csv(ruta_dfCompleto)
        #Mapa de calor Variables numericas
        self.heatMap=heatMap()
        self.box.addWidget(self.heatMap)
        #Resumen estadístico variables numéricas
        self.estandarizarDatos()
        #Matriz de covarianzas
        self.calcularMatrizCov()
        self.showDatosFinales()

        #Botón menú variables
        #self.botonSelecVariables.setFixedWidth(140)
        for indice, columna in enumerate(tuple(self.datos.columns), start=0):
            accion = QAction(columna, self.menu)
            accion.setCheckable(True)
            accion.setChecked(False)
            accion.setData(columna)
            self.menu.addAction(accion)
    
    def showDatosFinales(self):
        self.datosFinalTable.clearContents()
        datosNumericosTratados=pd.read_csv(ruta_dfEstandarizado)
        self.datosFinalTable.setColumnCount(len(datosNumericosTratados.columns))
        self.datosFinalTable.setRowCount(len(datosNumericosTratados))
        self.datosFinalTable.setHorizontalHeaderLabels(datosNumericosTratados.columns)
        #Llenado de datos en tabla
        for i in range(len(datosNumericosTratados)):
            for j in range(len(datosNumericosTratados.columns)):
                self.datosFinalTable.setItem(i,j,QtWidgets.QTableWidgetItem(str(datosNumericosTratados.iat[i,j])))
        
    def calculaVarAc(self):
        print("Función para calcular covar")
        #Obtener valor numético de usuario
        numComponenetes=int(self.numCP.toPlainText())
        if 0<numComponenetes<len(self.varianza):
            self.relevancia.setText(str(round(sum(self.varianza[0:numComponenetes])*100,2)))
        else:
            self.numCP.setText(str(len(self.varianza)-1))
            self.relevancia.setText(str(round(sum(self.varianza[0:numComponenetes])*100,2)))
            
    def eliminarVariables(self, accion):
        columna = accion.data()
        datosNumericosTratados=pd.read_csv(ruta_dfEstandarizadoCopy)
        if accion.isChecked():
            print("Si genero grafica de caja {}".format(str(columna)))
            varBox.append(str(columna))
        else:
            print("No genero grafica de caja {}".format(str(columna)))
            varBox.remove(str(columna))
        
        print("Voy a eliminar las siguientes variables {}".format(varBox))
        #Segmento de código para eliminar variables seleccionadas
        if len(varBox)>0:
            datosNumericosTratadosCopy=datosNumericosTratados.drop(columns=varBox)
        else:
            datosNumericosTratadosCopy=datosNumericosTratados
        datosNumericosTratadosCopy.to_csv(ruta_dfEstandarizado, index=False)
        self.showDatosFinales()
    def calcularMatrizCov(self):
        
        pca.fit(self.MEstandarizada)          # Se obtiene los componentes
        matrizCovarianzas=pd.DataFrame(pca.components_,columns=self.datosEstandarizados.columns.to_list())
        self.covTable.setColumnCount(len(matrizCovarianzas.columns))
        self.covTable.setRowCount(len(matrizCovarianzas))
        self.covTable.setHorizontalHeaderLabels(matrizCovarianzas.columns)
        #Llenado de datos en tabla
        for i in range(len(matrizCovarianzas)):
            for j in range(len(matrizCovarianzas.columns)):
                self.covTable.setItem(i,j,QtWidgets.QTableWidgetItem(str(matrizCovarianzas.iat[i,j])))
                
        #Se coloca la proporción de varianza acumulada
        self.varianza=pca.explained_variance_ratio_
        self.propVartextEdit.setText(str(list(self.varianza)))
        
        #Genera y muestra gráfica de varianza acumulada
        self.grafVarAc=grafVarAc()
        self.box2.addWidget(self.grafVarAc)
        
        #Se muestra matriz de proporción de relevancias
        self.CargasComponentes=pd.DataFrame(abs(pca.components_), columns=self.datosEstandarizados.columns)
        self.relevanciasTable.setColumnCount(len(self.CargasComponentes.columns))
        self.relevanciasTable.setRowCount(len(self.CargasComponentes))
        self.relevanciasTable.setHorizontalHeaderLabels(self.CargasComponentes.columns)
        #Llenado de datos en tabla
        for i in range(len(self.CargasComponentes)):
            for j in range(len(self.CargasComponentes.columns)):
                self.relevanciasTable.setItem(i,j,QtWidgets.QTableWidgetItem(str(self.CargasComponentes.iat[i,j])))
        
    def estandarizarDatos(self):
        Estandarizar = StandardScaler()
        self.datos=self.datos.dropna()
        self.MEstandarizada=Estandarizar.fit_transform(self.datos)
        self.datosEstandarizados=pd.DataFrame(self.MEstandarizada,columns=self.datos.columns)
        self.estandarTable.setColumnCount(len(self.datosEstandarizados.columns))
        self.estandarTable.setRowCount(len(self.datosEstandarizados))
        self.estandarTable.setHorizontalHeaderLabels(self.datosEstandarizados.columns)
        #Llenado de datos en tabla
        for i in range(len(self.datosEstandarizados)):
            for j in range(len(self.datosEstandarizados.columns)):
                self.estandarTable.setItem(i,j,QtWidgets.QTableWidgetItem(str(self.datosEstandarizados.iat[i,j])))
                
        self.datosEstandarizados.to_csv(ruta_dfEstandarizado, index=False)
        self.datosEstandarizados.to_csv(ruta_dfEstandarizadoCopy, index=False)
        
        
    
    def limpiar(self):
        for i in reversed(range(self.box.count())):
            self.box.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.box2.count())):
            self.box2.itemAt(i).widget().setParent(None)
        self.estandarTable.clearContents()
        self.estandarTable.setRowCount(0)
        self.covTable.clearContents()
        self.covTable.setRowCount(0)
        self.relevanciasTable.clearContents()
        self.relevanciasTable.setRowCount(0)
        self.datosFinalTable.clearContents()
        self.datosFinalTable.setRowCount(0)
        
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
        self.fig.suptitle("Matriz de Correlación")


class grafVarAc(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.axs = plt.subplots(nrows=1, ncols=1, sharey=False, tight_layout=True, clear=True) 
        super().__init__(self.fig)
        self.axs.plot(np.cumsum(pca.explained_variance_ratio_))
        self.axs.grid(True)
        self.axs.set_xlabel("Número de componentes")
        self.axs.set_ylabel("Varianza acumulada")
        self.fig.suptitle("Varianza Acumulada")
        
        
        
       
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
        
        