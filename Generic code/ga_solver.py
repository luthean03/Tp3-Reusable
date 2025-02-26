# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import tsp_problem
import mastermind_problem
import random
import cities

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""
    def initialize_population(self, pop_size: int) -> list:
            """Initializes a population of individuals for the problem
    
            Args:
                pop_size (int): number of individuals in the population
    
            Returns:
                list: list of Individuals
            """
            raise NotImplementedError

    def evaluate_fitness(self, individual: Individual) -> float:
            """Evaluates the fitness of an individual for the problem
    
            Args:
                individual (Individual): the individual to evaluate
    
            Returns:
                float: the fitness of the individual
            """
            raise NotImplementedError
    
    def crossover(self, parent1: Individual, parent2: Individual) -> tuple:
            """Applies the crossover operator to two parents and returns two children
    
            Args:
                parent1 (Individual): first parent
                parent2 (Individual): second parent
    
            Returns:
                tuple: two children resulting from the crossover
            """
            raise NotImplementedError
    
    def mutate(self, individual: Individual):
        """Applies the mutation operator to an individual
    
         Args:
            individual (Individual): the individual to mutate
        """
        raise NotImplementedError


class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        self._population = self._problem.initialize_population(self._pop_size)

    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        # Step 1: Evaluate fitness
        for individual in self._population:
            individual.fitness = self._problem.evaluate_fitness(individual)

        # Step 2: Selection (keep the best individuals)
        self._population.sort(reverse=True)  # Sort by fitness descending
        num_survivors = int(self._selection_rate * len(self._population))
        survivors = self._population[:num_survivors]

        # Step 3: Reproduction (crossover)
        new_population = survivors[:]
        while len(new_population) < self._pop_size:
            p1, p2 = random.sample(survivors, 2)
            if random.random() < 0.7:  # 70% chance of crossover
                child1, child2 = self._problem.crossover(p1, p2)
                new_population.extend([child1, child2])

        # Step 4: Mutation
        for individual in new_population:
            if random.random() < self._mutation_rate:
                self._problem.mutate(individual)

        self._population = new_population[:self._pop_size]

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        best_individual = max(self._population, key=lambda ind: ind.fitness)
        print(f"Best fitness: {best_individual.fitness:.2f}, Population Avg: {sum(ind.fitness for ind in self._population) / len(self._population):.2f}")

    def get_best_individual(self):
        """ Return the best Individual of the population """
        return max(self._population, key=lambda ind: ind.fitness)

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        self.reset_population()

        for generation in range(max_nb_of_generations):
            print(f"Generation {generation}")
            self.evolve_for_one_generation()
            self.show_generation_summary()

            best_individual = self.get_best_individual()
            if threshold_fitness is not None and best_individual.fitness >= threshold_fitness:
                print(f"Threshold fitness {threshold_fitness} reached at generation {generation}!")
                break

        return self.get_best_individual()

city_dict = cities.load_cities("Traveling/cities.txt")
solver = GASolver(tsp_problem)
solver.reset_population()
solver.evolve_until()
best = solver.get_best_individual()
cities.draw_cities(city_dict, best.chromosome)

MATCH = mm.MastermindMatch(secret_size=4)
solver = GASolver(mastermind_problem)
solver.reset_population()
solver.evolve_until(threshold_fitness=MATCH.max_score())
best = solver.get_best_individual()
print(f"Best guess {best.chromosome}")
print(f"Problem solved? {MATCH.is_correct(best.chromosome)}")