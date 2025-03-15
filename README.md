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
- `crossover(self, parent1, parent2)`: Effectue un croisement entre deux parents pour produire un nouvel individu.
- `mutate(self, chromosome)`: Muter un individu donné.
- `evaluate_fitness(self, chromosome)`: Évalue la valeur de fitness d'un individu donné.

### GASolver
La classe `GASolver` implémente l'algorithme génétique pour résoudre un problème défini par une sous-classe de `GAProblem`.
#### Méthodes
- `__init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1)`: Initialise une instance de `GASolver` pour un problème donné avec des taux de sélection et de mutation spécifiés.
- `reset_population(self, pop_size=50)`: Initialise la population avec des individus aléatoires.
- `evolve_for_one_generation(self)`: Applique le processus d'évolution pour une génération.
- `show_generation_summary(self, generation)`: Affiche des informations de débogage sur l'état actuel de la population.
- `get_best_individual(self)`: Retourne le meilleur individu de la population.
- `evolve_until(self, max_nb_of_generations=500, threshold_fitness=None)`: Lance la fonction `evolve_for_one_generation` jusqu'à ce que l'une des deux conditions soit remplie : le nombre maximum de générations est atteint ou la valeur de fitness du meilleur individu est supérieure ou égale à `threshold_fitness`.

## Utilisation
Pour utiliser ce module, il faut créer une sous-classe de `GAProblem` qui implémente les méthodes abstraites. Ensuite, on peut créer une instance de `GASolver` avec le problème et utiliser les méthodes pour résoudre le problème.
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
