import numpy as np

# Objective function
def objective_function(x):
    return x**2 + 4*x - 4

# Genetic Algorithm Parameters
population_size = 100
generations = 50
mutation_rate = 0.1

# Initialization
population = np.random.uniform(low=-10, high=10, size=population_size)

#Genetic Algorithm 
for generation in range(generations):
    # Evaluate fitness
    fitness_scores = objective_function(population)
    
    # Selection
    selected_indices = np.argsort(fitness_scores)[-population_size//2:]
    selected_population = population[selected_indices]
    
    # Crossover
    offspring = np.concatenate([np.random.choice(selected_population, size=2) for _ in range(population_size//2)])
    
    # Mutation
    mutation_mask = np.random.rand(population_size) < mutation_rate
    offspring += mutation_mask * np.random.uniform(low=-1, high=1, size=population_size)
    
    # Update population 
    population = np.concatenate([selected_population, offspring])

# Find the best solution
best_solution = population[np.argmax(objective_function(population))]

print("Best solution:", best_solution)
print("Maximum value:", objective_function(best_solution))
