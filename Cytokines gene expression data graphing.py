import pandas as pd
from matplotlib import pyplot as plt
from google.colab import files


""" THIS CODE IS USED FOR CYTOKINES GENE EXPRESSION GRAPHING"""

#Uploaded .csv file
uploaded = files.upload()

#Configured plot style
plt.style.use("bmh")

# Opening .csv file
data = pd.read_csv("citokinai.csv")

# Select appropriate columns for a bar chart
genes = data["Gene ID"]
logFC = data["log2FoldChange"]
lfcSE = data["lfcSE"]

# Configure labels position and a bar chart coloring
plt.bar(genes, logFC, color = "Purple")
plt.xticks(rotation=90)

# Create error bars with standard deviation
plt.errorbar(genes, logFC, yerr =lfcSE, fmt = " ", color = "Black", linewidth = 0.4, capsize = 1)

# Configure x,y axis labels, title
plt.xlabel('Genes ID')
plt.ylabel('Log2FoldChange')
plt.title('Citokines expression')

# Makes subplot to fits in to the figure area. Basically, looks nicer
plt.tight_layout()

# Save graph in png format
plt.savefig("figure.png", dpi=600)

# Show graph
plt.show()
