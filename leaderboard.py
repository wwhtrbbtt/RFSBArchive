from collections import Counter

def get_top(numbers, k=10):
    c = Counter(numbers)
    most_common = [key for key, val in c.most_common(k)]

    return most_common

names = []
with open("formatted.txt", "r") as f:
	raw = f.read()

lines = raw.split("\n")

for x in lines:
	try:
		names.append(x.split(" ")[2])
	except:
		pass

print(len(names))
leaderboard = get_top(names, k=31)


print(f"Total messages: {len(names)}")
print(f"Total unique accounts in SB: {len(list(set(names)))}")

place = 0
for x in leaderboard:
    if len(x) > 2:
        count = raw.count(" - " +x)
        print(f"{place}: @{x.replace(':', '')} ({count} messages)")

        place += 1


