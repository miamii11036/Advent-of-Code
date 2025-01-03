import numpy as np

data = np.loadtxt("clue.txt")

left = []
right = []

for i in range(0, len(data), 1):
    num = int(data[i][0])
    num2 = int(data[i][1])
    left.append(num)
    right.append(num2)

left = sorted(left)
right = sorted(right)

distance = []
for i in range(0, len(left), 1):
    distance.append(abs(left[i] - right[i]))

ans = sum(distance)

time = []

for i in left:
    if i in right:
        repeat = right.count(i)
        time.append(repeat)
    else: 
        time.append(0)

ans1 = 0

for i in range(0, len(left), 1):
    ans1 = (left[i] * time[i]) + ans1
print(ans1)