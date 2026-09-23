"""Big Frame"""

WORD_1 = " ".join(input().split())
WORD_2 = " ".join(input().split())
WORD_3 = " ".join(input().split())
WORD_4 = " ".join(input().split())
WORD_5 = " ".join(input().split())
longest_word = max(len(WORD_1), len(WORD_2), len(WORD_3), len(WORD_4), len(WORD_5))
print("*" * (longest_word + 4))
for i in range(5):
    if not i:
        print("* " + WORD_1 + " " * (longest_word - len(WORD_1)) + " *")
    elif i == 1:
        print("* " + WORD_2 + " " * (longest_word - len(WORD_2)) + " *")
    elif i == 2:
        print("* " + WORD_3 + " " * (longest_word - len(WORD_3)) + " *")
    elif i == 3:
        print("* " + WORD_4 + " " * (longest_word - len(WORD_4)) + " *")
    elif i == 4:
        print("* " + WORD_5 + " " * (longest_word - len(WORD_5)) + " *")
print("*" * (longest_word + 4))
