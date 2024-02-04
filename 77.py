import random

def generate_population(population_size, string_length):
    return ["".join(random.choice('01') for _ in range(string_length)) for _ in range(population_size)]

def fitness(individual, target):
    return sum(1 for a, b in zip(individual, target) if a == b)

def crossover(parent1, parent2):
    split_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    mutated_individual = ''.join(
        bit if random.random() > mutation_rate else random.choice('01')
        for bit in individual
    )
    return mutated_individual

def genetic_algorithm(target, population_size, mutation_rate, generations):
    population = generate_population(population_size, len(target))

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x, target), reverse=True)
        if fitness(population[0], target) == len(target):
            print(f"Target reached in generation {generation + 1}!")
            break

        new_population = population[:2]  # Keep the top two individuals

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population[:10], k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

    best_individual = max(population, key=lambda x: fitness(x, target))
    print(f"Best individual: {best_individual}, Fitness: {fitness(best_individual, target)}")

target_string = '1010101010101010'
genetic_algorithm(target_string, population_size=100, mutation_rate=0.01, generations=1000)