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
        print("agregar")
        

    @Slot()
    def mostrar_Particula(self):
        print("mostrar")