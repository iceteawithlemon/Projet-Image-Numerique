import sys 
import os 

from PyQt4 import QtCore, QtGui 
from math import sqrt, pi, exp
from PIL import Image 

LARGEUR = 256
HAUTEUR = 256
VAL_MAX = 255
VAL_MIN = 0


class ImageViewer(object): 
    def setupUi(self, Viewer): 
        Viewer.resize(640, 480) 
        Viewer.setWindowTitle(u"Exemples d'usage d'images")     
        self.image_1 = "boats.pbm" 
        self.image_2 = "image2.png"             
        self.centralwidget = QtGui.QWidget(Viewer) 
        self.gridLayout = QtGui.QGridLayout(self.centralwidget) 
        self.verticalLayout_2 = QtGui.QVBoxLayout() 
        self.horizontalLayout = QtGui.QHBoxLayout() 

       
 
        # QGraphicsView 
        self.vue = QtGui.QGraphicsView(self.centralwidget) 
        self.vue.wheelEvent = self.wheel_event
        self.verticalLayout_2.addWidget(self.vue) 
 
        self.horizontalLayout_4 = QtGui.QHBoxLayout() 
        self.horizontalLayout_4.setObjectName("horizontalLayout_4") 
        self.image_btn = QtGui.QToolButton(self.centralwidget) 
        self.image_btn.setText("Image") 
        self.image_btn.setObjectName("image_btn") 
        self.horizontalLayout_4.addWidget(self.image_btn) 
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, 
                                        QtGui.QSizePolicy.Minimum) 
        self.horizontalLayout_4.addItem(spacerItem2) 
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1) 
        Viewer.setCentralWidget(self.centralwidget) 
 
        self.m_h = QtGui.QToolButton() 
        self.m_h.setText("miroir_horizontal") 
        self.m_h.setObjectName("m_h") 
        self.horizontalLayout_4.addWidget(self.m_h) 
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, 
                                        QtGui.QSizePolicy.Minimum) 
        self.horizontalLayout_4.addItem(spacerItem2) 
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 2, 2) 
        Viewer.setCentralWidget(self.centralwidget) 

        
        self.f = QtGui.QToolButton() 
        self.f.setText("fermer") 
        self.f.setObjectName("f") 
        self.horizontalLayout_4.addWidget(self.f) 
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, 
                                        QtGui.QSizePolicy.Minimum) 
        self.horizontalLayout_4.addItem(spacerItem2) 
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1) 
        Viewer.setCentralWidget(self.centralwidget)     
        
        # Connections
        self.image_btn.clicked.connect(self.get_image)
        self.m_h.clicked.connect(self.miroir_horizontal)
        self.f.clicked.connect(Viewer.close)
    
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
    
    def get_image(self):
        img = unicode(QtGui.QFileDialog.getOpenFileName(Viewer, 
                                    u"Ouverture de fichiers",
                                    "", "Image Files (*.png *.jpg *.bmp *.pgm *.gif *.jpeg)")) 
        if not img:
            return
        self.open_image(img)

    def open_image(self, path):
        w_vue, h_vue = self.vue.width(), self.vue.height() 
        self.current_image = QtGui.QImage(path)
        self.pixmap = QtGui.QPixmap.fromImage(self.current_image.scaled(w_vue, h_vue,
                                    QtCore.Qt.KeepAspectRatio, 
                                    QtCore.Qt.SmoothTransformation)) 
        self.view_current()

    def miroir_horizontal(self):
		img=self.get_image()
		img2=img.transpose(Image.FLIP_LEFT_RIGHT)
        self.view_current(img2)
        
       

    def view_current(self):
        w_pix, h_pix = self.pixmap.width(), self.pixmap.height()
        self.scene = QtGui.QGraphicsScene()
        self.scene.setSceneRect(0, 0, w_pix, h_pix)
        self.scene.addPixmap(self.pixmap)
        self.vue.setScene(self.scene)
        
    


if __name__ == "__main__": 
    import sys 
    app = QtGui.QApplication(sys.argv) 
    Viewer = QtGui.QMainWindow() 
    ui = ImageViewer() 
    ui.setupUi(Viewer) 
    Viewer.show()   
    sys.exit(app.exec_()) 
