import inspect
import os
import sys

directory = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic
from PyQt5.Qt import QIcon
sys.path.append(directory)
from clientes import Clientes
from nuevo_cliente import NuevoCliente
from editar_cliente import EditarCliente
from proveedores import Proveedores
from nuevo_proveedor import NuevoProveedor
from editar_proveedor import EditarProveedor
from facturas_cliente import FacturasCliente
from nueva_factura_cliente import NuevaFacturaCliente
from editar_factura_cliente import EditarFacturaCliente
from facturas_proveedor import FacturasProveedor
from nueva_factura_proveedor import NuevaFacturaProveedor
from editar_factura_proveedor import EditarFacturaProveedor
from gastos import Gastos
from nuevo_gasto import NuevoGasto
from editar_gasto import EditarGasto
from facturas_gasto import FacturasGasto
from nueva_factura_gasto import NuevaFacturaGasto
from editar_factura_gasto import EditarFacturaGasto
from contabilidad import Contabilidad


class Main(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi(directory + "/../ui/wmain.ui", self)
		self.showMaximized()
		self.enableTools()
		self.setWindowIcon(QIcon(directory + "/../resources/logo.png"))

		archivo = open(directory+"/version.txt")
		self.version = archivo.readline()
		self.aClientes.triggered.connect(self.clientes)
		self.aProveedores.triggered.connect(self.proveedores)
		self.aGastos.triggered.connect(self.gastos)
		self.aContabilidad.triggered.connect(self.contabilidad)

		self.setCentralWidget(Proveedores(self))


	#ToolPrimary

	def proveedores(self):
		self.setCentralWidget(Proveedores(self))
		self.enableTools()

	def clientes(self):
		self.setCentralWidget(Clientes(self))
		self.enableTools()

	def gastos(self):
		self.setCentralWidget(Gastos(self))
		self.enableTools()

	def contabilidad(self):
		self.setCentralWidget(Contabilidad(self))
		self.toolSecondary.setVisible(False)

	# ToolSecundary
	# New Buttons

	def nuevoCliente(self):
		self.setCentralWidget(NuevoCliente(self))
		self.enableTools()

	def nuevoProveedor(self):
		self.setCentralWidget(NuevoProveedor(self))
		self.enableTools()

	def nuevoGasto(self):
		self.setCentralWidget(NuevoGasto(self))
		self.enableTools()

	# Edit Buttons

	def editarProveedor(self, id):
		self.setCentralWidget(EditarProveedor(self, id))
		self.enableTools()

	def editarCliente(self, id):
		self.setCentralWidget(EditarCliente(self, id))
		self.enableTools()

	def editarGasto(self, id):
		self.setCentralWidget(EditarGasto(self, id))
		self.enableTools()

	# Ver

	def verCliente(self, id):
		self.setCentralWidget(FacturasCliente(self, id))
		self.enableTools(False)

	def verProveedor(self, id):
		self.setCentralWidget(FacturasProveedor(self, id))
		self.enableTools(False)

	def verGasto(self, id):
		self.setCentralWidget(FacturasGasto(self, id))
		self.enableTools(False)

	# Nueva Factura

	def nuevaFacturaC(self, id):
		self.setCentralWidget(NuevaFacturaCliente(self, id))
		self.enableTools(False)

	def nuevaFacturaP(self, id):
		self.setCentralWidget(NuevaFacturaProveedor(self, id))
		self.enableTools(False)

	def nuevaFacturaG(self, id):
		self.setCentralWidget(NuevaFacturaGasto(self, id))
		self.enableTools(False)

	# Editar Factura

	def editarFacturaC(self, id_cliente, id):
		self.setCentralWidget(EditarFacturaCliente(self, id_cliente, id))
		self.enableTools(False)

	def editarFacturaP(self, id_proveedor, id):
		self.setCentralWidget(EditarFacturaProveedor(self, id_proveedor, id))
		self.enableTools(False)

	def editarFacturaG(self, id_gasto, id):
		self.setCentralWidget(EditarFacturaGasto(self, id_gasto, id))
		self.enableTools(False)

	#Auxiliary Functions

	def enableTools(self, ver=True):
		self.aEditar.setEnabled(False)
		self.toolSecondary.setVisible(True)
		if ver:
			self.aVer.setEnabled(False)
			self.aVer.setVisible(True)
		else:
			self.aVer.setVisible(False)
		#self.aEliminar.setEnabled(False)

	def enableActions(self, ver=True):
		self.aEditar.setEnabled(True)
		self.aVer.setEnabled(True)
		#self.aEliminar.setEnabled(True)

	def diconnectActions(self):
		try:
			self.aNuevo.triggered.disconnect()
		except:
			pass
		try:
			self.aEditar.triggered.disconnect()
		except:
			pass
		try:
			self.aVer.triggered.disconnect()
		except:
			pass


	#Events

	def closeEvent(self, event):
		resultado = QMessageBox.question(self, "Salir", "¿Seguro que quieres salir de la aplicación?",
										 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if resultado == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


	def about(self):
		about = About()
		about.exec_()

class About(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi(directory + "/../ui/about.ui", self)
		archivo = open(directory + "/version.txt")
		version = archivo.readline()
		self.setWindowTitle("Acerca de")
		self.txtText.setHtml("<p style='text-align: center;'><br>Arroyo v" + version + "<p/>" \
		                     "<p style='text-align: center;'>Web: https://github.com/soker90/arroyo/<p/>" \
		                     "<p style='text-align: center;'>Creado por Eduardo Parra Mazuecos<p/>" \
		                     "<p style='text-align: center;'>Contacto: eduparra90@gmail.com</p>" \
		                     "<p style='text-align: center;'>Licencia GPLv3<p/>")

