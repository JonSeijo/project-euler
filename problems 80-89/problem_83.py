# Problem 83
# Path sum: four ways

import queue
import math

SIZE = 80
INF = math.inf
matriz = []

with open("problem_83.txt") as fi:
    for line in fi:
        matriz.append([int(x) for x in line.split(',')])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dist = [ [ INF for __ in range(SIZE)] for _ in range(SIZE)]

def valido(x, y):
    return 0 <= x and x < SIZE and 0 <= y and y < SIZE

def dijskta(sx, sy):
    
    q = queue.PriorityQueue()
    q.put((matriz[sx][sy], sx, sy))

    while not q.empty():
        elem = q.get()

        curr = elem[0]
        x = elem[1]
        y = elem[2]

        if dist[x][y] <= curr:
            continue

        dist[x][y] = curr

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if valido(nx, ny) and dist[x][y] + matriz[nx][ny] < dist[nx][ny]:
                q.put((dist[x][y] + matriz[nx][ny], nx, ny)) 


dijskta(0, 0)
print(dist[SIZE-1][SIZE-1])
