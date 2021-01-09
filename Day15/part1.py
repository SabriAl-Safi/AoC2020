starts = [11,18,0,20,1,7,16]
last = {}
prev = -1

for n in range(2020):
    cur = starts[n] if n < len(starts) else \
          n - last[prev] if prev in last else \
          0
    last[prev] = n
    prev = cur
print(cur)
