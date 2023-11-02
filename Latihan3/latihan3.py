random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan

def check_float(x):
    return isinstance(x, float)


def check_int(x):
    return isinstance(x, int)


def check_str(x):
    return isinstance(x, str)


float_val = tuple(filter(check_float, random_list))
int_val = list(filter(check_int, random_list))
str_val = list(filter(check_str, random_list))


def pecahan(value):
    ratusan = value // 100
    sisa = value % 100
    puluhan = sisa // 10
    satuan = sisa % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}


mapped = list(map(pecahan, int_val))

# Output
print("Data Float:", float_val)
print("Data Int: ")
for item in mapped:
    print(item)

print("Data String:", str_val)
