KBK = []

KL_M = []
for n in range(0, 200):
    KL_M.append(f"M_{n + 1}")
KL_M = tuple(KL_M)

KL_K = []
for n in range(0, 16):
    KL_K.append(f"K_{n + 1}")
KL_K = tuple(KL_K)

KL_B1 = []
for n in range(0, 50):
    KL_B1.append(f"BA1_{n + 1}")
KL_B1 = tuple(KL_B1)

KL_B2 = []
for n in range(0, 50):
    KL_B2.append(f"BA2_{n + 1}")
KL_B2 = tuple(KL_B2)

KL_B3 = []
for n in range(0, 50):
    KL_B3.append(f"BA3_{n + 1}")
KL_B3 = tuple(KL_B3)

KL_B4 = []
for n in range(0, 50):
    KL_B4.append(f"BA4_{n + 1}")
KL_B4 = tuple(KL_B4)

KL_MB1 = []
for n in range(0, 25):
    KL_MB1.append(f"MB1_{n + 1}")
KL_MB1 = tuple(KL_MB1)

KL_MB2 = []
for n in range(0, 25):
    KL_MB2.append(f"MB2_{n + 1}")
KL_MB2 = tuple(KL_MB2)

KL_MB3 = []
for n in range(0, 25):
    KL_MB3.append(f"MB3_{n + 1}")
KL_MB3 = tuple(KL_MB3)

KL_MB4 = []
for n in range(0, 25):
    KL_MB4.append(f"MB4_{n + 1}")
KL_MB4 = tuple(KL_MB4)

KL_C = []
for n in range(0, 10):
    KL_C.append(f"C_{n + 1}")
KL_C = tuple(KL_C)

KBK.append(KL_M)
KBK.append(KL_K)
KBK.append(KL_B1)
KBK.append(KL_B2)
KBK.append(KL_B3)
KBK.append(KL_B4)
KBK.append(KL_MB1)
KBK.append(KL_MB2)
KBK.append(KL_MB3)
KBK.append(KL_MB4)
KBK.append(KL_C)

def print_kb(kb):
    for klemnik in kb:
        for node in klemnik:
            print(node)
