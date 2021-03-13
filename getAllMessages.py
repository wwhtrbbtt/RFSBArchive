name = "whtrbbt"

messages = []
with open("formatted.txt", "r") as f:
    lines = f.read().split("\n")

for x in lines:
    if x.find(f"] - {name}: ") != -1:
        messages.append(x)

print(f"{len(messages)} messages stored in {name}.txt")
with open(name + ".txt", "w") as f:
    f.write("\n".join(messages))