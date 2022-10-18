from nbformat import write


def readstudents(className):
    path = "data/" + className + ".txt"
    tmp = open(path, "r").readlines()
    listName = []
    for name in tmp:
        listName.append(name.replace('\n', ''))
    return listName

def match(input):
    output = []
    for name in input:
        if name in pesertaldk:
            output.append(name)
    output.sort()
    return output

def writeName(data, className):
    path = "output/" + className + ".txt"
    f = open(path, "a")
    for name in data:
        f.write(name + "\n")
    f.close()

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

koma = readstudents("koma")
komb = readstudents("komb")
csa = readstudents("csa")
csb = readstudents("csb")
pesertaldk = readstudents("pesertaldk")

komaldk = match(koma)
kombldk = match(komb)
csaldk = match(csa)
csbldk = match(csb)


writeName(komaldk, "koma")
writeName(kombldk, "komb")
writeName(csaldk, "csa")
writeName(csbldk, "csb")

alldata = csaldk + csbldk + komaldk + kombldk
missing = Diff(pesertaldk, alldata)

writeName(missing, "missing")