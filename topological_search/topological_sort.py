from collections import deque

def topological_sort(courses):
    graph = {}
    in_degree = {}
    
    for course in courses:
        course_name = course['course']
        graph[course_name] = []
        in_degree[course_name] = 0

    for course in courses:
        for prereq in course['prerequisites']:
            graph[prereq].append(course['course'])
            in_degree[course['course']] += 1
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)

        for dependent in graph[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    return result if len(result) == len(courses) else []


courses = [
        {"course": "Math", "prerequisites": ["Physics"]},
        {"course": "Physics", "prerequisites": []},
        {"course": "Computer Science", "prerequisites": ["Math", "Physics"]},
    ]
print(topological_sort(courses))