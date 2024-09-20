import heapq
from collections import defaultdict


lectures  = [(1,4), (2,6), (4,7), (5,9), (3,5)] #each tuple represents (start,end) time of a lecture
lectures.sort() #sort the lectures by their start time
assigned_lecture = defaultdict(list) #stores class number and their respective lectures
classrooms = [] #stores end time of respective assigned lectures


def brute_force(lectures, classrooms, assigned_lecture):
    # time complexity O(n**2) -- sort (O(nlogn) and classroom search n)

    for lecture in lectures:
        lecture_start, lecture_end = lecture
        lecture_assigned = False #initialization

        #if there are classrooms assigned
        for room in range(len(classrooms)):
        
            if lecture_start >= classrooms[room]: #lecture start > rooms' end time
                lecture_assigned = True
                assigned_lecture[room].append(lecture)
                classrooms[room] = lecture_end  #update new lecture endtime for that room
                break 
                
        if not lecture_assigned: #no room assigned so far
            classrooms.append(lecture_end) #assign new room and store its lecture endtime
            assigned_lecture[len(classrooms)-1].append(lecture)
    
    return classrooms, assigned_lecture


def optimized_partitioning(lectures, classrooms, assigned_lecture):
    # time complexity - O(nlogn)

    for lecture in lectures:
        lecture_start, lecture_end = lecture

        # If there are rooms available and the earliest finishing room is free before this lecture starts
        if classrooms and classrooms[0][0] <= lecture_start:
            # Assign the lecture to the room that finishes the earliest (pop from the heap)
            earliest_end_time, room = heapq.heappop(classrooms)
            assigned_lecture[room].append(lecture)
            # Push the new end time for that room into the heap
            heapq.heappush(classrooms, (lecture_end, room))
        else:
            # Create a new room for this lecture
            room = len(classrooms)
            assigned_lecture[room].append(lecture)
            heapq.heappush(classrooms, (lecture_end, room))

    return classrooms, assigned_lecture


# classrooms, assigned_lecture = brute_force(lectures, classrooms, assigned_lecture)
classrooms, assigned_lecture = optimized_partitioning(lectures, classrooms, assigned_lecture)

print('final allocated classrooms to lectures are ', assigned_lecture)
print('Total number of classrooms needed for the day are ',len(classrooms))

        
