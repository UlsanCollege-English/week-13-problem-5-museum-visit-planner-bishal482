from collections import deque

def shortest_path(rooms, doors, start, goal):
    # If start/goal not in rooms → no valid path
    if start not in rooms or goal not in rooms:
        return []

    # Special case: start == goal
    if start == goal:
        # If the room exists, return a one-element path
        return [start]

    # Build adjacency list
    graph = {room: [] for room in rooms}
    for a, b in doors:
        if a in graph and b in graph:
            graph[a].append(b)
            graph[b].append(a)

    # BFS for shortest path
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        room, path = queue.popleft()

        for neighbor in graph[room]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                if neighbor == goal:
                    return new_path
                queue.append((neighbor, new_path))

    # No path found
    return []
