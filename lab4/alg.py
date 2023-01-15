import random

def find_greedy_solution(distances):

    start_node = random.randint(0, N-1)
    path = [start_node]
    visited = [False for _ in range(N)]
    visited[start_node] = True
    total_distance = 0
    while len(path) < N:
        next_node = None
        min_distance = float('inf')
        for i in range(N):
            if not visited[i]:
                if distances[path[-1]][i] < min_distance:
                    min_distance = distances[path[-1]][i]
                    next_node = i
        path.append(next_node)
        visited[next_node] = True
        total_distance += min_distance

    return total_distance

def choose_next_random_node(start_node, visited, distances, ):
    next_node = random.randint(0,249)

    while distances[start_node][next_node] == float('inf') or visited[next_node] :
        next_node = random.randint(0,249)
    return next_node

def choose_next_node_with_pheromone(start_node, visited, distances, pheromones, alpha, beta):
    next_nodes = []
    probs = []
    total_prob = 0
    for i in range(len(distances)):
        if not visited[i]:
            next_nodes.append(i)
            p = pheromones[start_node][i] ** alpha * ((1/distances[start_node][i]) ** beta)
            if p == 0:
                p = 1.5e-323
            probs.append(p)
            total_prob += p
    

    # Normalize probabilities
    for i in range(len(probs)):
        probs[i] = probs[i] / total_prob

    # choose next node based on the probabilities
    next_node = None
    
    r = random.random()

    min_p = 0
    for i in range(len(probs)):
        if r <= min_p + probs[i]:
            next_node = next_nodes[i]
            break
        else:
            min_p += probs[i]


    return next_node

def spread_pheromone(path, min_path_length, path_length, pheromones):
    delta_pheromones = min_path_length / path_length



    for i in range(len(path) - 1):
        a = path[i]
        b = path[i+1]
        pheromones[a][b] += delta_pheromones
        pheromones[b][a] += delta_pheromones


    return pheromones

def evaporate_pheromone(pheromones,p):
    for i in range(len(pheromones)):
        for j in range(len(pheromones[i])):
            pheromones[i][j] = pheromones[i][j] * (1 - p)

    return pheromones

def calculate_path_length(path, distances):
    l = 0

    for i in range(len(path)-1):
        l += distances[path[i]][path[i+1]]        

    return l


def aco_solution(M,N,alpha, beta, p, distances, iterations):
    best_solution = None
    best_solution_length = float('inf')
    min_path_length = find_greedy_solution(distances)

    print("Greedy slotution length: ", min_path_length)

    pheromones = [[1 for j in range(N)] for i in range(N)]

    for j in range(0, iterations):
        all_path = []
        for i in range(M):

            start_node = random.randint(0, N-1)

            path = [start_node]
            visited = [False for _ in range(N)]
            visited[start_node] = True

            while len(path) < N:
                if i <= 10:
                    next_node = choose_next_random_node(path[-1], visited, distances)
                else:
                    next_node = choose_next_node_with_pheromone(path[-1], visited, distances, pheromones, alpha, beta)

                visited[next_node] = True
                path.append(next_node)

            path_length = calculate_path_length(path, distances)
            pheromones = spread_pheromone(path, min_path_length, path_length, pheromones)

            all_path.append(path)

            if path_length < best_solution_length:
                best_solution = path
                best_solution_length = path_length
    

        pheromones = evaporate_pheromone(pheromones, p)

    return (best_solution, best_solution_length)




# Number of ants
M = 45
# Number of nodes
N = 250
# Random distance between nodes (1-40)
distances= [[random.randint(1,40) if i != j else float('inf') for i in range(N)] for j in range(N)]

# Parameters for the ACO algorithm
alpha = 4
beta = 2
p = 0.3

solved = aco_solution(M,N,alpha,beta, p,distances,5 )




print('ACO solution length: ',solved[1])
print('Solution: ',solved[0])

