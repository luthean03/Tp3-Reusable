# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from ga_solver import GAProblem
import cities
import random

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
        
    def __init__(self):
        pass

    def generate_random_individual(self):
        chromosome = cities.default_road(city_dict)
        fitness = - cities.road_length(city_dict, chromosome)
        return chromosome, fitness

    def evaluate_fitness(self, chromosome):
        """Evaluate the fitness of an individual"""
        return  - cities.road_length(city_dict, chromosome)

    def crossover(self, parent1, parent2):
        x_point = random.randrange(0, len(parent1))        
        new_chrom = parent1[0:x_point] + [gene for gene in parent2 if gene not in parent1[0:x_point]]
        return new_chrom

    def mutate(self, chromosome):
        """Mutate an individual"""
        # Swap two genes in the chromosome
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
        return chromosome

if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = cities.load_cities("Traveling/cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    cities.draw_cities(city_dict, solver.get_best_individual().chromosome)
