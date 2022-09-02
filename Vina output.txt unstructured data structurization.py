import pandas as pd
from rdkit import Chem
from rdkit.Chem import PandasTools
import tkinter as tk
from tkinter import filedialog

# Open tkinter
root = tk.Tk()
# Close tkinter unusable window
root.withdraw()
# Choose vina results file (made from concatinated output.txt files)
file_path = filedialog.askopenfilename(initialdir="~", title="Pasirinkite Vina rezultatų failą",
                                       filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))

f = open(file_path, "r")

#Choose output files directory
out_path = filedialog.askdirectory(initialdir="~", title="Išsaugoti failus")
fn = open(out_path+"/Vina_results_all.csv", "w")

#Skip some lines and add only needed once
for line in f:
    if line.startswith(("#", "Reading input", "Setting up", "Analyzing the binding", "Using random", "Performing", "Refining", "Writing out")):
        pass
    else:
        fn.write(line)
fn.close()


fn = open(out_path+"/Vina_results_all.csv", "r")

names = []
first_mode_affinities = []

#Retrieve the best pose conformations affinity scores

for line in fn:
    if line.startswith("Out"):
        name = line[14:]
        for i in range(len(name)):
            if name[i] == "_":
                name1 = name[:i]
                names.append(name1)

    if line.startswith(" "):
        line = line.strip()
        if line.startswith("1"):
            line_split = line.split()
            first_mode_affinity = line_split[1]
            first_mode_affinities.append(first_mode_affinity)
            
#Choose smiles file of molecules

smiles_path = filedialog.askopenfilename(initialdir="~", title="Pasirinkite smiles rezultatų failą",
                                       filetypes=(("TXT files", "*.txt"), ("all files", "*.*")))

fsmiles = open(smiles_path, "r")
smiles = []
for smile in fsmiles:
    for i in range(len(smile)):
        if smile[i:i+1] == "\n":
            smile1 = smile[:i]
            smiles.append(smile1)

d = {"Name": pd.Series(names), "1st affinity": pd.Series(first_mode_affinities), "Smiles": pd.Series(smiles)}

s = pd.DataFrame(d)

#Create structured data table

Chem.PandasTools.AddMoleculeColumnToFrame(s, smilesCol='Smiles', molCol='Molecule')
Chem.PandasTools.SaveXlsxFromFrame(s, out_path + '/Docking_results.xlsx', molCol='Molecule')

print(s)

s.to_csv(out_path+"/S1PR1_vina_results.csv", index=False, header=True)

fn.close()
