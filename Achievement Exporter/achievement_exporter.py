import os
import fileinput
import time
pathx = "./After-the-End---Old-World/save games"
k = []
stuff = []
print("Reading...")
for path, subdirs, files in os.walk(pathx): #writing
    for fajl in files:
        if fajl.endswith(".ck2"):
            file = open(os.path.join(path, fajl))
            found = False
            try:
                for i in file.readlines():
                    if not found and i=="\tflags=\n":
                        found = True
                        newfile = i
                    elif found and i=="\t}\n":
                        break
                    elif found and i!="\t{\n":
                        o = i.split("=")[0].replace("\t","")
                        if o.startswith("achievement") and o not in k:
                            k.append(o)
                        newfile = newfile + i
                stuff.append((os.path.join(path, fajl),newfile))
            except:
                pass
print("Writing...")
for i in stuff:
    x = i[1]
    for o in k:
        if o not in x:
            x = x+"\t\t" + o.replace("\n","") + "=2555.1.1\n"
    file = open(i[0]).read()
    g = open(i[0]+"www","w")
    g.write(file.replace(i[1],x,1))
    g.close()
    os.remove(i[0])
    os.rename(i[0]+"www",i[0])
