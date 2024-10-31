# 변을 공유하는 두 개의 사각형은 다른 색
# 맨 왼쪽 위가 흰: WBWBWBWB, BWBWBWBW * 4
# 맨 왼쪽 위가 검: BWBWBWBW, WBWBWBWB * 4
# 리페인트값_min 설정
# 왼쪽 위 시작 위치를 정하기 위한 for문 - 패턴 1, 2 각각 리페인트값 = 0
# 8X8 for문 - 시작 위치에서 같은 위치 비교 -> 다르면 -> 리페인트값 +1
# min 값 정하기..


N, M = map(int, input().split())
board = [input().strip() for _ in range (N)]

pattern1 = ['WBWBWBWB', 'BWBWBWBW'] * 4
pattern2 = ['BWBWBWBW', 'WBWBWBWB'] * 4

repaint_min = 64

for i in range(N-7):
    for j in range(M-7):
        repaint1 = 0
        repaint2 = 0
        for x in range(8):
            for y in range(8):
                if board[i+x][j+y] != pattern1[x][y]:
                    repaint1 += 1
                if board[i+x][j+y] != pattern2[x][y]:
                    repaint2 += 1
        repaint_min = min(repaint_min, repaint1, repaint2)

print(repaint_min)

