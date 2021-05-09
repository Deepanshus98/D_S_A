
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
from collections import deque
 
 
# Below lists detail all eight possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]
 
 
# check if it is possible to go to pixel `(x, y)` from the
# current pixel. The function returns false if the pixel
# has a different color, or it is not a valid pixel
def isSafe(M, x, y, target):
    return 0 <= x < len(M) and 0 <= y < len(M[0]) and M[x][y] == target
 
 
# Flood fill using BFS
def floodfill(M, x, y, replacement):
 
    # create a queue and enqueue starting pixel
    q = deque()
    q.append((x, y))
 
    # get the target color
    target = M[x][y]
 
    # break when the queue becomes empty
    while q:
 
        # dequeue front node and process it
        x, y = q.popleft()
 
        # replace the current pixel color with that of replacement
        M[x][y] = replacement
 
        # process all eight adjacent pixels of the current pixel and
        # enqueue each valid pixel
        for k in range(len(row)):
            # if the adjacent pixel at position `(x + row[k], y + col[k])` is
            # is valid and has the same color as the current pixel
            if isSafe(M, x + row[k], y + col[k], target):
                # enqueue adjacent pixel
                q.append((x + row[k], y + col[k]))
 
 
if __name__ == '__main__':
 
    # matrix showing portion of the screen having different colors
    M = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]
 
    # start node
    x = 3
    y = 9
 
    # target color `X`
    # replacement color
    replacement = 'C'
 
    # replace the target color with a replacement color
    floodfill(M, x, y, replacement)
 
    # print the colors after replacement
    for r in M:
        print(r)
