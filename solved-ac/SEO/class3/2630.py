import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# print(paper)

zero_count = 0
one_count = 0

def slice_paper(paper, size):
    global zero_count, one_count
    if size == 1:
        if paper[0][0] == 1:
            one_count += 1
        else:
            zero_count += 1
        return
    
    if all(p == 1 for row in paper for p in row):
        one_count += 1
        return
    elif all(p == 0 for row in paper for p in row):
        zero_count += 1
        return
    
    half = size // 2
    first_quadrant = [p[int(half):]for p in paper[:int(half)]]
    second_quadrant = [p[:int(half)]for p in paper[:int(half)]]
    third_quadrant = [p[:int(half)]for p in paper[int(half):]]
    fourth_quadrant = [p[int(half):]for p in paper[int(half):]]

    slice_paper(first_quadrant, half)
    slice_paper(second_quadrant, half)
    slice_paper(third_quadrant, half)
    slice_paper(fourth_quadrant, half)

slice_paper(paper, N)

print(zero_count)
print(one_count)