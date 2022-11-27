from itertools import permutations

k = 0
gl = ["А", "И", "О", "У"]
sg = ["Б", "К", "Л", "Н"]
words = permutations("АБИКОЛУН")
for w in words:
    if (w[0] in gl and w[1] in sg and w[2] in gl and w[3] in sg and w[4] in gl and w[5] in sg and w[6] in gl and w[
        7] in sg) or (
            w[0] in sg and w[1] in gl and w[2] in sg and w[3] in gl and w[4] in sg and w[5] in gl and w[6] in sg and w[
        7] in gl):
        k += 1

print(k)

# 1152
