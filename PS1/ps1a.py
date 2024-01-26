###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import functools

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows = {}
    with open(filename) as file:
        for row in file:
            name, weight = row.strip().split(",")
            cows.update({name: weight})

    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # Sort dictionary by weights
    sorted_cows = sorted(cows.items(), key= lambda item: item[1], reverse=True)
    trips = []
    # initialize list that will contain already on-board cows
    on_trip = []
    while True:
        # initialize limit
        remain_limit = limit
        # list for one trip
        trip = []
        for i in range(len(sorted_cows)):
            if int(sorted_cows[i][1]) <= remain_limit and sorted_cows[i][0] not in on_trip:
                # append cow into trip
                trip.append(sorted_cows[i][0])
                # append to already on-board cows
                on_trip.append(sorted_cows[i][0])
                # decrement limit
                remain_limit -= int(sorted_cows[i][1])
        # append trip
        trips.append(trip)

        # if all cows on-board break out of loop
        if len(on_trip) == len(sorted_cows):
            break

    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    # TODO: Your code here
    trips = []
    # Append to 'trips' all possible trips within 'limit'
    for all_trips in get_partitions(list(cows.keys())):
        # Calculate cost (total weight) of each trip
        cost = [sum([int(cows[cow]) for cow in trip]) for trip in all_trips]
        # list of booleans representing if cost of each trip is within 'limit'
        boolean_cost = [num <= limit for num in cost]
        # If all trips is within 'limit', append to list 'trips'
        if all(boolean_cost):
            trips.append(all_trips)

    # Sort all the trips according to minimum number of trips
    sorted_trips = sorted(trips, key= lambda trip: len(trip))

    # Return minimal number of trips
    return sorted_trips[0]
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    # Load data
    cows = load_cows("ps1_cow_data.txt")

    # Start timer
    start = time.time()

    # Implement greedy algorithm
    greedy = greedy_cow_transport(cows)

    # End timer
    end = time.time()

    # The time greedy algorithm took in seconds
    greedy_time = end - start

    print(f"Greedy algorithm took {greedy_time} seconds and returned {len(greedy)} trips")

    # Start timer
    start = time.time()

    # Implement brute force algorithm
    brute_force = brute_force_cow_transport(cows)

    # End timer
    end = time.time()

    # The time brute force algorithm took in seconds
    brute_time = end - start

    print(f"Brute force algorithm took {brute_time} seconds and returned {len(brute_force)} trips")


if __name__ == "__main__":
    compare_cow_transport_algorithms()