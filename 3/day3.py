with open('input.txt') as f:
    lines = f.read().splitlines()

triangles = []
for line in lines:
    triangles.append(sorted([int(x) for x in line.split()]))

def possible(triangles):
    possible = 0
    for result in [triangle[0] + triangle[1] > triangle[2] for triangle in triangles]:
        if result:
            possible += 1
    return possible

print(possible(triangles))

triangles = [[],[],[]]
for line in lines:
    triangles[0].append(int(line.split()[0]))
    triangles[1].append(int(line.split()[1]))
    triangles[2].append(int(line.split()[2]))

temp = triangles[0]+triangles[1]+triangles[2]

triangles = [sorted(temp[i:i+3]) for i in range(0,len(temp),3)]

print(possible(triangles))
    
