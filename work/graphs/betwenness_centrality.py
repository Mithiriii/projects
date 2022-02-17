from collections import deque


users = [
 {"id": 0, "name": "Hero"},
 {"id": 1, "name": "Dunn"},
 {"id": 2, "name": "Sue"},
 {"id": 3, "name": "Chi"},
 {"id": 4, "name": "Thor"},
 {"id": 5, "name": "Clive"},
 {"id": 6, "name": "Hicks"},
 {"id": 7, "name": "Devin"},
 {"id": 8, "name": "Kate"},
 {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


def shortest_path_from(from_user):

    #słownik przypisujący najkrótksze ścieżki do indentyfikatorów użytkowników
    shortest_path_to = {from_user["id"]: [[]]}

    #kolejka składa się z park, które należy sprawdzić
    frontier = deque((from_user, friend) for friend in from_user["friends"])

    while frontier:
        prev_user, user = frontier.popleft()
        user_id = user["id"]
        path_to_prev = shortest_path_to[prev_user["id"]]
        paths_via_prev = [path + [user_id] for path in path_to_prev]
        old_paths_to_here = shortest_path_to.get(user_id, [])

        if old_paths_to_here:
            min_path_length = len(old_paths_to_here[0])
        else:
            min_path_length = float('inf')

        new_path_to_here = [path_via_prev
                            for path_via_prev in paths_via_prev
                            if len(path_via_prev) <= min_path_length
                            and path_via_prev not in old_paths_to_here]

        shortest_path_to[user_id] = old_paths_to_here + new_path_to_here

        frontier.extend((user, friend) for friend in users["friends"]
                        if friend["id"] not in shortest_path_to)
    return shortest_path_to


for user in users:
    user["betwenness_centrality"] = 0.0

for source in users:
    source_id = source["id"]
    for target_id, paths in iter(source["shortest_paths"].items()):
        if source_id < target_id:
            num_paths = len(paths)
            contrib = 1 / num_paths
            for path in paths:
                for id in path:
                    if id not in [source_id, target_id]:
                        users[id]["betwenness_centrality"] += contrib
