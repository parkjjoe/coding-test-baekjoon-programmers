import sys

total = [i for i in range(1, 31)]

for _ in range(28):
    a = int(sys.stdin.readline())
    total.remove(a)

print(min(total))
print(max(total))