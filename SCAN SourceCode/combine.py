import random

tot_cylinder = 200
curr_head = 50
moving_direction = "left"


def SCAN(requests, curr_head, moving_direction):
    seek_time = 0
    track_traveled, curr_track = 0, 0
    left_request = []
    right_request = []
    seek_req_sequence = []

    if moving_direction == "left":
        left_request.append(0)
    elif moving_direction == "right":
        right_request.append(tot_cylinder - 1)

    for i in range(len(requests)):
        if moving_direction == "left":
            if requests[i] <= curr_head:
                left_request.append(requests[i])
            else:
                right_request.append(requests[i])
        elif moving_direction == "right":
            if requests[i] < curr_head:
                left_request.append(requests[i])
            else:
                right_request.append(requests[i])

    left_request.sort()
    right_request.sort()

    loop = 2
    while loop != 0:
        if moving_direction == "left":
            for i in range(len(left_request) - 1, -1, -1):
                curr_track = left_request[i]
                seek_req_sequence.append(curr_track)
                track_traveled = abs(curr_track - curr_head)
                seek_time += track_traveled
                curr_head = curr_track

            moving_direction = "right"

        elif moving_direction == "right":
            for i in range(len(right_request)):
                curr_track = right_request[i]
                seek_req_sequence.append(curr_track)
                track_traveled = abs(curr_track - curr_head)
                seek_time += track_traveled
                curr_head = curr_track

            moving_direction = "left"

        loop -= 1

    print("\nSeek request sequence is", end=' ')
    for i in range(len(seek_req_sequence)):
        print(seek_req_sequence[i], end=' ')

    print("\n\nTotal seek times =", seek_time, "ms")

    num_requests = len(requests)
    average_seek_time = seek_time / num_requests
    print("\nAverage seek times =", average_seek_time, "ms")

    max_distance = max(abs(seek_req_sequence[0] - 50),
                      max(abs(track - seek_req_sequence[index]) for index, track in enumerate(seek_req_sequence[1:])))
    print("\nWorst-case seek times =", max_distance, "ms")


def c_look(requests, head):
    total_movement = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    for r in right:
        total_movement += abs(head - r)
        head = r

    if left:
        total_movement += abs(head - left[-1])
        head = left[-1]

    for r in reversed(left):
        total_movement += abs(head - r)
        head = r

    return total_movement


def generate_random_requests(num_requests, max_cylinder):
    random_requests = random.sample(range(max_cylinder), num_requests)
    return random_requests


def calculate_seek_times(algorithm, requests, trials, max_cylinder):
    average_seeks = []
    worst_case_seeks = []

    for trial in range(trials):
        initial_head_position = random.randint(0, max_cylinder)
        total_movement = algorithm(requests, initial_head_position)

        average_seek = total_movement / len(requests)
        average_seeks.append(average_seek)

        sorted_requests = sorted(requests)
        max_seek = max(abs(initial_head_position - sorted_requests[0]),
                       abs(initial_head_position - sorted_requests[-1]))
        worst_case_seeks.append(max_seek)

        if trial == trials - 1:
            print(f"Final Trial, Request Size {len(requests)}, Requests: {sorted_requests}")

    return sum(average_seeks) / trials, max(worst_case_seeks)


def analyze_algorithms(request_sizes, num_trials, max_cylinder):
    for size in request_sizes:
        random_requests = generate_random_requests(size, max_cylinder)

        print(f"\nRequest size: {size}")
        print(f"Random requests: {random_requests}")

        print("\nSCAN Algorithm:")
        SCAN(random_requests, curr_head, moving_direction)

        print("\nC-LOOK Algorithm:")
        avg_seek, worst_seek = calculate_seek_times(c_look, random_requests, num_trials, max_cylinder)
        print(f"Total seek times = {avg_seek * size} ms")
        print(f"Average seek times = {avg_seek} ms")
        print(f"Worst-case seek times = {worst_seek} ms")


# Example: Analyze for 10, 20, 50, 100 random requests (not sorted)
request_sizes = [10, 20, 50, 100]
num_trials = 100
max_cylinder = 199

analyze_algorithms(request_sizes, num_trials, max_cylinder)
