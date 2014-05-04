# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun May 04 21:03:48 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.image_area = QtGui.QLabel(self.centralwidget)
        self.image_area.setText(_fromUtf8(""))
        self.image_area.setAlignment(QtCore.Qt.AlignCenter)
        self.image_area.setObjectName(_fromUtf8("image_area"))
        self.gridLayout.addWidget(self.image_area, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOuvrir = QtGui.QMenu(self.menubar)
        self.menuOuvrir.setObjectName(_fromUtf8("menuOuvrir"))
        self.menuFiltres = QtGui.QMenu(self.menubar)
        self.menuFiltres.setObjectName(_fromUtf8("menuFiltres"))
        self.menuD_tection_de_contours = QtGui.QMenu(self.menubar)
        self.menuD_tection_de_contours.setObjectName(_fromUtf8("menuD_tection_de_contours"))
        self.menuMiroirs = QtGui.QMenu(self.menubar)
        self.menuMiroirs.setObjectName(_fromUtf8("menuMiroirs"))
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
        self.actionFermer = QtGui.QAction(MainWindow)
        self.actionFermer.setObjectName(_fromUtf8("actionFermer"))
        self.actionFiltre_Gaussien = QtGui.QAction(MainWindow)
        self.actionFiltre_Gaussien.setObjectName(_fromUtf8("actionFiltre_Gaussien"))
        self.actionFiltre_Median = QtGui.QAction(MainWindow)
        self.actionFiltre_Median.setObjectName(_fromUtf8("actionFiltre_Median"))
        self.actionFiltre_Moyenneur = QtGui.QAction(MainWindow)
        self.actionFiltre_Moyenneur.setObjectName(_fromUtf8("actionFiltre_Moyenneur"))
        self.actionSauvegarder_Sous = QtGui.QAction(MainWindow)
        self.actionSauvegarder_Sous.setObjectName(_fromUtf8("actionSauvegarder_Sous"))
        self.actionSobel = QtGui.QAction(MainWindow)
        self.actionSobel.setObjectName(_fromUtf8("actionSobel"))
        self.actionPrewitt = QtGui.QAction(MainWindow)
        self.actionPrewitt.setObjectName(_fromUtf8("actionPrewitt"))
        self.actionLaplacien = QtGui.QAction(MainWindow)
        self.actionLaplacien.setObjectName(_fromUtf8("actionLaplacien"))
        self.actionHorizontal = QtGui.QAction(MainWindow)
        self.actionHorizontal.setObjectName(_fromUtf8("actionHorizontal"))
        self.actionVertical = QtGui.QAction(MainWindow)
        self.actionVertical.setObjectName(_fromUtf8("actionVertical"))
        self.actionLUT = QtGui.QAction(MainWindow)
        self.actionLUT.setObjectName(_fromUtf8("actionLUT"))
        self.actionNiveaux_de_gris = QtGui.QAction(MainWindow)
        self.actionNiveaux_de_gris.setObjectName(_fromUtf8("actionNiveaux_de_gris"))
        self.actionBinarisation = QtGui.QAction(MainWindow)
        self.actionBinarisation.setObjectName(_fromUtf8("actionBinarisation"))
        self.actionSauvegarder = QtGui.QAction(MainWindow)
        self.actionSauvegarder.setObjectName(_fromUtf8("actionSauvegarder"))
        self.menuOuvrir.addAction(self.actionOuvrir)
        self.menuOuvrir.addAction(self.actionFermer)
        self.menuOuvrir.addSeparator()
        self.menuOuvrir.addAction(self.actionSauvegarder)
        self.menuOuvrir.addAction(self.actionSauvegarder_Sous)
        self.menuFiltres.addAction(self.actionFiltre_Gaussien)
        self.menuFiltres.addAction(self.actionFiltre_Median)
        self.menuFiltres.addAction(self.actionFiltre_Moyenneur)
        self.menuFiltres.addSeparator()
        self.menuFiltres.addAction(self.actionLUT)
        self.menuFiltres.addSeparator()
        self.menuFiltres.addAction(self.actionNiveaux_de_gris)
        self.menuFiltres.addAction(self.actionBinarisation)
        self.menuD_tection_de_contours.addAction(self.actionSobel)
        self.menuD_tection_de_contours.addAction(self.actionPrewitt)
        self.menuD_tection_de_contours.addAction(self.actionLaplacien)
        self.menuMiroirs.addAction(self.actionHorizontal)
        self.menuMiroirs.addAction(self.actionVertical)
        self.menubar.addAction(self.menuOuvrir.menuAction())
        self.menubar.addAction(self.menuFiltres.menuAction())
        self.menubar.addAction(self.menuD_tection_de_contours.menuAction())
        self.menubar.addAction(self.menuMiroirs.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuOuvrir.setTitle(_translate("MainWindow", "Menu", None))
        self.menuFiltres.setTitle(_translate("MainWindow", "Filtres", None))
        self.menuD_tection_de_contours.setTitle(_translate("MainWindow", "Détection de contours", None))
        self.menuMiroirs.setTitle(_translate("MainWindow", "Miroirs", None))
        self.actionQuit.setText(_translate("MainWindow", "quit", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir", None))
        self.actionOuvrir.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionFermer.setText(_translate("MainWindow", "Fermer", None))
        self.actionFermer.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionFiltre_Gaussien.setText(_translate("MainWindow", "Filtre Gaussien", None))
        self.actionFiltre_Median.setText(_translate("MainWindow", "Filtre Median", None))
        self.actionFiltre_Moyenneur.setText(_translate("MainWindow", "Filtre Moyenneur", None))
        self.actionSauvegarder_Sous.setText(_translate("MainWindow", "Sauvegarder Sous", None))
        self.actionSauvegarder_Sous.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))
        self.actionSobel.setText(_translate("MainWindow", "Sobel", None))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt", None))
        self.actionLaplacien.setText(_translate("MainWindow", "Laplacien", None))
        self.actionHorizontal.setText(_translate("MainWindow", "Horizontal", None))
        self.actionVertical.setText(_translate("MainWindow", "Vertical", None))
        self.actionLUT.setText(_translate("MainWindow", "LUT", None))
        self.actionNiveaux_de_gris.setText(_translate("MainWindow", "Niveaux de gris", None))
        self.actionBinarisation.setText(_translate("MainWindow", "Binarisation", None))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder", None))
        self.actionSauvegarder.setShortcut(_translate("MainWindow", "Ctrl+S", None))

