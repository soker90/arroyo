import sys, os, inspect
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5 import uic
directory = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
sys.path.append(directory + "/lib")
from bbdd import Bbdd
from gastos import Gastos

class EditarGasto(QWidget):
    def __init__(self, mainWindows, id):
        QWidget.__init__(self)
        uic.loadUi(directory + "/../ui/nuevo_cliente.ui", self)
        self.id = id
        self.mainWindows = mainWindows
        self.btnAceptar.clicked.connect(self.accept)
        self.btnCancelar.clicked.connect(self.cancel)
        self.mainWindows.setWindowTitle("Actualizar Gasto | Arroyo v" + mainWindows.version)
        self.txtNombre.returnPressed.connect(self.btnAceptar.click)

        self.initData()

    def initData(self):
        bd = Bbdd()

        nombre = bd.getValue(self.id, "gasto")
        self.txtNombre.setText(nombre)

        bd.close()

    def close(self):
            self.mainWindows.setCentralWidget(Gastos(self.mainWindows))

    def cancel(self):
        self.close()

    def accept(self):
        data = [self.txtNombre.text()]
        columns = ["name"]

        bbdd = Bbdd()
        bbdd.update(columns, data, "gasto", "id=" + str(self.id))
        bbdd.close()

        QMessageBox.information(self, "Añadido", "Gasto actualizado.")

        self.close()

