## Description
The `ga_solver.py` file contains a generic implementation of a Genetic Algorithm (GA) to solve various optimization problems. It defines the `Individual`, `GAProblem`, and `GASolver` classes, which can be used to create and solve optimization problems using genetic algorithms.

## Classes
### Individual
The `Individual` class represents an individual in a genetic algorithm. Each individual has a chromosome (a list of genes) and a fitness value (a measure of the individual's quality).
#### Methods
- `__init__(self, chromosome: list, fitness: float)`: Initializes an individual with a chromosome and a fitness value.
- `__lt__(self, other)`: Implements the "less than" comparison operator based on fitness value.
- `__repr__(self)`: Representation of the object for print calls.

### GAProblem
The `GAProblem` class defines a genetic algorithm problem to be solved by `GASolver`. This class is an abstract base class and must be extended to define specific problems.
#### Methods
- `generate_random_individual(self)`: Generates a random individual.
  - Returns a tuple containing a genome (list) and a fitness value (float).
- `crossover(self, parent1, parent2)`: Performs crossover between two parents to produce a new individual.
  - `parent1` (list): Chromosome of the first parent.
  - `parent2` (list): Chromosome of the second parent.
  - Returns a new chromosome (list).
- `mutate(self, chromosome)`: Mutates a given individual.
  - `chromosome` (list): The chromosome to mutate.
  - Returns a mutated chromosome (list).
- `evaluate_fitness(self, chromosome)`: Evaluates the fitness value of a given individual.
  - `chromosome` (list): The chromosome to evaluate.
  - Returns the fitness value (float).

### GASolver
The `GASolver` class implements the genetic algorithm to solve a problem defined by a subclass of `GAProblem`.
#### Methods
- `__init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1)`: Initializes a `GASolver` instance for a given problem with specified selection and mutation rates.
  - `problem` (GAProblem): The problem to be solved by this genetic algorithm.
  - `selection_rate` (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
  - `mutation_rate` (float, optional): Mutation rate between 0 and 1.0. Defaults to 0.1.
- `reset_population(self, pop_size=50)`: Initializes the population with random individuals.
  - `pop_size` (int, optional): Population size. Defaults to 50.
- `evolve_for_one_generation(self)`: Applies the evolution process for one generation.
- `show_generation_summary(self, generation)`: Displays debugging information about the current state of the population.
  - `generation` (int): The current generation number.
- `get_best_individual(self)`: Returns the best individual in the population.
  - Returns an `Individual` object.
- `evolve_until(self, max_nb_of_generations=500, threshold_fitness=None)`: Runs the `evolve_for_one_generation` function until one of two conditions is met: the maximum number of generations is reached or the best individual's fitness value is greater than or equal to `threshold_fitness`.
  - `max_nb_of_generations` (int, optional): Maximum number of generations. Defaults to 500.
  - `threshold_fitness` (float, optional): Fitness threshold value. Defaults to None.

## Usage
To use this module, a subclass of `GAProblem` must be created that implements the abstract methods. In this subclass, it is necessary to define how various methods will be handled, such as how mutation will be managed. Then, an instance of `GASolver` can be created with the problem, and its methods can be used to solve the problem.

Example usage:

```python
from ga_solver import GASolver, GAProblem

class MyProblem(GAProblem):
    def generate_random_individual(self):
        # Specific implementation
        pass

    def crossover(self, parent1, parent2):
        # Specific implementation
        pass

    def mutate(self, chromosome):
        # Specific implementation
        pass

    def evaluate_fitness(self, chromosome):
        # Specific implementation
        pass

problem = MyProblem()
solver = GASolver(problem)
solver.reset_population()
solver.evolve_until()
best_individual = solver.get_best_individual()
print(f'Best Individual: {best_individual}')
