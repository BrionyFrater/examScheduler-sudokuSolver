#using graph colouring to schedule exams using the minimal amount of time slots possible
#works on the theorm that no more than four colours are need to colour a map




course_pairs = {}
all_courses = []



print('\n\n\t\t\tSIMPLE EXAM SCHEDULER')
print('_'*70)
print('\n')

#get all vertices
all_courses = input('Enter all courses to be scheduled, seperate each by a comma?\n')
all_courses = [x.strip() for x in all_courses.split(',')]

print("""
----------------------------------------------------------------------------------------------------------------------------
HOW IT WORKS, an example,

The courses being evaluated are CS1, CS2, M1, M2, P1
Students who do CS1 also do CS2 and M1
Students who do P1 also do M2 and M1

What courses does CS1 conflict with? CS2, M1
What courses does P1 conflict with? M2, M1

In order for the program to understand that M1 cannot be the same time as M2 or CS2 it must be explicitly stated, therefore
What courses does M1 conflict with? M2, CS2

CS2 and M2 can be left blank
""")

for course in all_courses:

    print('-'*70)

    realted =  input(f'What courses does {course} conflict with, seperate each by a comma?\n')

    #track adjacent vertices for each vertex, also gives each vertex a list of possible colours
    course_pairs[course] = [x.strip() for x in realted.split(',')] +  [[1, 2, 3, 4]]

    if course in course_pairs[course][:-1]:
        print('A course cannot conflict with itself')
        exit()


#organize the vertices by degrees, those with more adjacent vertices are put to the front
course_pairs = dict(sorted(course_pairs.items(), key=lambda item: len(item[1]), reverse=True))

#goes through each vertex
for k,v in course_pairs.items():
    
    #gives vertex a colour 1, 2, 3, or 4 from the possible colours list
    col = v[-1][0]
    
    
    for adj in v[:-1]:
        

        if adj != "":
            
            try:
                #removes color selected above from posssible colours for each adj vertex
                if col in course_pairs[adj][-1]:
                    course_pairs[adj][-1].remove(col)
                
            except KeyError:
                #program needs to know all courses beforehand
                print(f'{adj} wasnt entered in the course list above, ensure you enter all the courses that will be used.')
                exit()


#presentation
print('\n\n')
print('SCHEDULE')
print('_'*70)
print("Time Period\t\t\t\tCourse")
print('_'*70)

#organize the courses by the selected time periods, for presentation purposes
course_pairs = dict(sorted(course_pairs.items(), key=lambda item: item[1][-1][0]))


#prints vertices(courses) and their colours(time periods)
for k,v in course_pairs.items():
    try:
        #assigns the vertex to the first colour in the list
        print(str(v[-1][0]) +"\t\t\t\t\t"+ k)
    except IndexError:
        #happens when the graph has to be coloured in more than four colours, we can account for this by modifying the possible colours list
        print('Im sorry the associations were to specific to be scheduled')
