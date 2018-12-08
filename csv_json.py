import json, sys

if (len(sys.argv) != 2):
    print("You need to have one arg")
    exit()

# IMPORTANT: make sure that the only commas are used for column separation!

with open(sys.argv[1]) as file:

    file = [s.replace("\n", "") for s in file]
    file = [s.replace("\"", "") for s in file]

    keys = file[0].split(",")
    dataL = []

    for l in file[1:]:
        l = l.split(",")
        print(l)
        dl = dict((dd, "") for dd in keys)
        for i,k in enumerate(keys):
            dl[k] = l[i]
        dataL.append(dl)

    dataJson = json.dumps(dataL, indent=4)

    write = open(f"{sys.argv[1][:-4]}.json", "w")

    write.write(dataJson)

