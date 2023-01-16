import random

import networkx as nx
import matplotlib.pyplot as plt

import numpy as np

def generate_random_adjacency_matrix(n, min, max):

    adjacency_matrix = [ [0 for i in range(n)] for j in range(n) ]
    
    for i in range(n):
        degree = 0
        while degree < 2 or degree > max:

            for j in range(n):
                if i != j:
                    r = np.random.random()
                    if r < 0.5 and degree < 2 :
                        adjacency_matrix[i][j] = 1
                        adjacency_matrix[j][i] = 1
                        degree += 1
                    elif r < 0.5 and degree < max:
                        adjacency_matrix[i][j] = 1
                        adjacency_matrix[j][i] = 1
                        degree += 1
    return adjacency_matrix

def generate_population(graph, size, n_colors):
    population = []
    for i in range(size):
        # Create a random coloring of the graph
        individual = [random.randint(0,n_colors) for i in range(len(graph[0]))]



        population.append(individual)
    return population

def max_colors(graph):

    max_degree = 0

    for i in range(len(graph[0])):
        degree = 0
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                degree +=1
        
        if degree > max_degree:
            max_degree = degree

    return max_degree + 1

def select_parents_propotional(population):
    parents = []
    for i in range(2):
        r = random.random()
        total = 0
        for individual in population:
            total += individual[1]
            if total > r:
                parents.append(individual)
                break
    return parents

def evaluate_fitness(individual, graph):

    conflicts = count_color_conflicts(individual, graph)

    if conflicts == 0:
        return 1 + 1/count_colors(individual)

    return 1/conflicts + 1/count_colors(individual)

def count_colors(individual):
    return len(set(individual))

def count_color_conflicts(individual, graph):
    conflicts = 0
    for i in range(len(graph[0])):
        for j in range(len(graph[0])):
            if graph[i][j] == 1 and individual[i] == individual[j]:
                conflicts += 1
    return conflicts


def one_point_cross_over(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)

    child1 = parent1[:crossover_point] + parent2[crossover_point:]

    
    return child1
    
def two_point_cross_over(parent1, parent2):
    crossover_point1 = random.randint(1, len(parent1)-2)
    crossover_point2 = random.randint(crossover_point1+1, len(parent1)-1)

    child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    
    return child1

def even_crossover(parent1, parent2):
    child1 = []
    for i in range(len(parent1)):
        if i % 2 == 0:
            child1.append(parent1[i])
        else:
            child1.append(parent2[i])
    return child1

def probability_mutation(individual, probability=0.1):
    for i in range(len(individual)):
        if random.random() < probability:
            individual[i] = random.randint(0, max(individual))

def swap_mutation(individual):
    index1 = random.randint(0, len(individual)-1)
    index2 = random.randint(0, len(individual)-1)
    individual[index1], individual[index2] = individual[index2], individual[index1]


def draw_graph(graph):
    G = nx.Graph()
    for i in range(len(graph)):
        G.add_node(i)
        for j in range( len(graph)-i):
            if graph[j][i] == 1:
                G.add_edge(j, i)

    nx.draw(G, with_labels=True)
    plt.show()

def draw_graph_with_colors(graph, colors):

    G = nx.Graph()
    for i in range(len(graph)):
        G.add_node(i, color=ids_to_colors(colors)[i])
        for j in range( len(graph)-i):
            if graph[j][i] == 1:
                G.add_edge(j, i)

    nx.draw(G, with_labels=True, node_color=[G.nodes[i]['color'] for i in G.nodes])
    plt.show()

def genetic_algorithm(graph, population_size, generation_amount, max_colors, crossover_function,  mutation_function, local_improvement_function):
    population = generate_population(graph, population_size, max_colors)

    for i in range(generation_amount):
        population = sorted(population, key=lambda x: evaluate_fitness(x, graph), reverse=True)

        for i in range(population_size):
            parents = select_parents_propotional(population)
            child1= crossover_function(parents[0], parents[1])
            mutation_function(child1)

            if evaluate_fitness(child1, graph) > evaluate_fitness(population[-1], graph):
                population[-1] = child1
                population = sorted(population, key=lambda x: evaluate_fitness(x, graph), reverse=True)

    population = sorted(population, key=lambda x: evaluate_fitness(x, graph), reverse=True)
    return population[0]

def local_improvement_random(individual, graph):
    for i in range(len(individual)):
        individual[i] = random.randint(0, max_colors)
        if count_color_conflicts(individual, graph) == 0:
            return individual
    return individual

def local_improvement_hill_climbing(individual, graph):
    ind = individual.copy()
    for i in range(len(ind)):
        for j in range(1, max_colors):
            ind[i] = j
            if count_color_conflicts(ind, graph) == 0:
                return ind
    return individual

def ids_to_colors(ids):
    colors = []
    for id in ids:
        colors.append(id_to_color(id))
    return colors

def id_to_color(id):
    if id == 0:
        return 'red'
    elif id == 1:
        return 'green'
    elif id == 2:
        return 'blue'
    elif id == 3:
        return 'yellow'
    elif id == 4:
        return 'orange'
    elif id == 5:
        return 'purple'
    elif id == 6:
        return 'pink'
    elif id == 7:
        return 'aqua'
    elif id == 8:
        return 'brown'
    elif id == 9:
        return 'grey'
    elif id == 10:
        return 'cyan'
    elif id == 11:
        return 'magenta'
    elif id == 12:
        return 'lime'
    elif id == 13:
        return 'olive'
    elif id == 14:
        return 'teal'
    elif id == 15:
        return 'coral'
    elif id == 16:
        return 'gold'
    elif id == 17:
        return 'khaki'
    elif id == 18:
        return 'maroon'
    elif id == 19:
        return 'navy'
    elif id == 20:
        return 'plum'
    elif id == 21:
        return 'salmon'
    elif id == 22:
        return 'sienna'
    elif id == 23:
        return 'tan'
    elif id == 24:
        return 'violet'
    elif id == 25:
        return 'wheat'

graph = generate_random_adjacency_matrix(300, 2, 30)
g1= graph.copy()


draw_graph(graph)

population_size = 20
generation_amount = 50
max_colors = max_colors(graph)

population = generate_population(graph, population_size, max_colors)


solution = genetic_algorithm(graph, population_size, generation_amount, max_colors, even_crossover, swap_mutation, local_improvement_hill_climbing)


# draw_graph_with_colors(graph, solution)

print(solution)
