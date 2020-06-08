KL_M = []
Chanel_name = []
for n in range(0, 100):
    Chanel_name.append(f"CH_{n}")
print(Chanel_name)
# KL_M = tuple(KL_M)

p1_p2 = []
for i in range(1, 51):
    p1_p2.append([i, 51 - i, Chanel_name[100 - i * 2 + 1]])
print(p1_p2)

p3_p4 = []
for i in range(1, 51):
    p3_p4.append([i, 51 - i, Chanel_name[100 - i * 2]])
print(p3_p4)


# for n in range(0, 100, 2):
#     KL_M.append([f"{n+1 }", f"{n + 2}",Chanel_name[100-n-2]])
# KL_M = tuple(KL_M)
# print(KL_M)


class Utils:

    # конструктор
    def __init__(self, name):
        self.name = name  # устанавливаем имя
        self.base = []
        self.m1_50 = ""
        self.m51_100 = ""
        self.m101_150 = ""
        self.m151_200 = ""

    def add_module_pxi2569(self, kb, m1_50="", m51_100="", m101_150="", m151_200=""):

        pass

    def process_node(self):
        pass

    def display_info(self):
        print("", self.name)
