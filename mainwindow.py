from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particulas

# la clase mainwindow hereda lo de QMainWindow
class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.pushButton.clicked.connect(self.agregar_Particula)
        ui.pushButton_2.clicked.connect(self.mostrar_Particula)



    @Slot()
    def agregar_Particula(self):
        self.id = self.ui.txt_Id.text()
        self.origenX = self.ui.sbx_origenX.value()
        self.origenY = self.ui.sbx_origenY.value()
        self.destinoX = self.ui.sbx_destinoX.value()
        self.destinoY = self.ui.sbx.destinoY.value()
        self.velocidad = self.ui.sbx_velocidad.value()
        self.colorR = self.ui.sbx_colorR.value()
        self.colorG = self.ui.sbx_colorG.value()
        self.colorB = self.ui.sbx_colorB.value()
        

    @Slot()
    def mostrar_Particula(self):
        print("hola")