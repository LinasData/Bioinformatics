from sys import exit

""" THIS CODE GENERATES BISULFITE MODIFICATION PATTERNS"""

# Input DNA sequence
seq = input("INPUT DNA SEQUENCE: ").upper().strip()

# Create list from DNA sequence
liseq=list(seq)

nucleo = ["G", "C", "T", "A"]

# Check if input is only dNTPs
for i in liseq:
  if i in nucleo:
    pass
  else:
    exit()

# Empty strings of (un)methylated sequences
meth_seq = ""
unmeth_seq = ""

# For unmethylated sequence every cytosine is changed to uracile
for i in liseq:
  if i != "C":
      unmeth_seq += i
  else:
      unmeth_seq += "U"

# If sequence CpG islands are methylated
for i in range(len(liseq)):
    if liseq[i] != "C":
        meth_seq += liseq[i]
    if liseq[i] == "C":
        if liseq[i+1] == "G":
            meth_seq += liseq[i]
        else:
            meth_seq += "U"

# Print results in a different new lines 
print("\nORIGINAL SEQUENCE\n"+seq)
print("\nUNMETHYLATED SEQUENCE\n"+unmeth_seq)
print("\nMETHYLATED SEQUENCE\n"+meth_seq)
