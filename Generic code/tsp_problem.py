# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from ga_solver import GAProblem
import cities

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
        
    def __init__(self):
            """Initializes a TSProblem instance"""
            pass
    
    def initialize_population(self, pop_size: int):
            """Initializes a population of individuals for the problem
    
            Args:
                pop_size (int): number of individuals in the population
    
            Returns:
                list: list of Individuals
            """
            population = []
            city_dict = cities.load_cities("cities.txt")
            for i in range(pop_size):
                chromosome = cities.default_road(city_dict)
                random.shuffle(chromosome)
                fitness = - cities.road_length(city_dict, chromosome)
                individual = Individual(chromosome, fitness)
                population.append(individual)
            return population
        
    def evaluate_fitness(self, individual: 'Individual'):
            """Evaluates the fitness of an individual for the problem
    
            Args:
                individual (Individual): the individual to evaluate
    
            Returns:
                float: the fitness of the individual
            """
            return individual.fitness


if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = cities.load_cities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    cities.draw_cities(city_dict, solver.getBestIndiv().chromosome)
