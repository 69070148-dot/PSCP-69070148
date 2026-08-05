"""Surprising Vote"""

s_sum = float(input())
s_max = float(input())
two_Score = s_sum - s_max
total_score = min(s_max, two_Score)
lowest_score = two_Score - total_score
difference = s_max - lowest_score

if difference > 2:
    print("Surprising")
else:
    print("Not surprising")
