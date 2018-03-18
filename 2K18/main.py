import os
import interface
from PyQt4 import*
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import time
import threading
try:
	import qdarkstyle
	os.system("clear")
except:
	print "Dark Stylesheet not found. Installing it..."
	os.system("clr")
	os.system("pip install qdarkstyle")

import sys




class App(QtGui.QMainWindow, interface.Ui_MainWindow):
	def __init__(self, parent = None):
		super(App, self).__init__(parent)
		self.setupUi(self)
	



def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
    form = App()
    form.show()
    app.exec_()



main()

