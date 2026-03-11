drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def slide(arr, d):
    # arr[0] -> 행, arr[1] -> 열
    # 각 열 별로 한 행씩 위로 올리려면 arr[j][i]
    # 반대면 arr[i][j]
    if d == 0:  # 위로밀기
        for i in range(n):  # 각 열 별로 한 행씩 위로 올려야 함 -> arr[j][i]
            for j in range(n):  # j를 -1해야
                ni, nj = i, j - 1
                if in_range(ni, nj):
                    arr[nj][ni] += arr[j][i]  # 이동하려는 칸에 값 더하고
                    arr[j][i] = 0  # 현재 위치 0으로

    elif d == 1:  # 우로밀기
        for i in range(n):  # 각 행 별로 한 열씩 우로 밀어야 함 -> arr[i][j]
            for j in range(n - 1, -1, -1):  # j를 +1해야 하며, 우측부터 하므로 역순
                ni, nj = i, j + 1
                if in_range(ni, nj):
                    arr[ni][nj] += arr[i][j]
                    arr[i][j] = 0
    elif d == 2:  # 아래로밀기
        for i in range(n):  # 각 열 별로 한 행씩 아래로 내려야 함 -> arr[j][i]
            for j in range(n - 1, -1, -1):  # j를 +1해야 하며, 아래부터 하므로 역순
                ni, nj = i, j + 1
                if in_range(ni, nj):
                    arr[nj][ni] += arr[j][i]  # 이동하려는 칸에 값 더하고
                    arr[j][i] = 0  # 현재 위치 0으로
    else:  # 좌로밀기
        for i in range(n):  # 각 행 별로 한 열씩 좌로 밀어야 함 -> arr[i][j]
            for j in range(n):  # j를 +1해야
                ni, nj = i, j + 1
                if in_range(ni, nj):
                    arr[ni][nj] += arr[i][j]
                    arr[i][j] = 0

    return arr


def get_max(arr):
    max_val = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_val:
                max_val = arr[i][j]

    return max_val


def main(arr, lv):  # 메인 풀이 함수
    if lv == 5:
        result.append(get_max(arr))
        return

    for d in range(4):
        next_arr = slide(arr, d)
        main(next_arr, lv + 1)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = []
main(arr, 0)
print(max(result))