#!python2
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from PIL import Image
from math import sqrt, pi, exp

LARGEUR = 256
HAUTEUR = 256
VAL_MAX = 255
VAL_MIN = 0

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
	somme = 0
	for y in filtre:
		for x in y:
			somme += x
	if somme == 0:
		somme = 1
	return somme

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

def gradientPGM(src):
	filtre_gradx = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
	filtre_grady = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
	dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
	gx = convolutionPGM(src, filtre_gradx)
	gy = convolutionPGM(src, filtre_grady)
	for y in range(0, HAUTEUR):
		for x in range(0, LARGEUR):
			dest[x][y] = sqrt(gx[x][y]**2 +gy[x][y]**2)
	return dest

def miroir_horizontal(src):
	HAUTEUR = len(src) -1
	LARGEUR = len(src[0]) -1
	dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
	for y in range(0, HAUTEUR):
		for x in range(0, LARGEUR):
			dest[x][y] = src[LARGEUR-x][y]
	return dest
	
def miroir_vertical(src):
	HAUTEUR = len(src) -1
	LARGEUR = len(src[0]) -1
	dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
	for y in range(0, HAUTEUR):
		for x in range(0, LARGEUR):
			dest[x][y] = src[x][HAUTEUR - y]
	return dest


def filtre_moyenneur(taille):
	return [[1 for x in range(0, taille)] for x in range(0, taille)]

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

def median_PGM(src, offset):
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

# ecrirePGM("test_LUT_eclaircir.pgm", LUT_PGM(boats, 100))
# ecrirePGM("test_LUT_assombrir.pgm", LUT_PGM(boats, -100))
# # ecrirePGM("test_grad.pgm", gradientPGM(boats))
#ecrirePGM("miroir.pgm", miroir_vertical(boats))






