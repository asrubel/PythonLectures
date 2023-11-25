my_dict = {"518": 8, "519": 14, "519st": 18, "518st": 5}
print(type(my_dict))
print(my_dict["518"])
my_dict["518"] = my_dict["518"] + 1
print(my_dict)

for key in my_dict:
    print(key)

for key in my_dict.keys():
    print(key)

for val in my_dict.values():
    print(val)

print(my_dict.keys())

for pair in my_dict.items():
    print(pair)

for key, val in my_dict.items():
    print(key, " -> ", val)

new_dict = {1: "python", 3.2: "float", "str": 100, (): [],
            (1, 2, 3): "numbers"}

print(new_dict)
print(hash((1, 2, [1, 2, 3])))
