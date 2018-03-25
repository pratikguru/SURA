import os
import interface
from PyQt4 import*
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import time
import threading
import SocketServer
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
	
	def run(self):
		self.pbSet = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4]
		self.hSlider = [self.horizontalSlider, self.horizontalSlider_2, self.horizontalSlider_3, self.horizontalSlider_4]
		for x in range(0, 3):
			self.pbSet[x].reset()
			self.hSlider[x].setRange(0, 180)
		self.horizontalSlider.valueChanged.connect(self.openGripper)
		self.horizontalSlider_2.valueChanged.connect(self.rotateGripper)
		self.horizontalSlider_3.valueChanged.connect(self.panCamera)
		self.horizontalSlider_4.valueChanged.connect(self.lights)
		self.progressBar.setRange(0, 180)
		self.progressBar_2.setRange(0, 180)
		self.progressBar_3.setRange(0, 180)



	def openGripper(self, x):
		self.progressBar.setValue(x)
	def rotateGripper(self,x):
		self.progressBar_2.setValue(x)
	def panCamera(self, x):
		self.progressBar_3.setValue(x)
	def lights(self, x):
		self.progressBar_4.setValue(x)

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
    form = App()
    form.run()
    form.show()
    app.exec_()



main()

