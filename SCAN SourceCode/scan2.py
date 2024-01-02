import random

#number of requests
num_request = 10 
#total number of cylinders
tot_cylinder = 200
#a set of random requests
set_request = [ 159, 33, 116, 149, 51, 153, 140, 184, 109, 69]
#current head position
curr_head = 50
#moving direction of the disk head 
moving_direction = "left"


def SCAN(set_request, curr_head, moving_direction):

	#initialize the variables
	#the required time to position the disk head on the requested track 
	seek_time = 0
	#the distance from current disk head to the next nearest requested track
	#store the next nearest requested track  
	track_traveled, curr_track = 0, 0
	#store requested track on the left hand side of the current disk head
	left_request = []
	#store requested track on the right hand side of the current disk head
	right_request = []
	#the requested track sequence visited by the disk head 
	seek_req_sequence = []

	#append the end value that disk head will visit before reversing the direction
	if (moving_direction == "left"):
		left_request.append(0)
	elif (moving_direction == "right"):
		right_request.append(tot_cylinder - 1)

	#append the requested track to store on the left or right hand side of the current disk head
	for i in range(num_request):
		if(moving_direction =="left"):
			if (set_request[i] <= curr_head):
				left_request.append(set_request[i])
			else:
				right_request.append(set_request[i])
		elif(moving_direction =="right"):
			if (set_request[i] < curr_head):
				left_request.append(set_request[i])
			else:
				right_request.append(set_request[i])

	# Sorting in ascending order
	left_request.sort()
	right_request.sort()

	#Will loop two times 
	#One to the left and another one to the right of the disk head
	loop = 2
	while (loop != 0):
		if (moving_direction == "left"):
			for i in range(len(left_request) - 1, -1, -1):
				curr_track = left_request[i]

				#append the current track to the seek request sequence
				seek_req_sequence.append(curr_track)

				#calculate the absolute distance traveled by the disk head
				track_traveled = abs(curr_track - curr_head)
				
				#print the subtraction operation
				print (curr_track, "-", curr_head, "=", track_traveled, "ms")

				#increase the seek time
				seek_time += track_traveled

				#visited track become new disk head
				curr_head = curr_track
			
			#reverse the direction
			moving_direction = "right"
	
		elif (moving_direction == "right"):
			for i in range(len(right_request)):
				curr_track = right_request[i]
				
				#append the current track to the seek request sequence
				seek_req_sequence.append(curr_track)

				#calculate the absolute distance traveled by the disk head
				track_traveled = abs(curr_track - curr_head)

				#print the subtraction operation
				print (curr_track, "-", curr_head, "=", track_traveled, "ms")

				#increase the seek time
				seek_time += track_traveled

				#visited track become new disk head
				curr_head = curr_track
			
			#reverse the direction
			moving_direction = "left"
		
		loop -= 1


	print("\nTotal number of seek time =", seek_time, "ms")

	print("\nSeek request sequence is", end=' ')
	for i in range(len(seek_req_sequence)):
		print(seek_req_sequence[i], end=' ')



SCAN(set_request, curr_head, moving_direction)
