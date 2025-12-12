from server import server
import time

def find_svr_to_out_through_dac_fft(file):
    _, servers = get_servers(file)
    queue = [[find_server_by_name(servers, 'svr'), 0, 0]]
    visited = []
    num_paths = 0

    while (len(queue) > 0):
        current, hasfft, hasdac = queue[0]
        path = current.path_to.append(current.name)

        if current.name not in visited:
            visited.append(current.name)
        # print(current.name, hasfft, hasdac)
        print(f'lenght of queue: {len(queue)} and num_paths: {num_paths}', end='\r', flush=True)


        if current.out and hasfft and hasdac:
            num_paths += 1
        else:
            for next_server in current.connections:
                if next_server.add_path_to(path):
                    if next_server.name == 'fft':
                        queue.append([next_server, True, hasdac])
                    elif next_server.name == 'dac':
                        queue.append([next_server, hasfft, True])
                    else:
                        queue.append([next_server, hasfft, hasdac])
                    next_server.remove_parent(current)
        queue.pop(0)

    return num_paths


def find_paths_from_to(start, end):
    num_paths = 0
    queue = [start]

    while (len(queue) > 0):
        current = queue[0]

        if current.name == end:
            num_paths += 1
        elif current.out:
            if end == 'out':
                num_paths += 1
            queue.pop(0)
            continue
        else:
            for next_servers in current.connections:
                if next_servers.name == end:
                    queue.append(next_servers)
                    break
                elif next_servers.has_parent(current):
                    queue.append(next_servers)
                    next_servers.remove_parent(current)

        # print(f'lenght of queue: {len(queue)} and num_paths: {num_paths}', end='\r', flush=True)
        queue.pop(0)

    return num_paths


def test_find_paths_from_to():
    _, servers = get_servers("actual_input.txt")
    svr = find_server_by_name(servers, "svr")
    dac = find_server_by_name(servers, "dac")
    fft = find_server_by_name(servers, "fft")

    print(f"from svr to dac {find_paths_from_to(svr, 'dac')}")
    reset_server_parents(servers)
    print(f"from svr to fft {find_paths_from_to(svr, 'fft')}")
    reset_server_parents(servers)
    print(f"from dac to fft {find_paths_from_to(dac, 'fft')}")
    reset_server_parents(servers)
    print(f"from fft to dac {find_paths_from_to(fft, 'dac')}")
    reset_server_parents(servers)
    print(f"from fft to out {find_paths_from_to(fft, 'out')}")
    reset_server_parents(servers)
    print(f"from dac to out {find_paths_from_to(dac, 'out')}")


def find_all_paths(file):
    first_server, _ = get_servers(file)
    num_paths = 0
    queue = [first_server]

    while (len(queue) > 0):
        if queue[0].out:
            num_paths += 1
        else:
            for next_servers in queue[0].connections:
                queue.append(next_servers)
        queue.pop(0)

    return num_paths
    

def find_server_by_name(servers, name):
    for s in servers:
        if s.name == name:
            return s
    return None


def reset_server_parents(servers):
    for s in servers:
        s.reset_parents()


def get_servers(file):
    servers = []
    connections = []
    first_server = None
    with open(file, 'r') as f:
        for line in f:
            s = line.strip("\n").split(" ")
            if s[1] == "out":
                servers.append(server(s[0][:-1], True))
            else:
                serv = server(s[0][:-1])
                if serv.name == 'you':
                    first_server = serv
                servers.append(serv)

            connections.append(s[1:])

    for i in range(len(servers)):
        for name in connections[i]:
            c = find_server_by_name(servers, name)
            if c != None:
                servers[i].add_connection(c)
                if c.name != 'out':
                    c.add_parent(servers[i])

    return first_server, servers


if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: number of paths from you to out is {find_all_paths('example_input.txt')}")
    print(f"Actual file: number of paths from you to out is {find_all_paths('actual_input.txt')} \n")

    print("The answers for the second half:")
    print(f"Test file: number of paths from svr to out through dac and fft {find_svr_to_out_through_dac_fft('example_input_part_ii.txt')}")
    # test_find_paths_from_to()
    print(f"Actual file: number of paths from svr to out through dac and fft {find_svr_to_out_through_dac_fft('actual_input.txt')} \n")