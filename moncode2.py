#importation du module Image de la lib PIL
from PIL import Image

#ouverture de l'image
img=Image.open("/net/cremi/manpintault/Bureau/nat-gris.jpeg")
#affichage des données de l'image
print list(img.getdata())
#affichage de l'image
img.show()
#retournement de l'image
img1=img.rotate(180)
img1.show()
#miroir horizontal
img2=img.transpose(Image.FLIP_LEFT_RIGHT)
img2.show()
#miroir vertical
img3=img.transpose(Image.FLIP_TOP_BOTTOM)
img3.show()

#sauvegarder une image
img.save('nomDeImage.extension')
