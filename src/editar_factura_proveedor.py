import sys, os, inspect
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5 import uic
from PyQt5.QtCore import QDate

directory = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
sys.path.append(directory + "/lib")
from bbdd import Bbdd
from func_aux import str_to_float
from facturas_proveedor import FacturasProveedor

class EditarFacturaProveedor(QWidget):
    def __init__(self, mainWindows, id_proveedor, id):
        QWidget.__init__(self)
        uic.loadUi(directory + "/../ui/nueva_factura.ui", self)
        self.mainWindows = mainWindows
        self.id = id
        self.id_proveedor= id_proveedor
        self.btnAceptar.clicked.connect(self.accept)
        self.btnCancelar.clicked.connect(self.cancel)
        bd = Bbdd()
        self.nombre = bd.select("proveedor", None, "id=" + str(self.id_proveedor), "name")[0][0]
        bd.close()
        self.mainWindows.setWindowTitle("Nueva Factura para " + self.nombre + " | Arroyo v" + mainWindows.version)
        self.initData()

    def initData(self):
        bd = Bbdd()
        data = bd.select("factura_proveedor", None, "id=" + str(self.id))[0]
        self.txtOrden.setValue(data[2])
        fecha = QDate.fromString(data[3], "yyyy-MM-dd")
        self.txtFecha.setDate(fecha)
        self.txtImporte.setValue(data[4])
        bd.close()

    def close(self):
            self.mainWindows.setCentralWidget(FacturasProveedor(self.mainWindows, self.id_proveedor))

    def cancel(self):
        self.close()

    def accept(self):
        data = [self.txtOrden.text(), self.txtFecha.date().toPyDate(),
                str(str_to_float(self.txtImporte.text()))]
        columns = ["n_orden", "fecha", "importe"]

        bbdd = Bbdd()
        bbdd.update(columns, data, "factura_proveedor", "id=" + str(self.id))
        bbdd.close()

        QMessageBox.information(self, "Añadido", "Factura de " + self.nombre + " actualizada.")

        self.close()

