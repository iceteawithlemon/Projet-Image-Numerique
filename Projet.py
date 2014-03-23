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
		f.write(str(VAL_MAX) + "\n")
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				f.write(str(img[x][y]) + "\n")
		f.close()

def lirePPM(file_name):
	with open(file_name, "r") as f:
		f.readline()
		LARGEUR, HAUTEUR = f.readline().split()
		LARGEUR = int(LARGEUR)
		HAUTEUR = int(HAUTEUR)
		VAL_MAX = int(f.readline())
		img = [[[0 for i in range(0, 3)] for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				for i in range(0, 3):
					img[x][y][i] = int(f.readline())
		f.close()
		return img

def ecrirePPM(file_name, img):
	HAUTEUR = len(img)
	LARGEUR = len(img[0])
	with open(file_name, "w") as f:
		f.write("P3\n" + str(LARGEUR) + " " + str(HAUTEUR) + "\n")
		f.write(str(VAL_MAX) + "\n")
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				for i in range(0, 3):
					f.write(str(img[x][y][i]) + "\n")
		f.close()

def RGBtoGray(src):
	dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
	for y in range(0, HAUTEUR):
		for x in range(0, LARGEUR):
			dest[x][y] = int(0.299*src[x][y][0] + 0.587*src[x][y][1] + 0.114*src[x][y][2])
	return dest

def binarisation(src, seuil):
	dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
	for y in range(0, HAUTEUR):
		for x in range(0, LARGEUR):
			if src[x][y] > seuil:
				dest[x][y] = 255
			else:
				dest[x][y] = 0
	return dest

def imageUnie(colour):
	dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
	for y in range(0, HAUTEUR):
		for x in range(0, LARGEUR):
			dest[x][y] = colour
	return dest

def degradeHorizontal(start, end):
	dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
	inc = (end-start)/float(LARGEUR)
	for y in range(0, HAUTEUR):
		for x in range(0, LARGEUR):
			dest[x][y] = int(start + x*inc)
	return dest

def sum_coef(filtre):
	sum = 0
	for y in filtre:
		for x in y:
			sum += x
	return sum

def convolutionPGM(src, filtre):
	somme = sum_coef(filtre)
	hauteur_filtre = len(filtre)
	largeur_filtre = len(filtre[0])
	dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
	lf = int(float(largeur_filtre) / 2)
	hf = int(float(hauteur_filtre) / 2)
	for y in range(0, HAUTEUR - hf):
		for x in range(0, LARGEUR - lf):
			tmp = 0
			for i in range(0, hauteur_filtre):
				for j in range(0, largeur_filtre):
					tmp += (src[x-j][y-i] * filtre[i][j])/somme
			dest[x][y] = tmp
	return dest







filtre_moyenneur = [[1, 1, 1], [1, 1, 1], [1, 1, 1]];
filtre_gaussien3 = [ [1, 2, 1], [2, 4, 2], [1, 2, 1]];
filtre_gaussien5 = [ [1, 4, 6, 4, 1], [4, 16, 25, 16, 4], [6, 24, 36, 24, 6], [4, 16, 25, 16, 4], [1, 4, 6, 4, 1]];



boats = lirePGM("images/boats.pgm")
# ecrirePGM("boats_test.pgm", boats)
# fleur = lirePPM("images/fleur.ppm")
# ecrirePPM("fleur_test.ppm", fleur)
# ecrirePGM("fleurBW.pgm", RGBtoGray(fleur))
# ecrirePGM("boatsBin.pgm", binarisation(boats, 128))
# colour = [128, 200, 100]
# ecrirePGM("imageUnieBW.pgm", imageUnie(128))
# ecrirePPM("imageUnieRGB.ppm", imageUnie(colour))
# ecrirePGM("degradHorizon.pgm", degradeHorizontal(1, 255))

ecrirePGM("test_convol_moy.pgm", convolutionPGM(boats, filtre_moyenneur))
ecrirePGM("test_convol_gauss5.pgm", convolutionPGM(boats, filtre_gaussien5))





