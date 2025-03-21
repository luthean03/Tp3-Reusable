# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem
import mastermind as mm
import random


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""

    def __init__(self, match):
        self._match = match

    def generate_random_individual(self):
        chromosome = self._match.generate_random_guess()
        fitness = self._match.rate_guess(chromosome)
        return chromosome, fitness

    def evaluate_fitness(self, chromosome):
        """Evaluate the fitness of an individual"""
        return self._match.rate_guess(chromosome)

    def crossover(self, parent1, parent2):
        x_point = random.randrange(0, len(parent1))
        return parent1[:x_point] + parent2[x_point:]

    def mutate(self, chromosome):
        """Mutate an individual"""
        valid_colors = mm.get_possible_colors()
        new_gene = random.choice(valid_colors)
        pos = random.randrange(0, len(chromosome))
        chromosome[pos] = new_gene
        return chromosome


if __name__ == '__main__':
    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem(match)
    solver = GASolver(problem)

    solver.reset_population()
    solver.evolve_until()

    print(f"Best guess {mm.encode_guess(solver.get_best_individual().chromosome)} {solver.get_best_individual()}")
    print(f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")