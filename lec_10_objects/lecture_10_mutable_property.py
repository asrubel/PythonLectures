class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        print(f"{self.name} created!")
        River.all_rivers.append(self)

    def show_info(self):
        print(f"{self.name} with length in km: {self.length}")


# Instantiate objects of class River
dnipro = River("Dnipro", 3000)
dnistro = River("Dnistro", 2000)
dunay = River("Dunay", 4000)

# List all rivers created previously
for river in River.all_rivers:
    river.show_info()
    River.show_info(river)
