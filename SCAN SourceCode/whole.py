import random

# Constants
DISK_SIZE = 200
INITIAL_HEAD_POSITION = 50

def generate_requests(n):
    """ Generate 'n' random disk requests. """
    return random.sample(range(DISK_SIZE), n)

def scan_algorithm(requests, initial_position):
    """ Implement the SCAN disk scheduling algorithm. """
    requests.sort()
    left = [r for r in requests if r < initial_position]
    right = [r for r in requests if r >= initial_position]
    schedule = right + left[::-1]  # Moving towards the end (right) first
    return schedule

def c_scan_algorithm(requests, initial_position):
    """ Implement the C-SCAN disk scheduling algorithm. """
    requests.sort()
    left = [r for r in requests if r < initial_position]
    right = [r for r in requests if r >= initial_position]
    schedule = right + [DISK_SIZE - 1] + [0] + left  # Only moving in one direction and jump back to start
    return schedule

def c_look_algorithm(requests, initial_position):
    """ Implement the C-LOOK disk scheduling algorithm. """
    requests.sort()
    left = [r for r in requests if r < initial_position]
    right = [r for r in requests if r >= initial_position]
    schedule = right + left  # Similar to C-SCAN but without going to the end
    return schedule

def calculate_seek_time(requests, initial_position):
    """ Calculate total seek time for a given sequence of requests. """
    seek_time = 0
    current_position = initial_position
    for request in requests:
        seek_time += abs(request - current_position)
        current_position = request
    return seek_time

def calculate_worst_case_seek_time(requests, initial_position):
    """ Calculate the worst-case seek time for a given sequence of requests. """
    worst_seek_time = 0
    current_position = initial_position
    for request in requests:
        seek_time = abs(request - current_position)
        worst_seek_time = max(worst_seek_time, seek_time)
        current_position = request
    return worst_seek_time

# Running simulations for each algorithm and request size
request_sizes = [10, 20, 50, 100]
results = {}

for size in request_sizes:
    requests = generate_requests(size)
    print(f"Request Size {size}: {requests}")  # Output the random requests
    for algorithm in [scan_algorithm, c_scan_algorithm, c_look_algorithm]:
        schedule = algorithm(requests, INITIAL_HEAD_POSITION)
        seek_time = calculate_seek_time(schedule, INITIAL_HEAD_POSITION)
        worst_case_seek_time = calculate_worst_case_seek_time(schedule, INITIAL_HEAD_POSITION)
        algorithm_name = algorithm.__name__
        if algorithm_name not in results:
            results[algorithm_name] = {}
        results[algorithm_name][size] = {
            'total_seek_time': seek_time,
            'average_seek_time': seek_time / size,
            'worst_case_seek_time': worst_case_seek_time
        }

# Print results
for algorithm in results:
    print(f"\n{algorithm} Results:")
    for size in results[algorithm]:
        total_seek = results[algorithm][size]['total_seek_time']
        avg_seek = results[algorithm][size]['average_seek_time']
        worst_seek = results[algorithm][size]['worst_case_seek_time']
        print(f"  {size} Requests: Total Seek Time = {total_seek}, Average Seek Time = {avg_seek}, Worst-Case Seek Time = {worst_seek}")
