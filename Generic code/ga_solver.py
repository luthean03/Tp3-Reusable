# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import random


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher the value, the better the fitness)
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

    def generate_random_individual(self):
        """Generates a random individual"""
        raise NotImplementedError

    def crossover(self, parent1, parent2):
        """Performs crossover between two parents to produce a new chromosome"""
        raise NotImplementedError

    def mutate(self, chromosome):
        """Mutates a given chromosome"""
        raise NotImplementedError

    def evaluate_fitness(self, chromosome):
        """Evaluates the fitness of a given chromosome"""
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
        """Initialize the population with pop_size random Individuals"""
        self._population = [
            Individual(*self._problem.generate_random_individual())
            for _ in range(pop_size)
        ]

    def evolve_for_one_generation(self):
        """Apply the process for one generation"""
        self._population.sort(reverse=True)
        selection_size = int(len(self._population) * self._selection_rate)
        removed_selection_size = len(self._population) - selection_size
        self._population = self._population[:selection_size]
        used_pairs = set()

        for _ in range(removed_selection_size):
            while True:
                parent1 = self._population[random.randrange(0, len(self._population))]
                parent2 = self._population[random.randrange(0, len(self._population))]
                if (parent1, parent2) not in used_pairs:
                    used_pairs.add((parent1, parent2))
                    break
            new_chrom = self._problem.crossover(parent1.chromosome, parent2.chromosome)
            if random.random() < self._mutation_rate:
                new_chrom = self._problem.mutate(new_chrom)
            new_individual = Individual(new_chrom, self._problem.evaluate_fitness(new_chrom))
            self._population.append(new_individual)

    def show_generation_summary(self,generation):
        """Print some debug information on the current state of the population"""
        best_individual = self.get_best_individual()
        print(f'Best Individual for generation {generation}: chromosome {best_individual.chromosome} fitness {best_individual.fitness}')

    def get_best_individual(self):
        """Return the best Individual of the population"""
        return max(self._population, key=lambda indiv: indiv.fitness)

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """Launch the evolve_for_one_generation function until one of the two conditions is achieved"""
        for generation in range(max_nb_of_generations):
            self.evolve_for_one_generation()
            self.show_generation_summary(generation)
            best_individual = self.get_best_individual()
            if threshold_fitness is not None and best_individual.fitness >= threshold_fitness:
                break