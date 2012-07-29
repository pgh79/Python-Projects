m3 = 0
m5 = 0
m15 = 0
for i in range(0, 1001):
    if i % 3 == 0:
        m3 += i
    if i % 5 == 0:
        m5 += i
    if i % 15 == 0:
        m15 += i
ans = m3 + m5 - m15
print ans
