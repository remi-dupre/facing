Principe
--------
L'idée part du constat qu'une image reproduit souvent plusieurs fois des formes semblables (par exemple à la frontière entre deux objets). On se retrouve donc ici à retenir des transformations de l'image dans elle même.

### Algorithme
Pour cela on a un ensemble de quelques transformations que l'on peut appliquer.
L'algorithme naïf consiste à calculer chacunes de ces transformations pour tous les blocs, et de chercher pour chaque portion laquelle est la plus proche.
Pour décompresser il suffit d'appliquer les tranformations obtenues récursivements, le théorème du point fixe de [Banach][fixpoint] assurant que cette opération converge vers un résultat.

Résultats
---------
L'algorithme qui précède est très lourd, et même si on peut avoir des taux de compression, il n'est pas réaliste (on prend de l'ordre d'une heure pour compresser une image couleur).

Travail en cours
----------------
Pour accélérer le processus, je cherche de temps en temps une structure de donnée qui permettrait d'accélérer le processus de recherche.
Un problème étant le concept de [fléaux de la dimension][dimension][^bigdim], il est difficile d'imaginer une méthode exacte. Les méthodes que j'utilises sont du coup arbitraires et doivent êtres testées manuelement avant de conclure.

À propos
--------
L'idée a été lancée par [Christophe Bertault][cbertault], qui était à ce moment mon professeur de MPSI.
Je me suis lancé dans ce projet pour mon TIPE que j'ai soutenu en MP* où j'ai été encadré par [Jérome Gaertner][jgaertner].

<p class="img-container">
    <img src="https://raw.githubusercontent.com/remi100756/Compression-Fractale/master/lena.gif">
</p>



[^bigdim]: En général on s'intéresse à des blocs de 4x4 ou 8x8 environs, donc des espaces de dimension 16 ou 64


[dimension]: https://www.wikiwand.com/fr/Fléau_de_la_dimension
[fixpoint]: https://fr.wikipedia.org/wiki/Théorèmes_de_point_fixe
[publication]: ../../static/pdf/tipe.pdf

[cbertault]: http://christophebertault.fr/
[jgaertner]: http://jerome.gaertner.free.fr/
