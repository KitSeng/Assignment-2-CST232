import random

# total number of cylinders
tot_cylinder = 200
# current head position
curr_head = 50
# moving direction of the disk head
moving_direction = "right"


def CLOOK(requests, curr_head, moving_direction):
    # Initialize variables
    seek_time = 0
    seek_req_sequence = []

    # Sort the request list in ascending order
    requests.sort()

    # Find the index where the current head is located in the sorted request list
    curr_head_index = 0
    for i in range(len(requests)):
        if requests[i] >= curr_head:
            curr_head_index = i
            break

    if moving_direction == "right":
        # Process requests from the current head position to the end of the disk
        for i in range(curr_head_index, len(requests)):
            track = requests[i]
            seek_req_sequence.append(track)
            seek_time += abs(track - curr_head)
            curr_head = track

        # Process requests from the beginning of the disk to the current head position
        for i in range(0, curr_head_index):
            track = requests[i]
            seek_req_sequence.append(track)
            seek_time += abs(track - curr_head)
            curr_head = track
    elif moving_direction == "left":
        # Process requests from the current head position to the beginning of the disk
        for i in range(curr_head_index - 1, -1, -1):
            track = requests[i]
            seek_req_sequence.append(track)
            seek_time += abs(track - curr_head)
            curr_head = track

        # Process requests from the end of the disk to the current head position
        for i in range(len(requests) - 1, curr_head_index - 1, -1):
            track = requests[i]
            seek_req_sequence.append(track)
            seek_time += abs(track - curr_head)
            curr_head = track

    # Calculate average seek time
    num_requests = len(requests)
    average_seek_time = seek_time / num_requests

    # Calculate worst-case seek time
    max_distance = max(abs(seek_req_sequence[0] - 50), max(abs(track - seek_req_sequence[index]) for index, track in enumerate(seek_req_sequence[1:])))

    # Print results
    print("\nSeek request sequence is:", seek_req_sequence)
    print("\nTotal seek time =", seek_time, "ms")
    print("Average seek time =", average_seek_time, "ms")
    print("Worst-case seek time =", max_distance, "ms")

# Example usage with 10 random requests and moving direction to the right
request_10 = [176, 79, 34, 60, 92, 11, 41, 114]
print("\nRequest size: 10")
print("10 random requests:", request_10)
CLOOK(request_10, curr_head, moving_direction)

# generate a set of 20 random requests
request_20 = random.sample(range(tot_cylinder), 20)
print("\n\n\nRequest size : 20")
print("20 random requests :", request_20)
CLOOK(request_20, curr_head, moving_direction)

# generate a set of 50 random requests
request_50 = random.sample(range(tot_cylinder), 50)
print("\n\n\nRequest size : 50")
print("50 random requests :", request_50)
CLOOK(request_50, curr_head, moving_direction)

# generate a set of 100 random requests
request_100 = random.sample(range(tot_cylinder), 100)
print("\n\n\nRequest size : 100")
print("100 random requests :", request_100)
CLOOK(request_100, curr_head, moving_direction)
