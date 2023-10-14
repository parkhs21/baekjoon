D,H,W = map(int, input().split())
D_ = (H**2 + W**2) ** (0.5)
print(int(D/D_*H), int(D/D_*W))