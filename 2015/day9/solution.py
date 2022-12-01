import codecs
import sys


def find_all_paths(graph, start, path=[]):
    path = path + [start]
    if start not in graph:
        return [path]
    paths = [path]
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def get_route(line):
    tmp = line.split()
    return tmp[0], tmp[2], int(tmp[-1])


if __name__ == "__main__":
    with codecs.open("input.txt") as input_file:
        distances = list(map(get_route, input_file.readlines()))
        routes_dict = {}
        cost_dict = {}
        for i in distances:
            from_, to_, cost = i
            if from_ not in routes_dict:
                routes_dict[from_] = [to_]
            else:
                routes_dict[from_].append(to_)
            if to_ not in routes_dict:
                routes_dict[to_] = [from_]
            else:
                routes_dict[to_].append(from_)
            cost_dict[(from_, to_)] = cost
            cost_dict[(to_, from_)] = cost
            min_cost = 1000000
        min_cost = sys.maxsize
        max_cost = 0
        longest_path = ""
        shortest_path = ""
        for start_node in routes_dict:
            all_paths = find_all_paths(routes_dict, start_node)
            for path_ in all_paths:
                if len(path_) == len(routes_dict):
                    cost = 0
                    for i, j in zip(path_, path_[1:]):
                        cost += cost_dict[(i, j)]
                    if cost < min_cost:
                        min_cost = cost
                        shortest_path = path_
                    if cost > max_cost:
                        max_cost = cost
                        longest_path = path_
        print("part 1:", " -> ".join(shortest_path), min_cost)
        print("part 2:", " -> ".join(longest_path), max_cost)
