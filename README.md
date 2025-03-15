## Description
Ce fichier `ga_solver.py` contient une implémentation générique d'un algorithme génétique (GA) pour résoudre divers problèmes d'optimisation. Il définit les classes `Individual`, `GAProblem`, et `GASolver` qui peuvent être utilisées pour créer et résoudre des problèmes d'optimisation en utilisant des algorithmes génétiques.

## Classes
### Individual
La classe `Individual` représente un individu dans un algorithme génétique. Chaque individu a un chromosome (une liste de gènes) et une valeur de fitness (une mesure de la qualité de l'individu).
#### Méthodes
- `__init__(self, chromosome: list, fitness: float)`: Initialise un individu avec un chromosome et une valeur de fitness.
- `__lt__(self, other)`: Implémente l'opérateur de comparaison "moins que" basé sur la valeur de fitness.
- `__repr__(self)`: Représentation de l'objet pour les appels print.

### GAProblem
La classe `GAProblem` définit un problème d'algorithme génétique à résoudre par `GASolver`. Cette classe est une classe de base abstraite et doit être étendue pour définir des problèmes spécifiques.
#### Méthodes
- `generate_random_individual(self)`: Génère un individu aléatoire.
  - Retourne un tuple contenant un génome (list) et une valeur de fitness (float).
- `crossover(self, parent1, parent2)`: Effectue un croisement entre deux parents pour produire un nouvel individu.
  - `parent1` (list): Le chromosome du premier parent.
  - `parent2` (list): Le chromosome du deuxième parent.
  - Retourne un nouveau chromosome (list).
- `mutate(self, chromosome)`: Muter un individu donné.
  - `chromosome` (list): Le chromosome à muter.
  - Retourne un chromosome muté (list).
- `evaluate_fitness(self, chromosome)`: Évalue la valeur de fitness d'un individu donné.
  - `chromosome` (list): Le chromosome à évaluer.
  - Retourne la valeur de fitness (float).

### GASolver
La classe `GASolver` implémente l'algorithme génétique pour résoudre un problème défini par une sous-classe de `GAProblem`.
#### Méthodes
- `__init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1)`: Initialise une instance de `GASolver` pour un problème donné avec des taux de sélection et de mutation spécifiés.
  - `problem` (GAProblem): Le problème à résoudre par cet algorithme génétique.
  - `selection_rate` (float, optionnel): Taux de sélection entre 0 et 1.0. Par défaut à 0.5.
  - `mutation_rate` (float, optionnel): Taux de mutation entre 0 et 1.0. Par défaut à 0.1.
- `reset_population(self, pop_size=50)`: Initialise la population avec des individus aléatoires.
  - `pop_size` (int, optionnel): Taille de la population. Par défaut à 50.
- `evolve_for_one_generation(self)`: Applique le processus d'évolution pour une génération.
- `show_generation_summary(self, generation)`: Affiche des informations de débogage sur l'état actuel de la population.
  - `generation` (int): Le numéro de la génération actuelle.
- `get_best_individual(self)`: Retourne le meilleur individu de la population.
  - Retourne un objet `Individual`.
- `evolve_until(self, max_nb_of_generations=500, threshold_fitness=None)`: Lance la fonction `evolve_for_one_generation` jusqu'à ce que l'une des deux conditions soit remplie : le nombre maximum de générations est atteint ou la valeur de fitness du meilleur individu est supérieure ou égale à `threshold_fitness`.
  - `max_nb_of_generations` (int, optionnel): Nombre maximum de générations. Par défaut à 500.
  - `threshold_fitness` (float, optionnel): Valeur de fitness seuil. Par défaut à None.


## Utilisation
Pour utiliser ce module, il faut créer une sous-classe de `GAProblem` qui implémente les méthodes abstraites. Dans cette sous-classe, il faut définir la façon dont vont être gérée les différentes méthode, par exemple comment va être gerer la mutation. Ensuite, on peut créer une instance de `GASolver` avec le problème et utiliser les méthodes pour résoudre le problème.
Exemple d'utilisation :

```python
from ga_solver import GASolver, GAProblem

class MyProblem(GAProblem):
    def generate_random_individual(self):
        # Implémentation spécifique
        pass

    def crossover(self, parent1, parent2):
        # Implémentation spécifique
        pass

    def mutate(self, chromosome):
        # Implémentation spécifique
        pass

    def evaluate_fitness(self, chromosome):
        # Implémentation spécifique
        pass

problem = MyProblem()
solver = GASolver(problem)
solver.reset_population()
solver.evolve_until()
best_individual = solver.get_best_individual()
print(f'Best Individual: {best_individual}')
```
