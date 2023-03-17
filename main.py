import random

weights = [1, 2, 3, 4, 5]
values = [10, 11, 12, 13, 14]
max_weight = 10
population_size = 5
gen_num = 100

population = []  # empty population list initialization
for i in range(population_size):
    answer = [random.randint(0, 1) for j in
              range(len(weights))]  # create answers in a list which its length=weights length that containts 0s and 1s
    population.append(answer)  # add at the end of population list


# make sure total weight isn't bigger than max weight and get total values (fitness)
def fitness(answer):
    total_weights = sum([weights[i] for i in range(len(answer)) if answer[i] == 1])
    if total_weights > max_weight:
        return 0
    else:
        total_values = sum([values[i] for i in range(len(answer)) if answer[i] == 1])
        return total_values


# Select parents for reproduction: Select pairs of parents to produce offspring for the next generation. You can use
# different selection methods, such as tournament selection or roulette wheel selection.
for generation in range(gen_num):  # calculate fitness for each answer
    fitnesses = [fitness(answer) for answer in population]
parents = []  # define parents in an empty list
for i in range(
        population_size):  # start picking random samples from the population list using the roulette wheel method
    total_fitness = sum(fitnesses)
    fitness_proportion = [fitness / total_fitness for fitness in fitnesses]  # calculates the proportion for the finess
    cumulative_proportions = [sum(fitness_proportion[:j + 1]) for j in range(population_size)]  # like the table in
    # lecture and the sum=1 to determine the probability of selecting each individual. and which has the higher
    # chance of getting picked
    random_num1 = random.uniform(0, 1)
    random_num2 = random.uniform(0, 1)  # Generate a random number between 0 and 1 (cant be 1 in uniform)
    parent1 = population[next(j for j in range(population_size) if cumulative_proportions[j] >= random_num1)]
    parent2 = population[next(j for j in range(population_size) if cumulative_proportions[j] >= random_num2)]
    parents.append([parent1, parent2])
# crossover and mutation
offspring = []
for i in range(population_size):
    parent1, parent2 = parents[i]  # combine them into 1
    crossover_point = random.randint(0, len(weights) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]  # makes child a combination of parent 1 and 2 now
    # mutation
    mutation_point = random.randint(0, len(weights) - 1)  # now switch 1s to 0s and vice versa
    if child[mutation_point] == 1:
        child[mutation_point] = 0
    else:
        child[mutation_point] = 1
        # now add child to offspring
    offspring.append(child)

    # get fitnesses for children
offspring_fitnesses = [fitness(answer) for answer in offspring]
# start creating next generations
next_gen = []
for i in range(population_size):
    if fitnesses[i] > offspring_fitnesses[i]:  # if the fitness is better you pick it in the next generation
        next_gen.append(population[i])
    else:
        next_gen.append(offspring[i])
        # turn the population into the new generation
population = next_gen
# print
best_solution = max(population, key=fitness)
best_fitness = fitness(best_solution)
print("Best solution found:", best_solution)
print("Fitness of best solution:", best_fitness)
