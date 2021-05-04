# Input your DNA sequence
sequence = input("")

# Create empty string to make your complementary sequence result in one line
complement_sequence = ""

# For loop that changes G into G, A into T and vice versa
for i in sequence:
  if i == "C":
    complement_sequence += "G"
  elif i == "G":
    complement_sequence += "C"
  elif i == "A":
    complement_sequence += "T"
  elif i == "T":
    complement_sequence += "A"
  else:
    print("invalid input")
    
# prints complementary sequence
print("Input seqence " + sequence)
print("Complement sequence " + complement_sequence)

# prints immature RNA
print("Input sequence immature mRNA " + sequence.replace("T", "U"))
print("Complement sequence immature mRNA " + complement_sequence.replace("T", "U"))
