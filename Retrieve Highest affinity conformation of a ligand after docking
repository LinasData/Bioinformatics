import re
import os
import tkinter as tk
from tkinter import filedialog
from sys import exit

"""
THIS CODE IS USED TO RETRIEVE ONLY THE HIGHEST AFFINITY CONFORMATION OF A LIGANDS AFTER DOCKING. 
ONLY USED ON UBUNTU LINUX OS
"""

# open tkinter
root = tk.Tk()
# close tkinter unusable window
root.withdraw()

# Choose directory based on your docked molecules file

direc = filedialog.askdirectory(initialdir="~", title="Docked ligands directory")

# Listing files of chosen directory
try:
    entries = os.listdir(direc)
except:
    print("Error when opening a directory")
    exit()

if len(entries) == 0:
    print("Error: No entries in a directory")
    exit()

# Regular expressions pattern (preparing for the for loop)
inp = input("Enter files ending pattern (default: _out.mol2): ")
if len(inp) == 0:
    inp = "_out.mol2"

pattern = re.compile(inp)

# Try to find all entries that corresponds to patter
listo = []
for i in entries:
    match = re.search(pattern, i)
    if match:
        listo.append(i)
    else:
        pass
# Stop program if list of entries is empty
if len(listo) == 0:
    print("No files found with written ending " + str(inp))
    exit()


stop = ""

# find second conformation line and exclude it
def find_stop_line(inpt, outpt):
    global stop
    fn = open(outpt, "w")
    with open(inpt) as f:
        count_line = 0
        count_pattern = 0

        for line in f:
            if line.startswith("@<TRIPOS>MOLECULE") and count_pattern == 0:
                start = count_line
                count_pattern += 1

            elif line.startswith("@<TRIPOS>MOLECULE") and count_pattern == 1:
                stop = count_line
                count_pattern += 1

            else:
                pass

            count_line += 1
    return stop

# Extract the best affinity (first) ligand
def mol2_with_best_affinity(inpt, outpt):
    fn = open(outpt, "w")
    stopped = find_stop_line(inpt, outpt)
    with open(inpt) as f:
        count = 0
        for line in f:
            if count < stopped:
                fn.write(line)
            else:
                pass
            count += 1


# Loop through the list of the docked ligands
ligandai = 0

try:
    for i in listo:
        name = str(i)
        #print("Ligand " + name)
        out = (direc + "/best_pose/" + i)
        ind = (direc + "/" + i)
        mol2_with_best_affinity(ind, out)
        ligandai += 1
except:
    print("BAD FILE FORMAT")
    exit()

# Print number of ligands
print("Number of ligands: ", ligandai)
