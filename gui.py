# -*- coding: utf-8 -*-

import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
import datetime

class ButtonBoxWidget(QtGui.QWidget):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent = parent)
		self.setup_ui()

	def setup_ui(self):
		self.start_button = QtGui.QPushButton("START", parent = self)
		self.score = QtGui.QLabel()


		layout = QtGui.QGridLayout()
		layout.addWidget(self.start_button,0,0)
		layout.addWidget(self.score,0,1)

		self.setLayout(layout)

	def start(self):
		self.score.setText(str(datetime.datetime.today()))


class GridWidget(QtGui.QWidget):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent = parent)
		self.setup_ui()

	def setup_ui(self):
		self.lb00 = QtGui.QLabel()
		self.lb01 = QtGui.QLabel()
		self.lb02 = QtGui.QLabel()
		self.lb03 = QtGui.QLabel()
		self.lb10 = QtGui.QLabel()
		self.lb11 = QtGui.QLabel()
		self.lb12 = QtGui.QLabel()
		self.lb13 = QtGui.QLabel()
		self.lb20 = QtGui.QLabel()
		self.lb21 = QtGui.QLabel()
		self.lb22 = QtGui.QLabel()
		self.lb23 = QtGui.QLabel()
		self.lb30 = QtGui.QLabel()
		self.lb31 = QtGui.QLabel()
		self.lb32 = QtGui.QLabel()
		self.lb33 = QtGui.QLabel()

		self.lb00.setText('4')
		self.lb01.setText('2')
		self.lb02.setText('2')
		self.lb03.setText('2')
		self.lb10.setText('2')
		self.lb11.setText('2')
		self.lb12.setText('4')
		self.lb13.setText('21')
		self.lb20.setText('4')
		self.lb21.setText('2')
		self.lb22.setText('2')
		self.lb23.setText('2')
		self.lb30.setText('2')
		self.lb31.setText('2')
		self.lb32.setText('4')
		self.lb33.setText('4')

		layout = QtGui.QGridLayout()
		layout.addWidget(self.lb00,0,0)
		layout.addWidget(self.lb01,0,1)
		layout.addWidget(self.lb02,0,2)
		layout.addWidget(self.lb03,0,3)
		layout.addWidget(self.lb10,1,0)
		layout.addWidget(self.lb11,1,1)
		layout.addWidget(self.lb12,1,2)
		layout.addWidget(self.lb13,1,3)
		layout.addWidget(self.lb20,2,0)
		layout.addWidget(self.lb21,2,1)
		layout.addWidget(self.lb22,2,2)
		layout.addWidget(self.lb23,2,3)
		layout.addWidget(self.lb30,3,0)
		layout.addWidget(self.lb31,3,1)
		layout.addWidget(self.lb32,3,2)
		layout.addWidget(self.lb33,3,3)

		self.setLayout(layout)

def start():
	app = QtGui.QApplication(sys.argv)

	panel = QtGui.QWidget()

	grid_widget = GridWidget(parent = panel)
	button_box_widget = ButtonBoxWidget(parent = panel)

	panel_layout = QtGui.QVBoxLayout()
	panel_layout.addWidget(grid_widget)
	panel_layout.addWidget(button_box_widget)
	panel.setLayout(panel_layout)
	panel.setFixedSize(320,400)

	main_window = QtGui.QMainWindow()
	main_window.setWindowTitle("noynelene2048")
	main_window.setCentralWidget(panel)

	main_window.show()

	button_box_widget.start_button.clicked.connect(button_box_widget.start)

	app.exec_()

if __name__ == "__main__":
	start()