# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond

Template for exercise 1
(genetic algorithm module specification)
"""
import mastermind as mm
import random

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm 

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher, the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GASolver:
    def __init__(self, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size):
            # Generate a random chromosome for a new individual
            chromosome = MATCH.generate_random_guess()
            
            # Evaluate the fitness of the generated chromosome
            fitness = MATCH.rate_guess(chromosome)
            
            # Create a new individual with the generated chromosome and its fitness
            new_individual = Individual(chromosome, fitness)
            
            # Add the new individual to the population
            self._population.append(new_individual)
    
    
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
        self._population.sort(reverse=True)
        # Calculate the size of the selection based on the selection rate
        selection_size = int(len(self._population) * self._selection_rate)
        # Calculate the number of individuals to be removed
        removed_selection_size = len(self._population) - selection_size
        # Keep only the top selection_size individuals
        self._population = self._population[:selection_size]
        # Initialize a set to keep track of used pairs
        used_pairs = set()

        for i in range(removed_selection_size):
            while True:
                # Randomly select two parents from the population
                a = self._population[random.randrange(0, len(self._population))]
                b = self._population[random.randrange(0, len(self._population))]
                # Ensure the pair (a, b) has not been used before
                if (a, b) not in used_pairs:
                    used_pairs.add((a, b))
                    break

            # Perform crossover at a random point
            x_point = random.randrange(0, len(a.chromosome))        
            new_chrom = a.chromosome[0:x_point] + b.chromosome[x_point:]

            # Apply mutation with a certain probability
            if random.random() < self._mutation_rate:
                valid_colors = mm.get_possible_colors()
                new_gene = random.choice(valid_colors)
                pos = random.randrange(0, len(new_chrom))
                new_chrom[pos] = new_gene

            # Create a new individual with the new chromosome and its fitness
            new_individual = Individual(new_chrom, MATCH.rate_guess(new_chrom))
            # Add the new individual to the population
            self._population.append(new_individual)    

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        pass  # REPLACE WITH YOUR CODE

    def get_best_individual(self):
        """ Return the best Individual of the population """
        self._population.sort(reverse=True)
        return self._population[0]

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        for i in range(max_nb_of_generations):
            # Evolve the population for one generation
            self.evolve_for_one_generation()
            # Get the best individual in the current population
            best = self.get_best_individual()
            # Get the fitness of the best individual
            fitness = best.fitness
            # Check if the fitness meets or exceeds the threshold
            if fitness >= threshold_fitness:
                return best
        # Return the best individual after the maximum number of generations
        return self.get_best_individual()

MATCH = mm.MastermindMatch(secret_size=4)
solver = GASolver()
solver.reset_population()
solver.evolve_until(threshold_fitness=MATCH.max_score())
best = solver.get_best_individual()
print(f"Best guess {best.chromosome}")
print(f"Problem solved? {MATCH.is_correct(best.chromosome)}")