#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import Projet

import gui

class ImageViewer(QtGui.QMainWindow, gui.Ui_MainWindow):

	def __init__(self, parent = None):
		super(ImageViewer, self).__init__(parent)
		self.setupUi(self)
		self.connectActions()

	def connectActions(self):
		self.actionFermer.triggered.connect(QtGui.qApp.quit)
		self.actionOuvrir.triggered.connect(self.openImage)

	def openImage(self):
		fileName = QtGui.QFileDialog.getOpenFileName(
			self,
			"Ouvrir fichier image", QtCore.QDir.homePath(),
			"Image Files (*.jpg *.jpeg *.gif *.png)"
			)
		if fileName:
			self.image_area.setPixmap(QtGui.QPixmap(fileName))


	def main(self):
		self.show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	imageViewer = ImageViewer()
	imageViewer.main()
	app.exec_()