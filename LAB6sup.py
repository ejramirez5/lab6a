def topological_sort(graph):
    all_in_degrees = [0] * (graph.get_num_vertices())
    for i in range(len(all_in_degrees)):
        all_in_degrees[i] = graph.compute_in_degree(i)

    sort_result = []
    q = []

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.append(i)
    while len(q) != 0:
        u = q.pop(0)

        sort_result.append(u)

        for adj_vertex in graph.get_vertices_reachable_from(u):
            all_in_degrees [adj_vertex] -=1

            if all_in_degrees[adj_vertex] == 0:
                q.append(adj_vertex)
    
    if len(sort_result) != graph.get_num_vertices():
        return None
    return sort_result
