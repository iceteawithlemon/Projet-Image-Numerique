# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logiciel.ui'
#
# Created: Mon Apr 07 14:19:51 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(810, 452)
        self.Ouvrir = QtGui.QPushButton(Form)
        self.Ouvrir.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.Ouvrir.setObjectName(_fromUtf8("Ouvrir"))
        self.mirroir = QtGui.QComboBox(Form)
        self.mirroir.setGeometry(QtCore.QRect(100, 20, 111, 22))
        self.mirroir.setObjectName(_fromUtf8("mirroir"))
        self.mirroir.addItem(_fromUtf8(""))
        self.mirroir.addItem(_fromUtf8(""))
        self.mirroir.addItem(_fromUtf8(""))
        self.filtre = QtGui.QComboBox(Form)
        self.filtre.setGeometry(QtCore.QRect(230, 20, 101, 22))
        self.filtre.setObjectName(_fromUtf8("filtre"))
        self.filtre.addItem(_fromUtf8(""))
        self.filtre.addItem(_fromUtf8(""))
        self.filtre.addItem(_fromUtf8(""))
        self.filtre.addItem(_fromUtf8(""))
        self.fermer = QtGui.QPushButton(Form)
        self.fermer.setGeometry(QtCore.QRect(730, 20, 75, 23))
        self.fermer.setObjectName(_fromUtf8("fermer"))
        self.lvl_gris = QtGui.QPushButton(Form)
        self.lvl_gris.setGeometry(QtCore.QRect(350, 20, 101, 23))
        self.lvl_gris.setObjectName(_fromUtf8("lvl_gris"))
        self.sauvegarde = QtGui.QPushButton(Form)
        self.sauvegarde.setGeometry(QtCore.QRect(470, 20, 121, 23))
        self.sauvegarde.setObjectName(_fromUtf8("sauvegarde"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.fermer, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QObject.connect(self.Ouvrir, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_image)
        QtCore.QObject.connect(self.sauvegarde, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sauvegarder)      
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Ouvrir.setText(_translate("Form", "Ouvrir Image", None))
        self.mirroir.setItemText(0, _translate("Form", "Mirroir", None))
        self.mirroir.setItemText(1, _translate("Form", "Mirroir Horizontal", None))
        self.mirroir.setItemText(2, _translate("Form", "Mirroir Vertical", None))
        self.filtre.setItemText(0, _translate("Form", "Filtre", None))
        self.filtre.setItemText(1, _translate("Form", "Filtre Gaussien", None))
        self.filtre.setItemText(2, _translate("Form", "Filtre Moyenneur", None))
        self.filtre.setItemText(3, _translate("Form", "Filtre Median", None))
        self.fermer.setText(_translate("Form", "Fermer", None))
        self.lvl_gris.setText(_translate("Form", "Niveau de gris", None))
        self.sauvegarde.setText(_translate("Form", "Sauvegarder Image", None))


    def get_image(self):         
        img = unicode(QtGui.QFileDialog.getOpenFileName(Form, 
                                    u"Ouverture de fichiers",
                                    "", "Image Files (*.png *.jpeg *.bmp *.pgm *.ppm *.gif)")) 
        if not img:
            return
        self.open_image(img)

    def sauvegarder(self):
        fichier = unicode (QtGui.QFileDialog.getSaveFileName(
            Form, 
           "Enregistrer un fichier", 
            QString(), 
           "Images (*.png *.gif *.jpg *.jpeg)"))

    

if __name__ == "__main__": 
    import sys 
    app = QtGui.QApplication(sys.argv) 
    Form = QtGui.QMainWindow() 
    ui = Ui_Form() 
    ui.setupUi(Form) 
    Form.show() 	
    sys.exit(app.exec_()) 



