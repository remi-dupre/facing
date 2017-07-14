Utilité
-------
Les union-find sont une structure de données qui permet de représenter une partition d'ensembles, et d'implémenter une opération de réunion.


Structure
---------
Chaque ensemble est représenté par un arbre. L'ensemble est identifié par sa racine, et chaque élément de l'ensemble référence une unique arrête vers son parent. Les racines référencent une arrête vers elle-même.
Ici, une fonction `repr` prendra en argument la structure et un élément et retourne la racine associée :
```
      3             4
     / \           / \
    2   7         0   6
       / \
      1   5

Ensemble [0, 7] partitionné en deux parties : {1, 2, 3, 5, 7} et {0, 4, 6}.
On a :
    repr(uf, 5) = repr(uf, 3) = 3
    repr(uf, 0) = repr(uf, 4) = 4
```

On peut alors représenter la structure par un unique tableau. Par exemple, pour représenter la partition ne contenant que des singletons :
```c++
vector<int> uf(n);
for(int i=0 ; i < n ; i++) {
    uf[i] = i;
}
```


Opérations
----------
### Réunion
La réunion se fait simplement en ajoutant l'une des racines aux fils de l'autre.
```c++
void union(vector<int> &uf, int a, int b) {
    // Effectue l'union de a et b dans le union-find donné.
    uf[repr(uf, b)] = repr(uf, a);
}
```

```
      3             4               3
     / \           / \             /|\
    2   7         0   6     ->    2 | \
       / \                          7  4
      1   5                        /|  |\
                                  1 5  0 6
```

### Recherche
La recherche se fait récursivement jusqu'à atteindre la racine.

On remarque que l'opération de réunion pourait créer un arbre de taille linéaire en le nombre de sommets, et faire monter la complexité moyenne de l'utilisation de la structure, pour y remédier, on profite de la recherche pour applatir l'arbre.

```c++
int repr(vector<int> uf, a) {
    if(uf[a] == a) {
        // a est parent de a, donc racine
        return a;
    }
    else {
        // recherche du représentant du parent
        int p = repr(uf, uf[a]);
        // on applatit en mettant a fils de son représentant
        return uf[a] = p;
    }
}
```


Complexité
----------
Il est possible d'ameillorer la complexité en une complexité très faible en rajoutant encore [une ameilloration](https://www.wikiwand.com/fr/Union-find#/Impl.C3.A9mentation_utilisant_des_for.C3.AAts).  
