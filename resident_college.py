from collections import deque

def stable_matching(student_pref, college_pref, positions):
    clgq = deque(college_pref.keys())
    
    student_priority = {stud: {j:i for i,j in enumerate(student_pref[stud])} 
                        for stud in student_pref} #reduces time complexity n of index() function
    
    clg_final = {i:[] for i in college_pref}
    clg_visited = {i:[] for i in college_pref}
    student_admit = {i:None for i in student_pref}

    while clgq:
        
        clg = clgq.popleft()
        for std in college_pref[clg]:
            
            # college positions are filled
            if not positions[clg] > 0:
                break
        
            # student has already been visited
            if std in clg_visited[clg]:
                continue
            
            clg_visited[clg].append(std) #to not repeat
            
            if not student_admit[std]:
                student_admit[std] = clg
                clg_final[clg].append(std)
                positions[clg] -= 1
            
            elif student_priority[std][clg] < student_priority[std][student_admit[std]]:
                #pre assigned clg change
                clg_final[student_admit[std]].remove(std)
                positions[student_admit[std]] += 1
                clgq.append(student_admit[std])

                #student change
                student_admit[std] = clg
                clg_final[clg].append(std)
                positions[clg] -= 1

    return student_admit,clg_final
                    
                    
                
student_pref = {'a':['g','r','s'],
                'b':['r','s','g'],
                'c':['g','r','s'],
                'd':['s','g','r'],
                'e':['s','r','g']}

college_pref = {'s':['a','b','c','d','e'],
                'r':['e','c','a','d','b'],
                'g':['a','e','b','d','c']}

positions = {'s':1, 'r':1, 'g':2}

student, college = stable_matching(student_pref, college_pref, positions)
print('student selection', student)
print('college selection', college)