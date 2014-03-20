#!python2
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from PIL import Image

LARGEUR = 256
HAUTEUR = 256
VAL_MAX = 255

def lireEnTete(fichier, mode):
	f_mode = f.read(2)
	return f_mode == mode

def lirePGM(file_name):
	with open(file_name, "r") as f:
		f.readline()
		LARGEUR, HAUTEUR = f.readline().split()
		LARGEUR = int(LARGEUR)
		HAUTEUR = int(HAUTEUR)
		img = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				img[x][y] = int(f.readline())
		f.close()
		return img

def ecrirePGM(file_name, img):
	HAUTEUR = len(img)
	LARGEUR = len(img[0])
	with open(file_name, "w") as f:
		f.write("P2\n" + str(LARGEUR) + " " + str(HAUTEUR) + "\n")
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				f.write(str(img[x][y]) + "\n")
		f.close()


test = lirePGM("images/boats.pgm")
ecrirePGM("boats_test.pgm", test)
test2 = lirePGM("boats_test.pgm")





