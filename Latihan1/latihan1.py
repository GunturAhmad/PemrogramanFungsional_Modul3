data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]


def conve(w=0):
    def days(d=0):
        def hours(h=0):
            def minutes(m=0):
                return ((w*7+d)*24+h)*60+m
            return minutes
        return hours
    return days


extract_datas = list(map(lambda i: [int(num)
                     for num in i.split() if num.isdigit()], data))
print(extract_datas)

save_res = []
for i in extract_datas:
    print("\n- - - - - - - - - - - -\n")
    a = int(i[0])
    b = int(i[1])
    c = int(i[2])
    d = int(i[3])

    print("Minggu\t: ", a)
    print("Hari\t: ", b)
    print("Jam\t: ", c)
    print("Menit\t: ", d)
    res = conve(a)(b)(c)(d)
    print("Hasil\t: {}\n".format(res))
    save_res.append(res)

    print(str(save_res))
