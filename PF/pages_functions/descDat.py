from PyQt5.QtWidgets import QWidget
from ui.pages.descDat_window_ui import Ui_Form

import pandas as pd
ruta_buf="buf/"
ruta_archivo=ruta_buf+"datos.csv"

class descDat(QWidget):
    def __init__(self):
        super(descDat, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Define window objects
        self.dtypesLabel=self.ui.dtypesTextEdit
        self.dnullLabel=self.ui.dnullTextEdit
        self.update_button = self.ui.actualizarButton
        self.eliminar_button = self.ui.eliminarButton
        
        #Dataframes
        self.datosPuros=pd.DataFrame()
        self.datosSinNulos=pd.DataFrame()
        self.datosObject=pd.DataFrame()
        self.datosNumericos=pd.DataFrame()
        
        
        
        #Asociación de botones con funciones
        self.update_button.clicked.connect(self.infoDatos)
        self.eliminar_button.clicked.connect(self.eliminarNulos)
        

    def infoDatos(self):
        #Data frame de los datos
        self.datosPuros=pd.read_csv(ruta_archivo)
        self.dtypesLabel.setText(str(self.datosPuros.dtypes))
        self.dnullLabel.setText(str(self.datosPuros.isnull().sum()))
        
        #Se generan dos dataframes. Uno para variables numéricas y otro para categóricas
        self.datosObject=self.datosPuros.select_dtypes(include='object')
        self.datosNumericos=self.datosPuros.select_dtypes(exclude='object')
        self.datosObject.to_csv(ruta_buf+"datosObject.csv", index=False)
        self.datosNumericos.to_csv(ruta_buf+"datosNumericos.csv", index=False)
        
    def eliminarNulos(self):
        self.datosPuros=self.datosPuros.dropna()
        self.datosPuros.to_csv(ruta_buf+"datos.csv", index=False)
        self.datosNumericos=self.datosNumericos.dropna()
        self.datosNumericos.to_csv(ruta_buf+"datosNumericos.csv", index=False)
        self.datosObject=self.datosObject.dropna()
        self.datosObject.to_csv(ruta_buf+"datosObject.csv", index=False)
        self.dtypesLabel.setText(str(self.datosPuros.dtypes))
        self.dnullLabel.setText(str(self.datosPuros.isnull().sum()))