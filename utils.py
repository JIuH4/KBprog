Chanel_name = []
for n in range(0, 100):
    Chanel_name.append(f"CH_{n}")

class Utils:

    # конструктор
    def __init__(self, name):
        self.name = name  # устанавливаем имя
        self.base = []
        self.m1_50 = ""
        self.m51_100 = ""
        self.m101_150 = ""
        self.m151_200 = ""
        self.connectors=["p1","p2","p3","p4"]

    def add_module_pxi2569(self):
        # m1_50
        if self.m1_50 == "p1":
            for i in range(1, 51):
                self.base.append([f"M_{i}", Chanel_name[100 - i * 2 + 1], Chanel_name[100 - i * 2 + 1]])
        if self.m1_50 == "p2":
            for i in range(1, 51):
                self.base.append([f"M_{51 - i}", Chanel_name[100 - i * 2 + 1], Chanel_name[100 - i * 2 + 1]])
        if self.m1_50 == "p3":
            for i in range(1, 51):
                self.base.append([f"M_{i}", Chanel_name[100 - i * 2], Chanel_name[100 - i * 2]])
        if self.m1_50 == "p4":
            for i in range(1, 51):
                self.base.append([f"M_{51 - i}", Chanel_name[100 - i * 2], Chanel_name[100 - i * 2]])
        # m51_100
        if self.m51_100 == "p1":
            for i in range(1, 51):
                self.base.append([f"M_{50 + i}", Chanel_name[100 - i * 2 + 1], Chanel_name[100 - i * 2 + 1]])
        if self.m51_100 == "p2":
            for i in range(1, 51):
                self.base.append([f"M_{101 - i}", Chanel_name[100 - i * 2 + 1], Chanel_name[100 - i * 2 + 1]])
        if self.m51_100 == "p3":
            for i in range(1, 51):
                self.base.append([f"M_{50 + i}", Chanel_name[100 - i * 2], Chanel_name[100 - i * 2]])
        if self.m51_100 == "p4":
            for i in range(1, 51):
                self.base.append([f"M_{101 - i}", Chanel_name[100 - i * 2], Chanel_name[100 - i * 2]])
        # m101_150
        if self.m101_150 == "p1":
            for i in range(1, 51):
                self.base.append([f"M_{100 + i}", Chanel_name[100 - i * 2 + 1], Chanel_name[100 - i * 2 + 1]])
        if self.m101_150 == "p2":
            for i in range(1, 51):
                self.base.append([f"M_{151 - i}", Chanel_name[100 - i * 2 + 1], Chanel_name[100 - i * 2 + 1]])
        if self.m101_150 == "p3":
            for i in range(1, 51):
                self.base.append([f"M_{100 + i}", Chanel_name[100 - i * 2], Chanel_name[100 - i * 2]])
        if self.m101_150 == "p4":
            for i in range(1, 51):
                self.base.append([f"M_{151 - i}", Chanel_name[100 - i * 2], Chanel_name[100 - i * 2]])
        # m151_200
        if self.m151_200 == "p1":
            for i in range(1, 51):
                self.base.append([f"M_{150 + i}", Chanel_name[100 - i * 2 + 1], Chanel_name[100 - i * 2 + 1]])
        if self.m151_200 == "p2":
            for i in range(1, 51):
                self.base.append([f"M_{201 - i}", Chanel_name[100 - i * 2 + 1], Chanel_name[100 - i * 2 + 1]])
        if self.m151_200 == "p3":
            for i in range(1, 51):
                self.base.append([f"M_{150 + i}", Chanel_name[100 - i * 2], Chanel_name[100 - i * 2]])
        if self.m151_200 == "p4":
            for i in range(1, 51):
                self.base.append([f"M_{201 - i}", Chanel_name[100 - i * 2], Chanel_name[100 - i * 2]])

    def generate_links(self):
        self.add_module_pxi2569()

    def process_node(self, node):
        links = []
        for link in self.base:
            if link[0] == node:
                links.append(link)
                for link2 in self.base:
                    if link2[1] == link[1] and link2[0] != link[0]:
                        links.append(link2)
        return links

    def display_info(self):
        print("", self.name)


# ut = Utils("ss")
# ut.m151_200 = "p2"
# ut.m1_50 = "p1"
#
# ut.add_module_pxi2569()
# print(ut.process_node("M_156"))
# print(ut.base)
