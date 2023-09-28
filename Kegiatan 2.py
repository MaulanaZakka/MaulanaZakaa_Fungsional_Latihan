#Kegiatan 2
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_values = {}
float_values = ()
string_values = []

for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        ratusan = item // 100
        puluhan = (item // 10) % 10
        satuan = item % 10
        int_values[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        float_values += (item,)
    elif isinstance(item, str):
        string_values.append(item)

print("Data int:")
print(int_values)

print("Data float:")
print(float_values)

print("Data string:")
print(string_values)
