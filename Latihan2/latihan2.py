data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def check(char):
    return char.isdigit()


value = []
for i in data:
    spl = i.split()
    checker = list(filter(check, spl))
    value.append(checker)

for i in value: print(i)
