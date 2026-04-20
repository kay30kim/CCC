A, B, X, Y = map(int, input().split())

# Case 1: side-by-side
w1 = A + X
h1 = max(B, Y)
p1 = 2 * (w1 + h1)

# Case 2: stacked
w2 = max(A, X)
h2 = B + Y
p2 = 2 * (w2 + h2)

print(min(p1, p2))