from PyQt5.QtWidgets import (QAbstractItemView, QMenu,
                             QAction, QWidget)
from PyQt5.QtCore import Qt
from PyQt5 import  QtWidgets
from ui.pages.BACla_window_ui import Ui_Form
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
class BACla(QWidget):
    def __init__(self):
        super(BACla, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
