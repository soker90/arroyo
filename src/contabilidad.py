import sys, os, inspect
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QMessageBox, QTreeWidget
from PyQt5.QtGui import QBrush, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5 import uic
directory = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
sys.path.append(directory + "/lib")
from bbdd import Bbdd
from func_aux import paint_row


class Contabilidad(QWidget):
	def __init__(self, mainWindows):
		QWidget.__init__(self)
		uic.loadUi(directory + "/../ui/contabilidad.ui", self)
		self.mainWindows = mainWindows
		self.mainWindows.setWindowTitle("Contabilidad | Arroyo v" + mainWindows.version)
		self.anyo = 2017
		self.initTree()

		self.itemSelected = -1

	def initTree(self):
		bd = Bbdd()

		#Clientes
		total = [0, 0, 0, 0]
		datos = bd.executeQuery("SELECT id, (select sum(importe) FROM factura_cliente WHERE fecha between '" + \
		                        str(self.anyo) + "-01-01' and '" + str(self.anyo) + "-03-31' AND cliente = cliente.id)," \
		                        " (select sum(importe) FROM factura_cliente WHERE fecha between '" + str(self.anyo) + \
		                        "-04-01' and '" + str(self.anyo) + "-06-30' AND cliente = cliente.id), " \
		                        "(select sum(importe) FROM factura_cliente WHERE fecha between '" + str(self.anyo) + "-07-01' " \
		                        "and '" + str(self.anyo) + "-09-30' AND cliente = cliente.id), (select sum(importe) " \
		                        "FROM factura_cliente WHERE fecha between '" + str(self.anyo) + "-10-01' and '" + \
		                        str(self.anyo) + "-12-31' AND cliente = cliente.id) from cliente")

		items = []
		for i in datos:
			nombre = bd.getValue(i[0], "cliente")
			t1 = 0.0 if i[1] is None else i[1]
			t2 = 0.0 if i[2] is None else i[2]
			t3 = 0.0 if i[3] is None else i[3]
			t4 = 0.0 if i[4] is None else i[4]
			total[0] += t1
			total[1] += t2
			total[2] += t3
			total[3] += t4
			item = QTreeWidgetItem([nombre, str(t1) + "€", str(t2) + "€", str(t3) + "€", str(t4) + "€"])
			items.append(item)

		item = QTreeWidgetItem(["TOTAL", str(total[0]) + "€", str(total[1]) + "€", str(total[2]) + "€", str(total[3]) + "€"])
		items.append(paint_row(item))
		self.treeClientes.addTopLevelItems(items)

		# Proveedores
		total = [0, 0, 0, 0]
		datos = bd.executeQuery("SELECT id, (select sum(importe) FROM factura_proveedor WHERE fecha between '" + \
		                        str(self.anyo) + "-01-01' and '" + str(self.anyo) + "-03-31' AND proveedor = proveedor.id)," \
		                        " (select sum(importe) FROM factura_proveedor WHERE fecha between '" + str(self.anyo) + \
		                        "-04-01' and '" + str(self.anyo) + "-06-30' AND proveedor = proveedor.id), " \
		                        "(select sum(importe) FROM factura_proveedor WHERE fecha between '" + str(self.anyo) + "-07-01' " \
		                        "and '" + str(self.anyo) + "-09-30' AND proveedor = proveedor.id), (select sum(importe) " \
		                        "FROM factura_proveedor WHERE fecha between '" + str(self.anyo) + "-10-01' and '" + \
		                        str(self.anyo) + "-12-31' AND proveedor = proveedor.id) from proveedor")

		items = []
		for i in datos:
			nombre = bd.getValue(i[0], "proveedor")
			t1 = 0.0 if i[1] is None else i[1]
			t2 = 0.0 if i[2] is None else i[2]
			t3 = 0.0 if i[3] is None else i[3]
			t4 = 0.0 if i[4] is None else i[4]
			total[0] += t1
			total[1] += t2
			total[2] += t3
			total[3] += t4
			item = QTreeWidgetItem([nombre, str(t1) + "€", str(t2) + "€", str(t3) + "€", str(t4) + "€"])
			items.append(item)

		item = QTreeWidgetItem(["TOTAL", str(total[0]) + "€", str(total[1]) + "€", str(total[2]) + "€", str(total[3]) + "€"])
		items.append(paint_row(item))
		self.treeProveedores.addTopLevelItems(items)

		# Gastos
		total = [0, 0, 0, 0]
		datos = bd.executeQuery("SELECT id, (select sum(importe) FROM factura_gasto WHERE fecha between '" + \
		                        str(self.anyo) + "-01-01' and '" + str(self.anyo) + "-03-31' AND gasto = gasto.id)," \
		                        " (select sum(importe) FROM factura_gasto WHERE fecha between '" + str(self.anyo) + \
		                        "-04-01' and '" + str(self.anyo) + "-06-30' AND gasto = gasto.id), " \
		                        "(select sum(importe) FROM factura_gasto WHERE fecha between '" + str(self.anyo) + "-07-01' " \
		                        "and '" + str(self.anyo) + "-09-30' AND gasto = gasto.id), (select sum(importe) " \
		                        "FROM factura_gasto WHERE fecha between '" + str(self.anyo) + "-10-01' and '" + \
		                        str(self.anyo) + "-12-31' AND gasto = gasto.id) from gasto")

		items = []
		for i in datos:
			nombre = bd.getValue(i[0], "gasto")
			t1 = 0.0 if i[1] is None else i[1]
			t2 = 0.0 if i[2] is None else i[2]
			t3 = 0.0 if i[3] is None else i[3]
			t4 = 0.0 if i[4] is None else i[4]
			total[0] += t1
			total[1] += t2
			total[2] += t3
			total[3] += t4
			item = QTreeWidgetItem([nombre, str(t1) + "€", str(t2) + "€", str(t3) + "€", str(t4) + "€"])
			items.append(item)

		item = QTreeWidgetItem(["TOTAL", str(total[0]) + "€", str(total[1]) + "€", str(total[2]) + "€", str(total[3]) + "€"])
		items.append(paint_row(item))
		self.treeGastos.addTopLevelItems(items)

		bd.close()
