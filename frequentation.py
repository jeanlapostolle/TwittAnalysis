import matplotlib.pyplot as plt


def FREQ(imgfname="freq.png"):
    file = open("res.csv", "r")

    y = [0] * 384

    for line in file.readlines():
        tmp = 0
        date = line.split(",")[1]
        tmp += int(date[:2]) * 4
        tmp += int(date[3:5]) // 15
        if date.endswith("21 mars 2013"):
            pass
        if date.endswith("22 mars 2013"):
            tmp += 96
            pass
        if date.endswith("23 mars 2013"):
            tmp += 192
            pass
        if date.endswith("24 mars 2013"):
            tmp += 288
            pass
        y[tmp] += 1

    plt.plot(range(384), y)

    plt.savefig(imgfname)
