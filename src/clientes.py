import sys, os, inspect
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QMessageBox, QTreeWidget
from PyQt5.QtGui import QBrush, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5 import uic
directory = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
sys.path.append(directory + "/lib")
from bbdd import Bbdd


class Clientes(QWidget):
	def __init__(self, mainWindows):
		QWidget.__init__(self)
		uic.loadUi(directory + "/../ui/clientes.ui", self)
		self.mainWindows = mainWindows
		mainWindows.diconnectActions()
		mainWindows.aNuevo.triggered.connect(mainWindows.nuevoCliente)
		self.mainWindows.setWindowTitle("Clientes | Arroyo v" + mainWindows.version)
		self.treeMain.header().hideSection(0)
		self.initTree()
		self.treeMain.itemSelectionChanged.connect(self.changeItem)
		self.mainWindows.aEditar.triggered.connect(self.editItem)
		self.mainWindows.aVer.triggered.connect(self.viewItem)

		self.itemSelected = -1

	def initTree(self):
		bd = Bbdd()
		data = bd.select("cliente", "name")

		items = []
		for i in data:
			id = i[0]
			nombre = i[1]

			item = QTreeWidgetItem([str(id), str(nombre)])
			items.append(item)

		self.treeMain.addTopLevelItems(items)

		bd.close()

	def changeItem(self):
		self.itemSelected = self.treeMain.currentItem().text(0)
		self.mainWindows.enableActions()

	def editItem(self):
		self.mainWindows.editarCliente(self.itemSelected)

	def viewItem(self):
		self.mainWindows.verCliente(self.itemSelected)
