import sys, os, inspect
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5 import uic
directory = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
sys.path.append(directory + "/lib")
from bbdd import Bbdd
from func_aux import str_to_float
from facturas_gasto import FacturasGasto

class NuevaFacturaGasto(QWidget):
    def __init__(self, mainWindows, id):
        QWidget.__init__(self)
        uic.loadUi(directory + "/../ui/nueva_factura.ui", self)
        self.mainWindows = mainWindows
        self.id = id
        self.btnAceptar.clicked.connect(self.accept)
        self.btnCancelar.clicked.connect(self.cancel)
        bd = Bbdd()
        self.nombre = bd.select("gasto", None, "id=" + str(self.id), "name")[0][0]
        bd.close()
        self.mainWindows.setWindowTitle("Nueva Factura para " + self.nombre + " | Arroyo v" + mainWindows.version)

    def close(self):
            self.mainWindows.setCentralWidget(FacturasGasto(self.mainWindows, self.id))

    def cancel(self):
        self.close()

    def accept(self):
        data = [str(self.id), self.txtOrden.text(), self.txtFecha.date().toPyDate(),
                str(str_to_float(self.txtImporte.text()))]
        columns = ["gasto", "n_orden", "fecha", "importe"]

        bbdd = Bbdd()
        bbdd.insert(columns, data, "factura_gasto")
        bbdd.close()

        QMessageBox.information(self, "Añadido", "Nueva factura para " + self.nombre + ".")

        self.close()

