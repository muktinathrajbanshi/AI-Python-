import random

# Define the two locations A and B as integers
A = 1
B = 0

# Define a function to print the current state of the environment
def print_environment(state):
    print(f"Location A: {state[A]}")
    print(f"Location B: {state[B]}")
    print("")

# Define a function to check if the environment is clean
def is_clean(state):
    return state[A] == 0 and state[B] == 0

# Define the main function that solves the problem
def vacuum_world():
    # Initialize the environment to a random state
    state = [0, 1] if random.random() < 0.5 else [1, 0]
    
    # Print the initial state of the environment
    print("Initial state:")
    print_environment(state)
    
    # Loop until the environment is clean
    while not is_clean(state):
        # Choose a random location to clean
        location = A if random.random() < 0.5 else B
        
        # Clean the location
        state[location] = 0
        
        # Print the new state of the environment
        print(f"Cleaned location {location}:")
        print_environment(state)
    
    # Print a message indicating that the environment is clean
    print("The environment is clean!")

# Call the vacuum_world() function
vacuum_world()
