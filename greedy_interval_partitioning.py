from collections import defaultdict

lectures  = [(1,4), (2,6), (4,7), (5,9), (3,5)] #each tuple represents (start,end) time of a lecture

#sort the lectures by their start time
lectures.sort()

assigned_lecture = defaultdict(list) #stores class number and their respective lectures
classrooms = [] #stores end time of respective assigned lectures


for lecture in lectures:
    lecture_start, lecture_end = lecture[0], lecture[1]
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

print('final allocated classrooms to lectures are ', assigned_lecture)
print('Total number of classrooms needed for the day are ',len(classrooms))

        
