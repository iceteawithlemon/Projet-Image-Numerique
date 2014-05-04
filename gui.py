# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sat May 03 17:40:35 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import sys 
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from scipy import *
from math import sqrt, pi, exp
from PIL import Image


LARGEUR = 256
HAUTEUR = 256
VAL_MAX = 255
VAL_MIN = 0




try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vue = QtGui.QGraphicsView(self.centralwidget) 
        self.vue.wheelEvent = self.wheel_event       
        self.gridLayout.addWidget(self.vue,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOuvrir = QtGui.QMenu(self.menubar)
        self.menuOuvrir.setObjectName(_fromUtf8("menuOuvrir"))
        self.menuFiltres = QtGui.QMenu(self.menubar)
        self.menuFiltres.setObjectName(_fromUtf8("menuFiltres"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOuvrir = QtGui.QAction(MainWindow)
        self.actionOuvrir.setObjectName(_fromUtf8("actionOuvrir"))
        self.actionSauvegarder = QtGui.QAction(MainWindow)
        self.actionSauvegarder.setObjectName(_fromUtf8("actionSauvegarder"))
        self.actionFermer = QtGui.QAction(MainWindow)
        self.actionFermer.setObjectName(_fromUtf8("actionFermer"))
        self.actionFiltre_Gaussien = QtGui.QAction(MainWindow)
        self.actionFiltre_Gaussien.setObjectName(_fromUtf8("actionFiltre_Gaussien"))
        self.actionFiltre_Median = QtGui.QAction(MainWindow)
        self.actionFiltre_Median.setObjectName(_fromUtf8("actionFiltre_Median"))
        self.actionFiltre_Moyenneur = QtGui.QAction(MainWindow)
        self.actionFiltre_Moyenneur.setObjectName(_fromUtf8("actionFiltre_Moyenneur"))
        self.actionLUT = QtGui.QAction(MainWindow)
        self.actionLUT.setObjectName(_fromUtf8("LUT"))
        self.menuOuvrir.addAction(self.actionOuvrir)
        self.menuOuvrir.addSeparator()
        self.menuOuvrir.addAction(self.actionSauvegarder)
        self.menuOuvrir.addSeparator()
        self.menuOuvrir.addAction(self.actionFermer)
        self.menuFiltres.addAction(self.actionFiltre_Gaussien)
        self.menuFiltres.addAction(self.actionFiltre_Median)
        self.menuFiltres.addAction(self.actionFiltre_Moyenneur)
        self.menuFiltres.addSeparator()
        self.menuFiltres.addAction(self.actionLUT)
        self.menubar.addAction(self.menuOuvrir.menuAction())
        self.menubar.addAction(self.menuFiltres.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connections
        self.actionOuvrir.triggered.connect(self.ouvrir)
        self.actionFermer.triggered.connect(MainWindow.close)
        self.actionFiltre_Gaussien.triggered.connect(self.gaussien)
        self.actionFiltre_Median.triggered.connect(self.median)
        self.actionFiltre_Moyenneur.triggered.connect(self.moyenneur)
        self.actionSauvegarder.triggered.connect(self.sauvegarder)
        self.actionLUT.triggered.connect(self.lut)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuOuvrir.setTitle(_translate("MainWindow", "Menu", None))
        self.menuFiltres.setTitle(_translate("MainWindow", "Filtres", None))
        self.actionQuit.setText(_translate("MainWindow", "quit", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir", None))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder", None))
        self.actionFermer.setText(_translate("MainWindow", "Fermer", None))
        self.actionFiltre_Gaussien.setText(_translate("MainWindow", "Filtre Gaussien", None))
        self.actionFiltre_Median.setText(_translate("MainWindow", "Filtre Median", None))
        self.actionFiltre_Moyenneur.setText(_translate("MainWindow", "Filtre Moyenneur", None))
        self.actionLUT.setText(_translate("MainWindow", "LUT", None))
    

    def wheel_event (self, event):
        steps = event.delta() / 120.0
        self.zoom(steps)
        event.accept()

    def zoom(self, step):
        w_pix, h_pix = self.pixmap.width(), self.pixmap.height()
        w, h = w_pix * (1 + 0.1*step), h_pix * (1 + 0.1*step)
        self.pixmap = QtGui.QPixmap.fromImage(self.current_image.scaled(w, h, 
                                            QtCore.Qt.KeepAspectRatio, 
                                            QtCore.Qt.FastTransformation))
        self.view_current()

    def ouvrir(self):
        fichier = QFileDialog.getOpenFileName(
                       MainWindow, 
                       "Ouvrir une image", 
                       "",
                       "Image Files (*.png *.gif *.jpg *.jpeg *.pgm)")
        if not fichier:
            return
        
        self.open_image(fichier)

    def open_image(self, path):
        w_vue, h_vue = self.vue.width(), self.vue.height() 
        self.current_image = QtGui.QImage(path)
        self.pixmap = QtGui.QPixmap.fromImage(self.current_image.scaled(w_vue, h_vue,
                                    QtCore.Qt.KeepAspectRatio, 
                                    QtCore.Qt.SmoothTransformation)) 
        self.view_current()

    def view_current(self):
        w_pix, h_pix = self.pixmap.width(), self.pixmap.height()
        self.scene = QtGui.QGraphicsScene()
        self.scene.setSceneRect(0, 0, w_pix, h_pix)
        self.scene.addPixmap(self.pixmap)
        self.vue.setScene(self.scene)

    def filtre_gaussien(taille, sigma = 1):
        offset = int(float(taille)/2)
        filtre = [[0 for x in range(0, taille)] for x in range(0, taille)]
        for x in range(-offset, offset+1):
                for y in range(-offset, offset+1):
                        filtre[x+offset][y+offset] =  1/(2*pi*sigma**2) * exp(-(x**2 + y**2)/(2*sigma**2))
        coef = 1/filtre[0][0]
        for x in range(0, taille):
                for y in range(0, taille):
                        filtre[x][y] = int(filtre[x][y] * coef)

        return filtre
        
    def gaussien(self):
        fichier = QFileDialog.getOpenFileName(
                       MainWindow, 
                       "Ouvrir une image", 
                       "",
                       "Image Files (*.png *.gif *.jpg *.jpeg *.pgm)")
        if not fichier:
            return
        self.filtre_gaussien(3,)
        self.view_current()

    def median(self):
        fichier = QFileDialog.getOpenFileName(
                       MainWindow, 
                       "Ouvrir une image", 
                       "",
                       "Image Files (*.png *.gif *.jpg *.jpeg *.pgm)")
        if not fichier:
            return
        self.filtre_median(fichier,1)
        self.view_current()
                            

    def filtre_median(src, offset):
        HAUTEUR = len(src)
        LARGEUR = len(src[0])
        dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
        for y in range(offset, HAUTEUR  - offset):
                for x in range(offset, LARGEUR - offset):
                        temp_vals = []
                        for i in range(-offset, offset):
                                for j in range(-offset, offset):
                                        temp_vals.append(src[x+i][y+j])
                        dest[x][y] = median_value(temp_vals)
        return dest

    def median_value(values):
        values.sort()
        l = int(len(values)/2)
        if len(values) %2 == 0:
                return (values[l] + values[l+1]) / 2
        return values[l]



    def filtre_moyenneur(taille):
        return [[1 for x in range(0, taille)] for x in range(0, taille)]

    def moyenneur(self):
        fichier = QFileDialog.getOpenFileName(
                       MainWindow, 
                       "Ouvrir une image", 
                       "",
                       "Image Files (*.png *.gif *.jpg *.jpeg *.pgm)")
        if not fichier:
            return
        self.filtre_moyenneur(3)
        self.view_current()

    def sauvegarder(self):
        fichier = QFileDialog.getSaveFileName(
            MainWindow, 
           "Enregistrer un fichier", 
            "", 
           "Images (*.png *.gif *.jpg *.jpeg *.pgm)")
        if not fichier:
            sys.stderr.write('ceci n est pas une extension image')

    def lut(self):
        fichier = QFileDialog.getOpenFileName(
                       MainWindow, 
                       "Ouvrir une image", 
                       "",
                       "Image Files (*.png *.gif *.jpg *.jpeg *.pgm)")
        if not fichier:
            return
        self.LUT_PGM(fichier,2)
        self.view_current()


    def check_level(pixel, level):
        val = pixel + level
        if(val < VAL_MIN):
                return VAL_MIN
        elif(val > VAL_MAX):
                return VAL_MAX
        else:
                return val

    def LUT_PGM(src, level):
        HAUTEUR = len(src)
        LARGEUR = len(src[0])
        dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
        for y in range(0, HAUTEUR):
                for x in range(0, LARGEUR):
                        dest[x][y] = check_level(src[x][y], level)
        return dest


if __name__ == "__main__": 
       
       app = QtGui.QApplication(sys.argv) 
       MainWindow = QtGui.QMainWindow() 
       ui = Ui_MainWindow()
       ui.setupUi(MainWindow) 
       MainWindow.show()   
       sys.exit(app.exec_())
