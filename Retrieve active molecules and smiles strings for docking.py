import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Enter what protein do you want to analyze 
klase = input("What protein today are we going to analyze?\n")

# Open tkinter user interface
root = tk.Tk()
# Close unused tkinter window
root.withdraw()
# Choose  and ChEMBL database file
file_path = filedialog.askopenfilename(initialdir="~", title="Pasirinkite ChEMBL duomenų bazės failą",
                                       filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
data = pd.read_csv(file_path, sep=";")

# Find antagonists
antagonists = data[data['Assay Description'].str.lower().str.contains("antagonist")]

# Retrieve only active antagonists
antagonists_active = antagonists[(antagonists["Standard Value"] < 1)]

# Finding agonists
agonists = data[data['Assay Description'].str.lower().str.contains("agonist")]

# Retrieve only active antagonist
agonists_active = agonists[(agonists["Standard Value"] < 1)]

# Choose values that are nano molar
filt_units = data[(data['Standard Units'] == "nM")]

for i in filt_units["Standard Value"]:
    if i != "NaN":
        column = float(i)
        filt_units["Standard Value"].replace([i], column)
    else:
        pass
    
# Choose only promising data
database = filt_units[(filt_units["Standard Value"] < 1)]

# Create list of smiles
dfSmiles = database["Smiles"]
# Pasirinkti ouput įrašymo vietą
out_path = filedialog.askdirectory(initialdir="~", title="Išsaugoti failus")

# Failas, kuriame nufiltruota ChEMBL duomenų bazė (tik nM)
filt_units.to_csv(out_path + "/ChEMBL_nM_std_unit.csv", index=False, header=True)
# Generate antagonists file
antagonists.to_csv(out_path + "/ChEMBL_antagonist.csv", index=False, header=True)
# Generate antagonists active file
antagonists_active.to_csv(out_path + "/ChEMBL_antagonist_active.csv", index=False, header=True)
# Generate agonist file
agonists.to_csv(out_path + "/ChEMBL_agonists.csv", index=False, header=True)
# Generate agonist active file
agonists_active.to_csv(out_path + "/ChEMBL_agonists_active.csv", index=False, header=True)

#Create file with list of promising molecules in smiles
fn = open(out_path + "/SMILES_" + klase + ".txt", "w")

#Create file with only promosing data of molecules
database.to_csv(out_path + "/ChEMBL_" + klase + "_filtruota.csv", index=False, header=True)
filt_units.to_csv(out_path + "/ChEMBL_" + klase + ".csv", index=False, header=True)

#Add smiles into the file
for n, l in dfSmiles.iteritems():
    if "." in l:
        for i in range(len(l)):
            if l[i] == ".":
                fn.write(l[0:i] + "\n")
    else:
        fn.write(l + "\n")
fn.close()

print("Darbas baigtas")
