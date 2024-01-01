import random

def c_look(requests, head):
    """
    C-LOOK disk scheduling algorithm implementation.

    :param requests: List of disk requests
    :param head: Initial position of the disk head
    :return: Total head movement
    """
    
    total_movement = 0

    # Split requests into two parts based on the head position
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    # First serve the requests on the right side of the head
    for r in right:
        total_movement += abs(head - r)
        head = r

    # If there are requests on the left side, jump to the closest on the left
    if left:
        total_movement += abs(head - left[-1])
        head = left[-1]

    # Then serve the remaining requests on the left
    for r in reversed(left):
        total_movement += abs(head - r)
        head = r

    return total_movement

def generate_random_requests(num_requests, max_cylinder):
    # Generate random requests
    random_requests = [random.randint(0, max_cylinder) for _ in range(num_requests)]
    return random_requests

def calculate_seek_times(algorithm, num_requests, trials, max_cylinder):
    average_seeks = []
    worst_case_seeks = []

    for trial in range(trials):
        requests = generate_random_requests(num_requests, max_cylinder)
        initial_head_position = random.randint(0, max_cylinder)
        total_movement = algorithm(requests, initial_head_position)

        # Calculate average seek time
        average_seek = total_movement / num_requests
        average_seeks.append(average_seek)

        # Track the worst-case seek time
        sorted_requests = sorted(requests)
        max_seek = max(abs(initial_head_position - sorted_requests[0]), abs(initial_head_position - sorted_requests[-1]))
        worst_case_seeks.append(max_seek)

        if trial == trials - 1:
            # Print the requests for the final trial only
            print(f"Final Trial, Request Size {num_requests}, Requests: {requests}")

    return sum(average_seeks) / trials, max(worst_case_seeks)

# Example: Analyze for 10, 20, 50, 100 random requests (not sorted)
request_sizes = [10, 20, 50, 100]
for size in request_sizes:
    avg_seek, worst_seek = calculate_seek_times(c_look, size, 100, 199)
    print(f"Request Size {size}: Average Seek = {avg_seek}, Worst-Case Seek = {worst_seek}")