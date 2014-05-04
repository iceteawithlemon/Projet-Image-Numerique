#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys, os
from Image import *

import gui

def getFileType(fileName):
	return fileName[len(fileName)-3:]


class ImageViewer(QtGui.QMainWindow, gui.Ui_MainWindow):
	fileType = "none"
	pgm = PGM()
	ppm = PPM()

	def __init__(self, parent = None):
		super(ImageViewer, self).__init__(parent)
		self.setupUi(self)
		self.connectActions()

	def connectActions(self):
		self.actionFermer.triggered.connect(QtGui.qApp.quit)
		self.actionOuvrir.triggered.connect(self.openImage)
		self.actionFiltre_Gaussien.triggered.connect(self.showDialog)
		self.actionSauvegarder_Sous.triggered.connect(self.saveAsImage)
		self.actionHorizontal.triggered.connect(self.miroirHorizontal)
		self.actionVertical.triggered.connect(self.miroirVertical)

	def openImage(self):
		fileName = QtGui.QFileDialog.getOpenFileName(
			self,
			"Ouvrir fichier image", QtCore.QDir.homePath(),
			 "Fichier Image NdG PGM ( *.pgm *.PGM);;Fichier Image Couleur PPM (*.ppm *.PPM)"
			)
		if fileName:
			self.image_area.setPixmap(QtGui.QPixmap(fileName))
			ext = str(getFileType(fileName))
			ext = ext.upper()
			print ext
			if ext == 'PPM':
				self.ppm.lirePPM(fileName)
				self.fileType = ext
				self.ppm.afficher()
			elif ext == 'PGM':
				self.pgm.lirePGM(fileName)
				self.fileType = ext
				self.pgm.afficher()
			else:
				QtGui.QMessageBox.about(self, "Erreur", "Format fichier incorrect.")

	def openImageName(self, name):
		self.image_area.setPixmap(QtGui.QPixmap(fileName))

	def refresh(self):
		fileName = "tmp_file_for_refresh"
		self.saveImage(fileName)
		self.image_area.setPixmap(QtGui.QPixmap(fileName))
		os.remove(fileName)

	def saveImage(self, fileName):
		ext = str(self.fileType).upper()
		if ext == 'PPM':
			self.ppm.ecrirePPM(fileName)
		elif ext == 'PGM':
			self.pgm.ecrirePGM(fileName)
		else:
			QtGui.QMessageBox.about(self, "Erreur", "Format fichier incorrect.")


	def saveAsImage(self):
		fileName = QtGui.QFileDialog.getSaveFileName(
			self,
			"Sauvegarder Sous", QtCore.QDir.homePath(),
			"Fichier Image NdG PGM ( *.pgm *.PGM);;Fichier Image Couleur PPM (*.ppm *.PPM)"
			)
		if fileName:
			self.saveImage(fileName)


	def showDialog(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Taille du filtre: ')
		if ok:
				try: val = int(text)
				except:
					QtGui.QMessageBox.about(self, "Erreur", "Ce valeur n'est pas un nombre: veuillez entrer un nombre impair.")
				if val%2 == 1:
					print text
				else:
					QtGui.QMessageBox.about(self, "Erreur", "Ce valeur n'est pas impair: veuillez entrer un nombre impair.")

	def miroirHorizontal(self):
		self.pgm.miroir_horizontal()
		self.refresh()

	def miroirVertical(self):
		self.pgm.miroir_vertical()
		self.refresh()


	def main(self):
		self.show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	imageViewer = ImageViewer()
	imageViewer.main()
	app.exec_()