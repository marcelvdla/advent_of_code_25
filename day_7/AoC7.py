def get_manifold(file):
    manifold = []

    with open(file, 'r') as f:
        for line in f:
            manifold.append(line.strip("\n"))
    
    return manifold


def split_beams(file):
    manifold = get_manifold(file)
    splits = 0
    beams = {manifold[0].index("S")}

    for i in range(2, len(manifold), 2):
        for j in range(len(manifold[i])):
            if j in beams and manifold[i][j] == "^":
                splits += 1
                beams.remove(j)
                beams.add(j-1)
                beams.add(j+1)
    
    return splits


def compute_timelines(file):
    timelines = 1
    manifold = get_manifold(file)
    beams = {manifold[0].index("S"):1}

    for i in range(2, len(manifold), 2):
        for j in range(len(manifold[i])):
            if j in beams.keys() and manifold[i][j] == "^":
                if beams[j] > 1:
                    timelines += beams[j]
                else:
                    timelines += 1

                if j - 1 in beams.keys():
                    beams[j-1] += beams[j]
                else:
                    beams[j-1] = beams[j]

                if j + 1 in beams.keys():
                    beams[j+1] += beams[j]
                else:
                    beams[j+1] = beams[j]

                beams.pop(j)

    return timelines



if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: the beam gets split {split_beams('test_diagram.txt')} times")
    print(f"Actual file: the beam gets split {split_beams('actual_diagram.txt')} times \n")

    print("The answers for the second half:")
    print(f"Test file: the beam splits into {compute_timelines('test_diagram.txt')} timelines")
    print(f"Actual file: the beam splits into {compute_timelines('actual_diagram.txt')} timelines")