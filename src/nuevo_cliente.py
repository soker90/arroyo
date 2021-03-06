import sys, os, inspect
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5 import uic
directory = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
sys.path.append(directory + "/lib")
from bbdd import Bbdd
from clientes import Clientes

class NuevoCliente(QWidget):
    def __init__(self, mainWindows):
        QWidget.__init__(self)
        uic.loadUi(directory + "/../ui/nuevo_cliente.ui", self)
        self.mainWindows = mainWindows
        self.btnAceptar.clicked.connect(self.accept)
        self.btnCancelar.clicked.connect(self.cancel)
        self.mainWindows.setWindowTitle("Nuevo Cliente | Arroyo v" + mainWindows.version)
        self.txtNombre.returnPressed.connect(self.btnAceptar.click)

    def close(self):
            self.mainWindows.setCentralWidget(Clientes(self.mainWindows))

    def cancel(self):
        self.close()

    def accept(self):
        data = [self.txtNombre.text()]
        columns = ["name"]

        bbdd = Bbdd()
        bbdd.insert(columns, data, "cliente")
        bbdd.close()

        QMessageBox.information(self, "Añadido", "Nuevo cliente añadido.")

        self.close()

