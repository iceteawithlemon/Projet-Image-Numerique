# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sat May 03 17:40:35 2014
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
        self.gridLayout.addWidget(self.image_area, 0, 0, 1, 1)
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
        self.actionFermer = QtGui.QAction(MainWindow)
        self.actionFermer.setObjectName(_fromUtf8("actionFermer"))
        self.actionFiltre_Gaussien = QtGui.QAction(MainWindow)
        self.actionFiltre_Gaussien.setObjectName(_fromUtf8("actionFiltre_Gaussien"))
        self.actionFiltre_Median = QtGui.QAction(MainWindow)
        self.actionFiltre_Median.setObjectName(_fromUtf8("actionFiltre_Median"))
        self.actionFiltre_Moyenneur = QtGui.QAction(MainWindow)
        self.actionFiltre_Moyenneur.setObjectName(_fromUtf8("actionFiltre_Moyenneur"))
        self.menuOuvrir.addAction(self.actionOuvrir)
        self.menuOuvrir.addSeparator()
        self.menuOuvrir.addAction(self.actionFermer)
        self.menuFiltres.addAction(self.actionFiltre_Gaussien)
        self.menuFiltres.addAction(self.actionFiltre_Median)
        self.menuFiltres.addAction(self.actionFiltre_Moyenneur)
        self.menubar.addAction(self.menuOuvrir.menuAction())
        self.menubar.addAction(self.menuFiltres.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuOuvrir.setTitle(_translate("MainWindow", "Menu", None))
        self.menuFiltres.setTitle(_translate("MainWindow", "Filtres", None))
        self.actionQuit.setText(_translate("MainWindow", "quit", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir", None))
        self.actionFermer.setText(_translate("MainWindow", "Fermer", None))
        self.actionFiltre_Gaussien.setText(_translate("MainWindow", "Filtre Gaussien", None))
        self.actionFiltre_Median.setText(_translate("MainWindow", "Filtre Median", None))
        self.actionFiltre_Moyenneur.setText(_translate("MainWindow", "Filtre Moyenneur", None))

