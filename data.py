import numpy as np

with open("Pulse_rate.txt") as f1, open("BP.txt") as f2, open("ratios.txt") as f:
    for x, y in zip(f1, f2):
        a = np.asarray([])
        b = np.asarray([])
        x = x.strip()
        y = y.strip()
        np.insert(a, 0, x)
        np.insert(b, 0, y)
        if x.isdigit() and y.isdigit():
            z = float(x)/float(y)
            print(str(z))

f1.close()
f2.close()
f.close()
