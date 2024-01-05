import pandas as pd

with open("notes.txt") as f:
    lines = [l.strip() for l in f.read().split("\n") if l]

data = []
for line in lines:
    # res = re.match(r"(.*) (.*) (.*) \"(.*)\"", line)
    class_name, name, line = line.split(" ", 2)
    condition, description = line.split(" \"")
    condition = "" if condition == "-" else condition
    description = description[:-1]

    data.append((class_name, name, condition, description))

df = pd.DataFrame(data, columns=["Class", "Name", "Condition", "Description"])
print(df)
# df.to_csv("bolt_passes.csv", index=False)
