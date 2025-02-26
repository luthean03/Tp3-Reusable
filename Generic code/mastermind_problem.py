# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem
import mastermind as mm


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    
    def __init__(self, match: mm.MastermindMatch):
            """Initializes a MastermindProblem instance
    
            Args:
                match (MastermindMatch): a MastermindMatch instance
            """
            self._match = match
    
    def initialize_population(self, pop_size: int):
            """Initializes a population of individuals for the problem
    
            Args:
                pop_size (int): number of individuals in the population
    
            Returns:
                list: list of Individuals
            """
            population = []
            for i in range(pop_size):
                chromosome = self._match.generate_random_guess()
                fitness = self._match.rate_guess(chromosome)
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

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem(match)
    solver = GASolver(problem)

    solver.reset_population()
    solver.evolve_until()

    print(
        f"Best guess {mm.decode_guess(solver.getBestDNA())} {solver.get_best_individual()}")
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")
