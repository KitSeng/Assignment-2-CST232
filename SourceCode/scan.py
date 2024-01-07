import random

# total number of cylinders
tot_cylinder = 200
# current head position
curr_head = 50
# moving direction of the disk head
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


# generate a set of 10 random requests
request_10 = [176, 79, 34, 60, 92, 11, 41, 114]
print("\nRequest size : 10")
print("10 random requests :", request_10)
SCAN(request_10, curr_head, moving_direction)

# generate a set of 20 random requests
request_20 = random.sample(range(tot_cylinder), 20)
print("\n\n\nRequest size : 20")
print("20 random requests :", request_20)
SCAN(request_20, curr_head, moving_direction)

# generate a set of 50 random requests
request_50 = random.sample(range(tot_cylinder), 50)
print("\n\n\nRequest size : 50")
print("50 random requests :", request_50)
SCAN(request_50, curr_head, moving_direction)

# generate a set of 100 random requests
request_100 = random.sample(range(tot_cylinder), 100)
print("\n\n\nRequest size : 100")
print("100 random requests :", request_100)
SCAN(request_100, curr_head, moving_direction)
