xa,ya,xb,yb,xc,yc = map(int, input().split())

if (ya-yb)*(xb-xc) == (yb-yc)*(xa-xb):
    print(-1.0)
else:
    ab = ((xa-xb)**2 + (ya-yb)**2)**0.5
    bc = ((xb-xc)**2 + (yb-yc)**2)**0.5
    ca = ((xc-xa)**2 + (yc-ya)**2)**0.5
    length = [ab+bc, bc+ca, ca+ab]
    print(2*max(length)-2*min(length))
