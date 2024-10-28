from pathlib import Path

src_root = Path(__file__).parent.parent

# filename = src_root / "rockyou.txt"
# file = open(file=filename, mode='rt')
# lines = file.readlines()
# file.close

count = 0

with open(src_root / "rockyou.txt", "rt", encoding='latin-1') as file:
    phrase = input("what do you need to check?")
    for line in file:
        if phrase in line:
            count += 1
    print(count)
