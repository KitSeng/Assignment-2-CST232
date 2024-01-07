import random

# total number of cylinders
tot_cylinder = 200
# current head position
curr_head = 50
# moving direction of the disk head
moving_direction = "right"


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

# generate a set of 10 random requests
request_10 = [176, 79, 34, 60, 92, 11, 41, 114]
print("\nRequest size: 10")
print("10 random requests:", request_10)
CSCAN(request_10, curr_head, moving_direction)

# generate a set of 20 random requests
request_20 = random.sample(range(tot_cylinder), 20)
print("\n\n\nRequest size : 20")
print("20 random requests :", request_20)
CSCAN(request_20, curr_head, moving_direction)

# generate a set of 50 random requests
request_50 = random.sample(range(tot_cylinder), 50)
print("\n\n\nRequest size : 50")
print("50 random requests :", request_50)
CSCAN(request_50, curr_head, moving_direction)

# generate a set of 100 random requests
request_100 = random.sample(range(tot_cylinder), 100)
print("\n\n\nRequest size : 100")
print("100 random requests :", request_100)
CSCAN(request_100, curr_head, moving_direction)


