import matplotlib.pyplot as plt


def FREQ(dateFrom, dateTo, pas=4, imgfname="freq.png"):
    # print(self.ui.dateFrom.date().toString("d MMMM yyyy"))
            # for dat in range(x.daysTo(self.ui.dateTo.date())):
            #     x = x.addDays(1)
            #     print(x)
    file = open("res.csv", "r")

    NbOfDays = dateFrom.daysTo(dateTo)
    y = [0] * (NbOfDays * pas)

    for line in file.readlines():
        date = line.split(",")[1]
        x = dateFrom
        for i in range(NbOfDays):
            if date.endswith(x.toString(" d MMM yyyy")):
                d = i * pas
                d += int(int(date[3:5]) / 60 + int(date[0:2]) * pas / 24)
                if d < len(y):
                    y[d] += 1
            x = x.addDays(1)

    plt.clf()
    plt.plot(range(NbOfDays * pas), y)

    plt.savefig(imgfname)
