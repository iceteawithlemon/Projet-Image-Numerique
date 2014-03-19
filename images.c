#include <stdio.h>
#include <stdlib.h>
#include <math.h>



#define LARGEUR 256
#define HAUTEUR 256
#define VAL_MAX 255


#define R 0
#define G 1
#define B 2

#define PI 3.14159265358979323846

// Definition du type representant une image en
// niveaux de gris (ndg)
typedef unsigned char ndgIm [LARGEUR][HAUTEUR];
// Image couleur
typedef unsigned char coulIm [LARGEUR][HAUTEUR][3];

typedef int histo [255];


// mode = "r" ou "w"
void 
ouvrirFichier (char *nom, FILE **desc, char *mode)
{
  *desc = fopen (nom, mode);
  if (*desc == NULL)
    {
      fprintf (stderr, 
	       "\"%s\": nom de fichier incorrect", 
	       nom);
      if (mode [0] == 'w')
	fprintf (stderr, " ou ouverture en ecriture impossible.");
      exit (EXIT_FAILURE);
    }
}


// Lecture et verification que l'en-tete est correcte et correspond 
// bien a notre mode (P2 = ndg ASCII, P3 = rgb ASCII)
void
lireEnTete (FILE *descFic, char *mode)
{
  char c;
  int v;

  fscanf (descFic, "%c", &c);
  // Lecture du mode
  if (c != mode[0])
    {
      fprintf (stderr, "Mode non defini (%c*).\n", c);
      exit (EXIT_FAILURE);
    }
  fscanf (descFic, "%c", &c);
  if (c != mode[1])
    {
      fprintf (stderr, "%s est necessaire pour une image ASCII en niveaux de gris.\n", mode);
      exit (EXIT_FAILURE);
    }
  // Lecture des dimensions
  fscanf (descFic, "%d", &v);
  if (v != HAUTEUR)
    {
      fprintf (stderr, "La hauteur doit etre de %d.\n", HAUTEUR);
      exit (EXIT_FAILURE);
    }
  fscanf (descFic, "%d", &v);
  if (v != LARGEUR)
    {
      fprintf (stderr, "La largeur doit etre de %d.\n", LARGEUR);
      exit (EXIT_FAILURE);
    }
  // Et lecture de la valeur maximale d'une intensite
  fscanf (descFic, "%d", &v);
  if (v != VAL_MAX)
    {
      fprintf (stderr, "L'intensite maximale doit etre de %d.\n", VAL_MAX);
      exit (EXIT_FAILURE);
    }
}
  

// Lecture d'une image en ndg: mise a jour de la 
// structure de donnees de type ndgIm
void 
lireNdgImage (char *nom, ndgIm im)
{
  FILE *descFic = NULL;
  int c, x, y;

  ouvrirFichier (nom, &descFic, "r");
  lireEnTete (descFic, "P2");

  for (y=0; y < HAUTEUR; y++)  
    for (x=0; x < LARGEUR; x++)
      {
	fscanf (descFic, "%d", &c);
	im [x][y] = c;
      }
  
  fclose (descFic);
}

void lireCoulImage(char *nom, coulIm im)
{
  FILE *descFic = NULL;
  int c, x, y;

  ouvrirFichier(nom, &descFic, "r");
  lireEnTete(descFic, "P3");

  for(y = 0; y < HAUTEUR; y++)
  {
    for(x = 0; x < LARGEUR; x++)
    {
      for(int i = 0; i < 3; i++)
      {
        fscanf (descFic, "%d", &c);
        im [x][y][i] = c;
      }
    }
  }

  fclose(descFic);
}

// Ecrit l'en-tete correcte en fonction du mode
// le fichier est deja ouvert
void 
ecrireEnTete (FILE *descFic, char *mode)
{
  fprintf (descFic, "%s\n", mode);
  fprintf (descFic, "%d %d\n", HAUTEUR, LARGEUR);
  fprintf (descFic, "%d\n", VAL_MAX);
}


// Ecrit une image en ndg
void 
ecrireNdgImage (char *nom, ndgIm im)
{
  FILE *descFic = NULL;
  int x, y;
  
  ouvrirFichier (nom, &descFic, "w");
  ecrireEnTete (descFic, "P2");
  
  for (y=0; y < HAUTEUR; y++)
    {
      for (x=0; x < LARGEUR; x++)
        fprintf (descFic, "%d ", im[x][y]);
      fprintf (descFic, "\n");
    }

  fclose (descFic);
}

void ecrireCoulImage(char *nom, coulIm im)
{
  FILE *descFic = NULL;
  int x, y;

  ouvrirFichier(nom, &descFic, "w");
  ecrireEnTete(descFic, "P3");

  for(y = 0; y < HAUTEUR; y++)
  {
    for(x = 0; x < LARGEUR; x++)
    {
      for(int i = 0; i < 3; i++)
      {
        fprintf(descFic, "%d ", im[x][y][i]);
      }
      fprintf (descFic, "\n");
    }
  }

  fclose(descFic);
}

void RGBtoGray(coulIm src, ndgIm dest)
{
  int x, y;
  for (y=0; y < HAUTEUR; y++)
    {
      for (x=0; x < LARGEUR; x++)
      {
        dest[x][y] = 0.299*src[x][y][0] + 0.587*src[x][y][1] + 0.114*src[x][y][2];
      }
    }
}

void binarisation(ndgIm src, ndgIm dest, unsigned char seuil)
{
  int x, y;
  for (y=0; y < HAUTEUR; y++)
    {
      for (x=0; x < LARGEUR; x++)
      {
          dest[x][y] = (src[x][y] >= seuil)? 255 :0;
      }
    }
}

void imageUnie(char *nom, int ng)
{
  FILE *descFic = NULL;
  int x, y;

  ouvrirFichier(nom, &descFic, "w");
  ecrireEnTete(descFic, "P2");

  for(y = 0; y < HAUTEUR; y++)
  {
    for(x = 0; x < LARGEUR; x++)
      fprintf(descFic, "%d ", ng);
    fprintf(descFic, "\n");
  }
  fclose(descFic);
}

void degradeHorizontal(char *nom, int ng1, int ng2)
{
  FILE *descFic = NULL;
  int x, y;

  ouvrirFichier(nom, &descFic, "w");
  ecrireEnTete(descFic, "P2");
  float ng = ng1;
  float inc = (float)(ng2-ng1)/LARGEUR;
  for(y = 0; y < HAUTEUR; y++)
  {
    for(x = 0; x < LARGEUR; x++)
    {
      ng = ng1+x*inc;
      fprintf(descFic, "%d ", (int)ng);

    }
    fprintf(descFic, "\n");
  }
  fclose(descFic);
}

void histogramme(histo h, ndgIm im)
{
  int x, y, c;
  for (y=0; y < HAUTEUR; y++)
    {
      for (x=0; x < LARGEUR; x++)
      {
          c = (int)im[x][y];
          h[c]++;
      }
    }
}


/**********************/
// Question 8.3
/**********************/
void histogramme_dat(char* hnom, histo h){ 
  FILE *hfile = NULL;
  ouvrirFichier (hnom, &hfile, "w");
  int i; 
  for (i = 0; i < VAL_MAX; i++) 
    fprintf(hfile,"%d %f \n", i,h[i]); 
  fclose(hfile);
} 


void initHist(histo h)
{
  for(int i = 0; i < 256; i++)
  {
    h[i] = 0;
  }
}

int 
main ()
{
  ndgIm im;
  ndgIm im4;
  ndgIm im3;
  coulIm im2;
  lireNdgImage ("brume.pgm", im);
  lireNdgImage("brume.pgm", im4);
  ecrireNdgImage ("test.pgm", im);

  imageUnie("gris.pgm", 50);
  degradeHorizontal("degrade.pgm", 100, 200);

  lireCoulImage("fleur.ppm", im2);
  im2[LARGEUR/2][HAUTEUR/2][0] = 0;
  im2[LARGEUR/2][HAUTEUR/2][1] = 255;
  im2[LARGEUR/2][HAUTEUR/2][2] = 0;
  ecrireCoulImage("test2.ppm", im2);


  RGBtoGray(im2, im);
  ecrireNdgImage("test3.pgm", im);

  binarisation(im4, im3, 128);
  ecrireNdgImage("test4.pgm", im3);

  histo h, h2;
  initHist(h);
  initHist(h2);
  histogramme(h, im4);
  histogramme(h2, im3);

  histogramme_dat("hist1", h);
  histogramme_dat("hist2", h2);

  return EXIT_SUCCESS;
}
