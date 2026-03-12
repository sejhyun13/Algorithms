import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

mapping = {
    1 : [0,1,2,3],
    2 : [0,2],
    3 : [1,3],
    4 : [0,1],
    5 : [1,2],
    6 : [2,3],
    7 : [0,3],
}

def bfs(x,y):
    vis = [[False] * m for _ in range(n)]
    cnt = 1
    q = [(x,y)]
    vis[x][y] = True
    while cnt < l:
        r, c = q.pop(0)
        for d in mapping[arr[r][c]]:
            nr, nc = r + dr[d], c + dc[d]
            if in_range(nr, nc) and not vis[nr][nc]:
                q.append((nr, nc))
        cnt += 1



T = int(input())
for tc in range(1,T+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
