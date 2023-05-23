from pathlib import Path

concatenated = ""
for child in Path("data").glob("*.txt"):
    if child.is_file():
        concatenated += child.read_text()

with open("data/out/concatenated.txt", "w") as f:
    f.write(concatenated)
    f.close()