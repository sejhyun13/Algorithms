# 중위 탐색하는 문제임

import sys;sys.stdin = open('이진탐색input.txt')


def recur(nums, i): # i : 넣을 노드 번호
    mid = max(nums) // 2 + 1
    tree[i][2] = mid
    # tree[i][0] =
    # tree[i][1] =
    left = nums[1:mid]
    right = nums[mid+1:n+1]
    if i != 0 and 2*i + 1 < len(nums):
        recur(left, 2*i)
        recur(right, 2*i + 1)

T = int(input())
for tc in range(1,T+1):
    n = int(input()) # 정점 갯수
    arr = list(range(n+1))
    tree = [[0] * 3 for _ in range(n+1)]
    recur(arr, 1)
    print(tree)