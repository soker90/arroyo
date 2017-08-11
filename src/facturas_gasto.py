import sys, os, inspect
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QMessageBox, QTreeWidget
from PyQt5.QtGui import QBrush, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5 import uic
directory = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
sys.path.append(directory + "/lib")
from bbdd import Bbdd


class FacturasGasto(QWidget):
	def __init__(self, mainWindows, id):
		QWidget.__init__(self)
		uic.loadUi(directory + "/../ui/facturas.ui", self)
		self.mainWindows = mainWindows
		self.id = id
		mainWindows.diconnectActions()
		mainWindows.aNuevo.triggered.connect(self.nuevaFactura)
		bd = Bbdd()
		nombre = bd.select("gasto", None, "id="+self.id, "name")[0][0]
		self.mainWindows.setWindowTitle("Facturas de " + nombre + " | Arroyo v" + mainWindows.version)
		bd.close()
		self.treeMain.header().hideSection(0)
		self.initTree()
		self.treeMain.itemSelectionChanged.connect(self.changeItem)
		self.mainWindows.aEditar.triggered.connect(self.editItem)

		self.itemSelected = -1

	def initTree(self):
		bd = Bbdd()
		data = bd.select("factura_gasto", "n_orden", "gasto=" + str(self.id))

		items = []
		for i in data:
			id = i[0]
			n_orden = i[2]
			fecha = i[3]
			importe = i[4]

			item = QTreeWidgetItem([str(id), str(n_orden), fecha, str(importe)])
			items.append(item)

		self.treeMain.addTopLevelItems(items)

		bd.close()

	def changeItem(self):
		self.itemSelected = self.treeMain.currentItem().text(0)
		self.mainWindows.enableActions()

	def editItem(self):
		self.mainWindows.editarFacturaG(self.id, self.itemSelected)

	def nuevaFactura(self):
		self.mainWindows.nuevaFacturaG(self.id)