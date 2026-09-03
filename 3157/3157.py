"""เกมสะสมแต้ม"""

N = int(input())
score = 0

for _ in range(1 , N+1):
    command = input()
    if command == '+':
        score += 10
    elif command == '-':
        score -= 5

print(score)
