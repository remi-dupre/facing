Objectif
--------
L'objectif d'un segment-tree est de représenter pour une liste de n éléments le résultat d'une opération associative sur chaque segment [i, j] des éléments.
Ils permettent d'effectuer en temps logarithmique les opérations d'affectation et de requête (de la valeur de l'opération sur chaque élément d'un intervalle).

Représentation
--------------
On représente facilement l'intervalle par un arbre binaire de hauteur logarithmique, il suffit de couper l'intervalle en deux.*
Pour chaque noeud de l'arbre, on se propose de conserver le résultat de l'opération appliquée aux éléments qu'il représente.
On peut alors initialiser l'arbre en donnant comme valeur à tous les noeuds l'élément neutre de l'opération considérée.
```
                                        [0, 5]
Représentation de [0, 5]               /      \
par un segment tree               [0, 2]      [3, 5]
                                  /    \      /    \
                              [0, 1]    2  [3, 4]   5
                               /  \         /  \
                              0    1       3    4
```

Opérations
----------
### Affectation
Dans la version la plus simple, on ne se permet que de modifier un élément par opération.
Il suffit alors de mettre à jours la feuille qui concerne cet élément et tous ses parents.
```cpp
/* Le segment tree est ici représenté par un tableau 'sum'.
 * La racine est située à l'indice 0, les fils du noeud v sont 2v+1 et 2v+2.
 *
 * set(x, i, v, l, r)
 *   - met à jour la valeur du sommet 'i' à 'x'
 *   - affecte les informations sur l'intervalle [l, r-1]
 *   - 'v' est l'indice qui représente [l, r-1] */
void set(lint x, int i, int v, int l, int r) {
    if (l == r-1) {
        // 'v' est une feuille
        sum[v] = x;
    }
    else {
        int mid = (l + r + 1) / 2;
        if (i < mid) {
            // on met à jour la partie gauche de l'arbre
            set(sum, x, i, 2*v+1, l, mid);
        }
        else {
            // on met à jour la partie droite de l'arbre
            set(sum, x, i, 2*v+2, mid, r);
        }
        // on met à jour le résultat sur [l, r-1]
        sum[v] = sum[2*v+1] + sum[2*v+2];
    }
}
```

### Requête
Pour récupérer la valeur d'un intervalle on récupère tous les plus haut noeuds qui sont inclus dans l'intervalle.
```cpp
/* get(a, b, v, l, r)
 *  - retourne la somme des valeurs d'éléments dans un intervalle
 *  - considère les éléments dans [a, b-1] et [l, r-1]
 *  - 'v' est l'indice qui représente [l, r-1] */
lint get_sum(int a, int b, int v, int l, int r) {
    if (b <= l || a >= r) {
        // [a, b-1] et [l, r-1] sont disjoints
        return 0;
    }
    else if (a <= l && b >= r) {
        // [l, r-1] est inclus dans [a, b-1]
        return sum[v];
    }
    else {
        // on coupe la somme en deux puis réuni les résultats
        int mid = (l + r) / 2;
        return get_sum(sum, a, b, 2*v+1, l, mid) + get_sum(sum, a, b, 2*v+2, mid, r);
    }
}
```
