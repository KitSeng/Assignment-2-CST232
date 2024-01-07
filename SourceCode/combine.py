import random

tot_cylinder = 200
curr_head = 50
moving_direction = "right"


def SCAN(requests, curr_head, moving_direction):

    # initialize the variables
    # to store the total required time to position the disk head on the requested tracks for the whole requests
    seek_time = 0
    # the distance from the current disk head to the next nearest requested track
    # store the next nearest requested track
    track_traveled, curr_track = 0, 0
    # store requested tracks on the left-hand side of the current disk head
    left_request = []
    # store requested tracks on the right-hand side of the current disk head
    right_request = []
    # the requested tracks sequence visited by the disk head
    seek_req_sequence = []

    # append the end value that the disk head will visit before reversing the direction
    if moving_direction == "left":
        left_request.append(0)
    elif moving_direction == "right":
        right_request.append(tot_cylinder - 1)

    # append the requested tracks to store on the left or right-hand side of the current disk head
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

    # Sorting in ascending order
    left_request.sort()
    right_request.sort()

    # Will loop two times
    # One to the left and another one to the right of the disk head
    loop = 2
    while loop != 0:
        if moving_direction == "left":
            for i in range(len(left_request) - 1, -1, -1):
                curr_track = left_request[i]

                # append the current track to the seek request sequence
                seek_req_sequence.append(curr_track)

                # calculate the absolute distance traveled by the disk head
                track_traveled = abs(curr_track - curr_head)

                # increase the seek time
                seek_time += track_traveled

                # visited track becomes the new disk head
                curr_head = curr_track

            # reverse the direction
            moving_direction = "right"

        elif moving_direction == "right":
            for i in range(len(right_request)):
                curr_track = right_request[i]

                # append the current track to the seek request sequence
                seek_req_sequence.append(curr_track)

                # calculate the absolute distance traveled by the disk head
                track_traveled = abs(curr_track - curr_head)

                # increase the seek time
                seek_time += track_traveled

                # visited track becomes the new disk head
                curr_head = curr_track

            # reverse the direction
            moving_direction = "left"

        loop -= 1

    print("\nSeek request sequence is", end=' ')
    for i in range(len(seek_req_sequence)):
        print(seek_req_sequence[i], end=' ')

    print("\n\nTotal seek times =", seek_time, "ms")

    # Calculate average seek times
    num_requests = len(requests)
    average_seek_time = seek_time / num_requests
    print("\nAverage seek times =", average_seek_time, "ms")

    # Calculate worst-case seek times
    # Identify the two tracks that are furthest apart
    max_distance = max(abs(seek_req_sequence[0]-50), max(abs(track - seek_req_sequence[index]) for index, track in enumerate(seek_req_sequence[1:])))
    print("\nWorst-case seek times =", max_distance, "ms")


def CSCAN(requests, curr_head, moving_direction):
    # Initialize cariables
    seek_time = 0
    track_travelled = 0
    curr_track = 0
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
    # First service the requests on the right side of the head.
        for i in range(curr_head_index, len(requests)):
            curr_track = requests[i]

            # Appending current track to seek sequence
            seek_req_sequence.append(curr_track)

            # Calculate absolute distance travelled by the disk head
            track_travelled = abs(curr_track - curr_head)

            # Increase the seek time
            seek_time += track_travelled

            # Accessed track becoming the new head
            curr_head = curr_track
        
        # The C-SCAN algorithm will visit the end value before reversing the direction
        seek_req_sequence.append(tot_cylinder -1)
        
        # Increase the seek time from the last request to the end value
        seek_time += ((tot_cylinder -1) - curr_head)
        
        # Once reached the right end jump to the beginning.
        curr_head = 0
        seek_req_sequence.append(0)
        
        # adding seek time for head returning to 0
        seek_time += (tot_cylinder -1)

        # Now service the requests again which are left.
        for i in range(0, curr_head_index):
            curr_track = requests[i]
            seek_req_sequence.append(curr_track)
            track_travelled = abs(curr_track - curr_head)
            seek_time += track_travelled
            curr_head = curr_track

    # First service the requests on the left side of the head.
    elif moving_direction == "left":
        for i in range(curr_head_index - 1, -1, -1):
            curr_track = requests[i]
            seek_req_sequence.append(curr_track)
            track_travelled = abs(curr_track - curr_head)
            seek_time += track_travelled
            curr_head = curr_track
        
        # The C-SCAN algorithm will visit the end value before reversing the direction
        seek_req_sequence.append(0)
        
        # Increase the seek time from the last request to the end value
        seek_time += curr_head
        
        # Once reached the left end jump to the right end.
        curr_head = tot_cylinder -1
        seek_req_sequence.append(tot_cylinder -1)
        
        # adding seek time from left end to right end
        seek_time += (tot_cylinder -1)

        # Now service the requests again which are right.
        for i in range(len(requests) - 1, curr_head_index - 1, -1):
            curr_track = requests[i]
            seek_req_sequence.append(curr_track)
            track_travelled = abs(curr_track - curr_head)
            seek_time += track_travelled
            curr_head = curr_track
    
    # Print results
    print("\nSeek request sequence is", end=' ')
    for i in range(len(seek_req_sequence)):
        print(seek_req_sequence[i], end=' ')

    print("\n\nTotal seek times =", seek_time, "ms")

    # Calculate average seek times
    num_requests = len(requests)
    average_seek_time = seek_time / num_requests
    print("\nAverage seek times =", average_seek_time, "ms")

    # Calculate worst-case seek times
    # Identify the two tracks that are furthest apart
    max_distance = max(abs(seek_req_sequence[0]-50), max(abs(track - seek_req_sequence[index]) for index, track in enumerate(seek_req_sequence[1:])))
    print("\nWorst-case seek times =", max_distance, "ms")


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


# Function to run all three algorithms with given requests
def run_algorithms(requests):
    print("\n\n-------------------------------------------------------------------------------------------------------------------")
    print("\n\nRequest size:", len(requests))
    print("Random requests:", requests)

    print("\n\n-------- SCAN Algorithm --------")
    SCAN(requests, curr_head, moving_direction)

    print("\n-------- C-SCAN Algorithm --------")
    CSCAN(requests, curr_head, moving_direction)

    print("\n-------- C-LOOK Algorithm --------")
    CLOOK(requests, curr_head, moving_direction)


# Example usage with different request sizes
request_sizes = [10, 20, 50, 100]

for size in request_sizes:
    requests = random.sample(range(tot_cylinder), size)
    run_algorithms(requests)
