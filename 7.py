import random

# Genetic Algorithm Parameters
population_size = 10
chromosome_length = 8
mutation_rate = 0.1
crossover_rate = 0.7
generations = 100

# Target binary string
target = "11011010"

# Generate initial population
def initialize_population():
    return [''.join(random.choice('01') for _ in range(chromosome_length)) for _ in range(population_size)]

# Fitness function (number of matching bits with the target)
def calculate_fitness(individual):
    return sum(c1 == c2 for c1, c2 in zip(individual, target))

# Selection: Tournament selection
def tournament_selection(population, tournament_size):
    selected = []
    for _ in range(population_size):
        participants = random.sample(population, tournament_size)
        winner = max(participants, key=calculate_fitness)
        selected.append(winner)
    return selected

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation: Flip a bit with a certain probability
def mutate(individual):
    mutated = ''.join('1' if bit == '0' else '0' if bit == '1' and random.random() <= mutation_rate else bit for bit in individual)
    return mutated

# Main Genetic Algorithm
def genetic_algorithm():
    population = initialize_population()

    for generation in range(generations):
        # Evaluate fitness of each individual
        fitness_scores = [calculate_fitness(individual) for individual in population]

        # Select parents using tournament selection
        parents = tournament_selection(population, 3)

        # Create next generation through crossover and mutation
        next_generation = []

        for i in range(0, population_size, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]

            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            child1 = mutate(child1)
            child2 = mutate(child2)

            next_generation.extend([child1, child2])

        # Replace the old population with the new one
        population = next_generation

        # Check for convergence
        if any(fitness == chromosome_length for fitness in fitness_scores):
            print("Target reached in generation", generation)
            break

    best_individual = max(population, key=calculate_fitness)
    print("Best individual:", best_individual)

# Run the genetic algorithm
genetic_algorithm()
