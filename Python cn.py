from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

total = 0
for _ in range(n):
    data = Student(*input().split())
    total += int(data.MARKS)

print(f"{total / n:.2f}")
