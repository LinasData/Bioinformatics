import pandas as pd


f = open("S1PR1_Chembl_all.csv", "r")
df = pd.read_csv(f, sep=";")

dfSmiles = df["Smiles"]
fn = open("TrueSmiles_new.txt", "w")

for n, l in dfSmiles.iteritems():
    if "." in l:
        for i in range(len(l)):
            if l[i] == ".":
                fn.write(l[0:i]+"\n")
                print(l[0:i])
    else:
        fn.write(l+"\n")
        print(l)

f.close()
fn.close()

dfSmiles.to_csv (r'S1PR1.only.smiles.csv', index = False, header=True)
