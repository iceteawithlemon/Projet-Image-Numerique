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

#define get_min(a,b) (a<b)?a:b; 
#define get_max(a,b) (a>b)?a:b; 

// Definition du type representant une image en
// niveaux de gris (ndg)
typedef unsigned char ndgIm [LARGEUR][HAUTEUR];
// Image couleur
typedef unsigned char coulIm [LARGEUR][HAUTEUR][3];

typedef int Histo[256];


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



 void lireCoulImage (char *nom, coulIm im)
 {
  FILE *descFic = NULL;

  int canalRouge, canalVert, canalBleu, x, y;

  ouvrirFichier (nom, &descFic, "r");
  lireEnTete (descFic, "P3");

  for (y=0; y < HAUTEUR; y++)  
    for (x=0; x < LARGEUR; x++)
    {
     fscanf (descFic, "%d", &canalRouge);
     im [x][y][0] = canalRouge;
     fscanf (descFic, "%d", &canalVert);
     im [x][y][1] = canalVert;
     fscanf (descFic, "%d", &canalBleu);
     im [x][y][2] = canalBleu;
   }
   fclose (descFic);
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


void 
ecrireCoulImage (char *nom, coulIm im)
{
  FILE *descFic = NULL;
  int x, y;

  ouvrirFichier (nom, &descFic, "w");
  ecrireEnTete (descFic, "P3");
  
  for (y=0; y < HAUTEUR; y++)
  {
    for (x=0; x < LARGEUR; x++)
    {
     fprintf (descFic, "%d ", im[x][y][0]);
     fprintf (descFic, "%d ", im[x][y][1]);
     fprintf (descFic, "%d ", im[x][y][2]);
   }
   fprintf (descFic, "\n");
 }
 fclose (descFic);
}

void init_histo(Histo h)
{
  for(int i = 0; i < 256; i++)
    h[i] = 0;
}


void remplir_histogramme(ndgIm im, Histo h)
{
  //init_histo(h);
  for(int y = 0; y < HAUTEUR; y++)
  {
    for(int x = 0; x < LARGEUR; x++)
    {
     h[im[x][y]]++;
   }
 }
}

void histogramme_dat(char *hnom, Histo h)
{
  FILE *descFic = NULL; 
  ouvrirFichier (hnom, &descFic, "w");
  // ecrireEnTete (descFic, "DAT");
  for (int i=0; i < 256; i++)
  {
    fprintf (descFic, "%d ", h[i]);
    fprintf (descFic, "\n");
  }
  fclose (descFic);

}

int maximum(ndgIm im)
{
  int max = 0;
  for(int y = 0; y < HAUTEUR; y++)
  {
    for(int x = 0; x < LARGEUR; x++)
    {
     if (im[x][y] > max)
       max = im[x][y];
   }
 }
 return max;
}

int minimum(ndgIm im)
{
  int min = VAL_MAX;
  for(int y = 0; y < HAUTEUR; y++)
  {
    for(int x = 0; x < LARGEUR; x++)
    {
     if (im[x][y] < min)
       min = im[x][y];
   }
 }
 return min;
}

void augmenter_contraste(ndgIm im)
{
  int min = minimum(im);
  int max = maximum(im);
  int n = 255/2;
  for(int y = 0; y < HAUTEUR; y++)
  {
    for(int x = 0; x < LARGEUR; x++)
    {
     if(im[x][y] < n)
       im[x][y] -= min;
     else
       im[x][y] += 255 - max;
   }
 }
}


int somme_coef(int filtre[][3], int largeur_filtre, int hauteur_filtre)
{
  int sum = 0;
  for(int i = 0; i < hauteur_filtre; i++)
  {
    for(int j = 0; j < largeur_filtre; j++)
    {
     sum += filtre[i][j];
   }
 }
 return sum;
}


void convolution(ndgIm a, ndgIm b, int largeur_filtre, int hauteur_filtre, int filtre[largeur_filtre][hauteur_filtre])
{
  int lf = largeur_filtre/2.0 +0.5f;
  int hf = (int)hauteur_filtre/2.0 + 0.5f;
  int sum = somme_coef(filtre, largeur_filtre, hauteur_filtre);
  for(int y = hf; y < HAUTEUR - hf; y++)
  {
    for(int x = lf; x < LARGEUR - lf; x++)
    {
     int tmp = 0;
     for(int i = 0; i < hauteur_filtre; i++)
     {
      for(int j = 0; j < largeur_filtre; j++)
      {
       tmp += a[x-j][y-i]*filtre[i][j]/sum;
       }
     }
     b[x][y] = tmp;
    }
  }
}






int 
main ()
{
  ndgIm im, dest;
  
  lireNdgImage ("baboon.pgm", im);
  ecrireNdgImage ("test.pgm", im);

  // Question 5.1 
  ndgIm im1,im2;
  lireNdgImage("diffA.pgm", im1);
  lireNdgImage("diffB.pgm", im2);

  ecrireNdgImage ("diff.pgm",dest);

  // Question 5.2 et 5.3 
  coulIm im3,im4,destC;
  lireCoulImage("fond.ppm", im3);
  lireCoulImage("objet.ppm", im4);

  ecrireCoulImage ("add.ppm",destC);
  ecrireCoulImage ("supp.ppm",destC);

  //Question 2.5
  Histo hist_1, hist_2;
  ndgIm im_1, im_2;
  lireNdgImage("image1.pgm", im_1);
  remplir_histogramme(im_1, hist_1);
  histogramme_dat("hist_1.dat", hist_1);

  lireNdgImage("image2.pgm", im_2);
  remplir_histogramme(im_2, hist_2);
  histogramme_dat("hist_2.dat", hist_2);

  //Question 4.1
  printf("Valeur max d'image2: %d\n", maximum(im_2));
  printf("Valeur min d'image2: %d\n", minimum(im_2));

  // augmenter_contraste(im_2);
  // ecrireNdgImage("image2_contrast.pgm", im_2);

  int filtre_moyenneur[3][3] = {{1, 1, 1}, {1, 1, 1}, {1, 1, 1}};
  int filtre_gaussien3[3][3] = { {1, 2, 1}, {2, 4, 2}, {1, 2, 1}};
  int filtre_gaussien5[5][5] = { {1, 4, 6, 4, 1}, {4, 16, 25, 16, 4}, {6, 24, 36, 24, 6}, {4, 16, 25, 16, 4}, {1, 4, 6, 4, 1}};


  ndgIm b;
  convolution(im_2, b, 3, 3, filtre_moyenneur);
  ecrireNdgImage("image2_convol.pgm", b);

  convolution(im_2, b, 5, 5, filtre_gaussien5);
  ecrireNdgImage("image2_gauss5.pgm", b);
  
  convolution(im_2, b, 3, 3, filtre_gaussien3);
  ecrireNdgImage("image2_gauss3.pgm", b);



  return EXIT_SUCCESS;
}
