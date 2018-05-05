

file = 'astar_octile'

points = []

with open(file, 'r') as f:
    titles = f.readline().rstrip().split(';')
    for line in f:
        initial_point, final_point, cost, state, time = line.rstrip().split(';')
        points.append([initial_point, final_point, float(cost), int(state), float(time)])


points = sorted(points, key=lambda x: x[2])
# print(points)
for line in points:
    print(line[0].replace(',', ' ') + ' ' + line[1].replace(',', ' '))
