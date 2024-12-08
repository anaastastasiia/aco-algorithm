import numpy as np
import random

class AntColony:
    def __init__(self, distances, num_ants, num_iterations, alpha, beta, rho):
        self.distances = distances
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha 
        self.beta = beta
        self.rho = rho
        self.num_cities = len(distances)
        self.pheromones = np.ones((self.num_cities, self.num_cities))  
        self.best_path = None
        self.best_length = float('inf')

    def _calculate_probabilities(self, ant_position):
        probabilities = np.zeros(self.num_cities)
        current_city = ant_position[-1]
        total = 0

        for i in range(self.num_cities):
            if i not in ant_position:
                pheromone = self.pheromones[current_city][i] ** self.alpha
                distance = self.distances[current_city][i] ** (-self.beta)
                probabilities[i] = pheromone * distance
                total += probabilities[i]

        probabilities /= total
        return probabilities

    def _choose_next_city(self, probabilities):
        return np.random.choice(range(self.num_cities), p=probabilities)

    def _update_pheromones(self, paths, lengths):
        for i in range(len(paths)):
            path = paths[i]
            length = lengths[i]
            for j in range(len(path) - 1):
                self.pheromones[path[j], path[j+1]] += 1 / length

        self.pheromones *= (1 - self.rho)

    def solve(self):
        for iteration in range(self.num_iterations):
            paths = []
            lengths = []
            for ant in range(self.num_ants):
                ant_position = [random.randint(0, self.num_cities - 1)]
                while len(ant_position) < self.num_cities:
                    probabilities = self._calculate_probabilities(ant_position)
                    next_city = self._choose_next_city(probabilities)
                    ant_position.append(next_city)

                path_length = sum(self.distances[ant_position[i], ant_position[i + 1]] for i in range(self.num_cities - 1))
                paths.append(ant_position)
                lengths.append(path_length)

                if path_length < self.best_length:
                    self.best_length = path_length
                    self.best_path = ant_position

            self._update_pheromones(paths, lengths)

        return self.best_path, self.best_length
