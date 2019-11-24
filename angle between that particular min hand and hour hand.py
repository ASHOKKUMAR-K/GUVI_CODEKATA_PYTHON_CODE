(h, m) = map(int, input().split())
minhanddeg = m * 6
hourhanddeg = (h * 60 * 0.5) + (m * 0.5)
angle = (int(abs(minhanddeg - hourhanddeg)))
if angle > 180:
    angle = 360 - angle
print(angle)
