#include <stdio.h>
#include <stdlib.h>
#include <math.h>



#define LARGEUR 256
#define HAUTEUR 256
#define VAL_MAX 255


#define R 0
#define G 1
#define B 2



// Definition du type representant une image en
// niveaux de gris (ndg)
typedef int ndgIm [LARGEUR][HAUTEUR];
// Image couleur
typedef int coulIm [LARGEUR][HAUTEUR][3];



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

//fonction convolution
void convolution(ndgIm src, ndgIm dest, int** filtre, int largeur_filtre, int hauteur_filtre, int norm) {

  int x,y,ix,iy;

  for (y=hauteur_filtre/2;y<HAUTEUR-hauteur_filtre/2; y++) {  
    for (x=largeur_filtre/2;x<LARGEUR-largeur_filtre/2; x++) {
      int somme = 0;
      for (iy=-hauteur_filtre/2; iy<=hauteur_filtre/2; iy++) {
		for (ix=-largeur_filtre/2; ix<=largeur_filtre/2; ix++) {
			somme += src[x+iy][y+ix]; 
	}
      }
      norm = somme/9;
    }
  }
}

//fonction filtre moyenneur generique pour fonctionnement convolution à tester 
void filtre_moyenneur (ndgIm im, int masque){
	int som;
	int Moy=0;
		
	for(int i=1; i<LARGEUR-1;i++){
		for(int j=1; j<HAUTEUR-1;j++){
			som =0;
			for(int k=-1; k<1;k++){
				for(int l=-1; l<1; l++)
					som=som+(im[i+k][j+l]);
				}
			Moy = som/9;
			im[i][j]=Moy;
			}

			
		}
	}


int main ()
{
  ndgIm im;
  
  lireNdgImage ("lena.pgm", im);


  ndgIm dest;

  int** filtre;
  int largeur_filtre = 3;
  int hauteur_filtre = 3;
  filtre =(int**) malloc((largeur_filtre+1)*sizeof(int*));  
  for (int ix=0; ix<=largeur_filtre; ix++) {
    filtre[ix] =(int*) malloc((hauteur_filtre+1)*sizeof(int));  
  }
  for (int iy=0; iy<=hauteur_filtre; iy++) {
    for (int ix=0; ix<=largeur_filtre; ix++) {
      filtre[ix][iy] = 0;
    }
  }

  convolution(im, dest, filtre, 3, 3, 1);

  ecrireNdgImage ("conv.pgm", dest);
  for (int ix=largeur_filtre;ix>=0; ix--) {
    free(filtre[ix]);
  }

  free(filtre);

  return EXIT_SUCCESS;
}
