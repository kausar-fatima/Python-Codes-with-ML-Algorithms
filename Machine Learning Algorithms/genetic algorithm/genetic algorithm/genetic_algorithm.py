import random

# Genetic Algorithm parameters
POPULATION_SIZE = 4
MUTATION_RATE = 0.1

# Generate a random board state
# function generates a random placement of queens on the chessboard, 
# where each queen is assigned a random row position in its respective column.
def generate_board_state():
    board_state = [random.randint(0, 7) for _ in range(8)]
    return board_state

# Calculate the fitness of a board state
def calculate_fitness(board_state):
    conflicts = 0
    for i in range(8): # This initiates an outer loop that iterates over each column (queen) 
        for j in range(i + 1, 8):# This initiates an inner loop that iterates over 
                                 # each subsequent column (queen) to the right of the current one.

            # The first condition (board_state[i] == board_state[j]) checks for row conflicts. 
            # The second condition (abs(board_state[i] - board_state[j]) == j - i) checks for diagonal conflicts.
            if board_state[i] == board_state[j] or abs(board_state[i] - board_state[j]) == j - i:
                conflicts += 1
    return 30 - conflicts  # Max fitness = 28 (no conflicts)

# Select parents for crossover using tournament selection
def tournament_selection(population):
    tournament_size = 3
    # Randomly selects tournament_size individuals from the population.
    tournament = random.sample(population, tournament_size)
    #  Returns the individual from the tournament with the highest fitness. 
    return max(tournament, key=lambda x: x[1])

# Crossover operation (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, 7)
    # takes the first part of parent1 up to the crossover_point and 
    # combines it with the second part of parent2 from the crossover_point
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutation operation (swap two positions)
def mutate(board_state):
    # Randomly selects two positions (pos1 and pos2) from the range 0 to 7 (inclusive)
    pos1, pos2 = random.sample(range(8), 2)
     # Swaps the values at positions pos1 and pos2 in the board_state list
    board_state[pos1], board_state[pos2] = board_state[pos2], board_state[pos1]
    return board_state

# Print the chessboard
def print_chessboard(board_state):
    for row in range(8):
        line = "|"
        for col in range(8):
            line += " Q |" if board_state[col] == row else "   |"
        print("-" * 33)
        print(line)
    print("-" * 33)

# Generate the initial population
population = [(generate_board_state(), 0) for _ in range(POPULATION_SIZE)]

# Main Genetic Algorithm loop
generation = 0
while True:
    # Calculate fitness for each board state
    population = [(board_state, calculate_fitness(board_state)) for board_state, _ in population]
    
    print(f"Processing generation {generation}")
    # Check if at least three individuals have fitness >= 27
    count_high_fitness = sum(1 for _, fitness in population if fitness >= 27)
    if count_high_fitness >= 3:
        print(f"At least three individuals have fitness >= 27 in generation {generation}")
        
        # Print the best solution
        for i,j in population:
            print_chessboard(i)
            print('fitness: '+str(j))
        break

    # Create the next generation
    new_population = []

    # Elitism: Keep the best board state from the previous generation
    new_population.append(max(population, key=lambda x: x[1]))

    # Perform selection, crossover, and mutation
    while len(new_population) < POPULATION_SIZE:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child = crossover(parent1[0], parent2[0])
        if random.random() < MUTATION_RATE: # line checks whether a randomly generated number (between 0.0 and 1.0)
                                            # is less than the specified MUTATION_RATE
            child = mutate(child)
        new_population.append((child, 0))

    # Update the population
    population = new_population

    generation += 1
    if(generation==1001):    # check condition to terminate the loop
        print('generation limit has reached 1000')
        break



