#!python2
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from math import sqrt, pi, exp

LARGEUR = 256
HAUTEUR = 256
VAL_MAX = 255
VAL_MIN = 0


class Image(object):
	hauteur = 0
	largeur = 0
	fileType = "NONE"
	def __init__(self, hauteur = 0, largeur = 0, fileType = 'NONE'):
		self.hauteur = hauteur
		self.largeur = largeur
		self.fileType = fileType

	def getFileType(self):
		return self.fileType

class PPM(Image):
	fileName = "tmp.ppm"
	values = []
	def __init__(self, hauteur = HAUTEUR, largeur = LARGEUR, fileName = "tmp.ppm", values = []):
		self.fileName = fileName
		self.values = values
		self.fileType = "PPM"
		self.hauteur = HAUTEUR
		self.largeur = LARGEUR

	def afficher(self):
		print "File name: " , self.fileName
		print "File type: " , self.fileType
		print "Dimensions (hauteur x largeur): " , self.hauteur , " x " , self.largeur

	def lirePPM(self, file_name):
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
			self.fileName = file_name
			self.largeur = LARGEUR
			self.hauteur = HAUTEUR
			self.values = img

	def ecrirePPM(self, file_name):
		HAUTEUR = self.hauteur
		LARGEUR = self.largeur
		with open(file_name, "w") as f:
			f.write("P3\n" + str(LARGEUR) + " " + str(HAUTEUR) + "\n")
			f.write(str(VAL_MAX) + "\n")
			for y in range(0, HAUTEUR):
				for x in range(0, LARGEUR):
					for i in range(0, 3):
						f.write(str(self.values[x][y][i]) + "\n")
			f.close()

	def PPMtoPGM(self):
		pgm = PGM()
		HAUTEUR = self.hauteur
		LARGEUR = self.largeur
		dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				dest[x][y] = int(0.299*self.values[x][y][0] + 0.587*self.values[x][y][1] + 0.114*self.values[x][y][2])
		pgm.values = dest
		pgm.fileName = self.fileName[:len(self.fileName)-3] + "pgm"
		pgm.largeur = self.largeur
		pgm.hauteur = self.hauteur
		return pgm



		
class PGM(Image):
	fileName = "tmp.pgm"
	values = []
	def __init__(self, hauteur = HAUTEUR, largeur = LARGEUR, fileName = "tmp.pgm", values = []):
		self.fileName = fileName
		self.values = values
		self.fileType = "PGM"
		self.hauteur = HAUTEUR
		self.largeur = LARGEUR

	def afficher(self):
		print "File name: " , self.fileName
		print "File type: " , self.fileType
		print "Dimensions (hauteur x largeur): " , self.hauteur , " x " , self.largeur

	def lirePGM(self, fileName):
		with open(fileName, "r") as f:
			f.readline()
			LARGEUR, HAUTEUR = f.readline().split()
			LARGEUR = int(LARGEUR)
			HAUTEUR = int(HAUTEUR)
			img = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
			for y in range(0, HAUTEUR):
				for x in range(0, LARGEUR):
					img[x][y] = int(f.readline())
			f.close()
			self.fileName = fileName
			self.largeur = LARGEUR
			self.hauteur = HAUTEUR
			self.values = img

	def ecrirePGM(self, fileName):
		HAUTEUR = self.hauteur
		LARGEUR = self.largeur
		with open(fileName, "w") as f:
			f.write("P2\n" + str(LARGEUR) + " " + str(HAUTEUR) + "\n")
			f.write(str(VAL_MAX) + "\n")
			for y in range(0, HAUTEUR):
				for x in range(0, LARGEUR):
					f.write(str(self.values[x][y]) + "\n")
			f.close()

	def binarisation(self, seuil):
		dest = [[0 for x in range(0, self.largeur)] for x in range(0, self.hauteur)]
		for y in range(0, self.hauteur):
			for x in range(0, self.largeur):
				if self.values[x][y] > seuil:
					dest[x][y] = 255
				else:
					dest[x][y] = 0
		self.values = dest

	def imageUnie(self, colour, hauteur, largeur):
		dest = [[0 for x in range(0, largeur)] for x in range(0, hauteur)]
		for y in range(0, hauteur):
			for x in range(0, largeur):
				dest[x][y] = colour
		self.hauteur = hauteur
		self.largeur = largeur
		self.values = dest

	def degradeHorizontal(self, start, end, hauteur, largeur):
		dest = [[0 for x in range(0, largeur)] for x in range(0, hauteur)]
		inc = (end-start)/float(largeur)
		for y in range(0, hauteur):
			for x in range(0, largeur):
				dest[x][y] = int(start + x*inc)
		self.hauteur = hauteur
		self.largeur = largeur
		self.values = dest


	def miroir_horizontal(self):
		HAUTEUR = self.hauteur -1
		LARGEUR = self.largeur -1
		dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				dest[x][y] = self.values[LARGEUR-x][y]
		self.hauteur -= 1
		self.largeur -= 1
		self.values = dest
	

	def miroir_vertical(self):
		HAUTEUR = self.hauteur -1
		LARGEUR = self.largeur -1
		dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				dest[x][y] = self.values[x][HAUTEUR - y]
		self.hauteur -= 1
		self.largeur -= 1
		self.values = dest

	def sum_coef(self, filtre):
		somme = 0
		for y in filtre:
			for x in y:
				somme += x
		if somme == 0:
			somme = 1
		return somme

	def convolution(self, filtre):
		somme = self.sum_coef(filtre)
		hauteur_filtre = len(filtre)
		largeur_filtre = len(filtre[0])
		dest = [[0 for x in range(0, self.largeur+1)] for x in range(0, self.hauteur+1)]
		lf = int(float(largeur_filtre) / 2)
		hf = int(float(hauteur_filtre) / 2)
		for y in range(0, self.hauteur - hf ):
			for x in range(0, self.largeur - lf ):
				tmp = 0
				for i in range(0, hauteur_filtre):
					for j in range(0, largeur_filtre):
						tmp += (self.values[(x-j)%self.largeur][(y-i)%self.hauteur] * filtre[i][j])/somme
				dest[x][y] = tmp
		self.hauteur -= hf
		self.largeur -= lf
		return dest

	def detectionContours(self, filtre_gradx, filtre_grady):
		HAUTEUR = self.hauteur
		LARGEUR = self.largeur
		dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
		gx = self.convolution(filtre_gradx)
		gy = self.convolution(filtre_grady)
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				#print x, y
				dest[x][y] = sqrt(gx[x][y]**2 +gy[x][y]**2)
		self.values = dest

	def dcPrewitt(self):
		filtre_gradx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
		filtre_grady = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
		self.detectionContours(filtre_gradx, filtre_grady)

	def dcSobel(self):
		filtre_gradx = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
		filtre_grady = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
		self.detectionContours(filtre_gradx, filtre_grady)

	def dcLaplacien(self):
		filtre = [[-1, -1, -1], [-1, 8, 1], [-1, -1, -1]]
		self.values = self.convolution(filtre)

	def filtre_moyenneur(self, taille):
		return [[1 for x in range(0, taille)] for x in range(0, taille)]

	def filtre_gaussien(self, taille, sigma = 1):
		offset = int(float(taille)/2)
		filtre = [[0 for x in range(0, taille)] for x in range(0, taille)]
		for x in range(-offset, offset+1):
			for y in range(-offset, offset+1):
				filtre[(x+offset)%self.largeur][(y+offset)%self.hauteur] =  1/(2*pi*sigma**2) * exp(-(x**2 + y**2)/(2*sigma**2))
		coef = 1/filtre[0][0]
		for x in range(0, taille):
			for y in range(0, taille):
				filtre[x][y] = int(filtre[x][y] * coef)
		return filtre

	def moyenneur(self, taille):
		filtre = self.filtre_moyenneur(taille)
		self.values = self.convolution(filtre)

	def gaussien(self, taille):
		filtre = self.filtre_gaussien(taille)
		self.values = self.convolution(filtre)



	def median_value(self, values):
		values.sort()
		l = int(len(values)/2)
		if len(values) %2 == 0:
			return (values[l] + values[l+1]) / 2
		return values[l]

	def median(self, offset):
		HAUTEUR = self.hauteur
		LARGEUR = self.largeur
		dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
		for y in range(offset, HAUTEUR  - offset):
			for x in range(offset, LARGEUR - offset):
				temp_vals = []
				for i in range(-offset, offset):
					for j in range(-offset, offset):
						temp_vals.append(self.values[(x+i)%LARGEUR][(y+j)%HAUTEUR])
				dest[x][y] = self.median_value(temp_vals)
		self.values = dest

	def check_level(self, pixel, level):
		val = pixel + level
		if(val < VAL_MIN):
			return VAL_MIN
		elif(val > VAL_MAX):
			return VAL_MAX
		else:
			return val

	def LUT(self, level):
		HAUTEUR = self.hauteur
		LARGEUR = self.largeur
		dest = [[0 for x in range(0, LARGEUR)] for x in range(0, HAUTEUR)]
		for y in range(0, HAUTEUR):
			for x in range(0, LARGEUR):
				dest[x][y] = self.check_level(self.values[x][y], level)
		self.values = dest


# boats2 = PGM()
# boats2.afficher()
# boats2.lirePGM("images/camera.pgm")


# test = PPM()
# test.afficher()
# test.lirePPM("images/fleur.ppm")
# test.afficher()
# test.ecrirePPM("testPPM.ppm")

# boats2 = test.PPMtoPGM()
# boats2.afficher()
# boats2.LUT(50)
# boats2.ecrirePGM("test_classes.pgm")







