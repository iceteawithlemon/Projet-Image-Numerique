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

		self.actionSauvegarder_Sous.triggered.connect(self.saveAsImage)
		self.actionSauvegarder.triggered.connect(self.save)

		self.actionNiveaux_de_gris.triggered.connect(self.NiveauxDeGris)
		self.actionBinarisation.triggered.connect(self.Binarisation)
		self.actionLUT.triggered.connect(self.LUT)

		self.actionFiltre_Gaussien.triggered.connect(self.gaussien)
		self.actionFiltre_Median.triggered.connect(self.median)
		self.actionFiltre_Moyenneur.triggered.connect(self.moyenneur)

		self.actionSobel.triggered.connect(self.sobel)
		self.actionPrewitt.triggered.connect(self.prewitt)
		self.actionLaplacien.triggered.connect(self.laplacien)
		
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
			if ext == 'PPM':
				self.ppm.lirePPM(fileName)
				self.fileType = ext
				#self.ppm.afficher()
			elif ext == 'PGM':
				self.pgm.lirePGM(fileName)
				self.fileType = ext
				#self.pgm.afficher()
			else:
				QtGui.QMessageBox.about(self, "Erreur", "Format fichier incorrect.")

	def openImageName(self, name):
		self.image_area.setPixmap(QtGui.QPixmap(fileName))

	def refresh(self):
		fileName = "tmp_file_for_refresh"
		self.saveImage(fileName)
		self.image_area.setPixmap(QtGui.QPixmap(fileName))
		os.remove(fileName)

	def save(self):
		ext = str(self.fileType).upper()
		if ext == 'PPM':
			fileName = self.ppm.fileName
		elif ext == 'PGM':
			fileName = self.pgm.fileName
		self.saveImage(fileName)

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


	def getValue(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Taille du filtre: ')
		if ok:
				try: val = int(text)
				except:
					QtGui.QMessageBox.about(self, "Erreur", "Ce valeur n'est pas un nombre: veuillez entrer un nombre impair.")
				if val%2 == 1:
					return val
				else:
					QtGui.QMessageBox.about(self, "Erreur", "Ce valeur n'est pas impair: veuillez entrer un nombre impair.")

	def miroirHorizontal(self):
		self.check()
		self.pgm.miroir_horizontal()
		self.refresh()

	def miroirVertical(self):
		self.check()
		self.pgm.miroir_vertical()
		self.refresh()

	def NiveauxDeGris(self):
		self.pgm = self.ppm.PPMtoPGM()
		self.fileType = 'PGM'
		self.refresh()

	def Binarisation(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Seuil: ')
		if ok:
			try: val = int(text)
			except:
				QtGui.QMessageBox.about(self, "Erreur", "Ce valeur n'est pas un nombre.")
		if val:
			self.check()
			self.pgm.binarisation(val)
			self.refresh()

	def LUT(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Seuil: ')
		if ok:
			try: val = int(text)
			except:
				QtGui.QMessageBox.about(self, "Erreur", "Ce valeur n'est pas un nombre.")
		if val:
			self.check()
			self.pgm.LUT(val)
			self.refresh()
				
	def sobel(self):
		self.check()
		self.pgm.dcSobel()
		self.refresh()

	def laplacien(self):
		self.check()
		self.pgm.dcLaplacien()
		self.refresh()

	def prewitt(self):
		self.check()
		self.pgm.dcPrewitt()
		self.refresh()

	def gaussien(self):
		self.check()
		taille = self.getValue()
		self.pgm.gaussien(taille)
		self.refresh()

	def check(self):
		ext = str(self.fileType).upper()
		if ext == 'PPM':
			self.NiveauxDeGris()

	def median(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Taille: ')
		if ok:
			try: val = int(text)
			except:
				QtGui.QMessageBox.about(self, "Erreur", "Ce valeur n'est pas un nombre.")
		if val:
			self.check()
			self.pgm.median(val)
			self.refresh()

	def moyenneur(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Taille: ')
		if ok:
			try: val = int(text)
			except:
				QtGui.QMessageBox.about(self, "Erreur", "Ce valeur n'est pas un nombre.")
		if val:
			self.check()
			self.pgm.moyenneur(val)
			self.refresh()





	def main(self):
		self.show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	imageViewer = ImageViewer()
	imageViewer.main()
	app.exec_()