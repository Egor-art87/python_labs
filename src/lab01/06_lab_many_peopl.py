n, o, z = int(input()), 0, 0
for i in range(n):
    a = input("in_" + str(i + 1) + ":").split()
    if (a[-1]) == "True":
        o += 1
    elif (a[-1]) == "False":
        z += 1
print(f"out: {o} {z}")
