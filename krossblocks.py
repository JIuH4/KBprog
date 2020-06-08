KBK = []

KL_M = []
for n in range(0, 200):
    KL_M.append(f"M_{n + 1}")
KL_M = tuple(KL_M)

KL_K = []
for n in range(0, 8):
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

KBK.append(KL_M)
KBK.append(KL_K)
KBK.append(KL_B1)
KBK.append(KL_B2)
KBK.append(KL_B3)
KBK.append(KL_B4)


def print_kb(kb):
    for klemnik in kb:
        for node in klemnik:
            print(node)
