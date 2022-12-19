r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = set()
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0


def dfs(x, y, cnt):
    global ans

    ans = max(ans, cnt)
    visited.add(graph[x][y])

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] not in visited:
                dfs(nx, ny, cnt + 1)

    # 동서남북 가려 했는데 갈 곳이 없으면 dfs 끝나면서 방문 함수에서 제거
    # 이전에 dfs 호출 했던 곳으로 이동 하면서 cnt+1 했던거 무효 된다.
    visited.remove(graph[x][y])


dfs(0, 0, 1)

print(ans)