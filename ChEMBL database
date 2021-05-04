from chembl_webresource_client.new_client import new_client
import pandas as pd

"""
Sphingosine-1-phosphate receptor 1 target research on ChEMBL database
"""


target = new_client.target
#Search for target
target_query = target.search('s1pr1')

pd.set_option("display.max_columns", None)
#Find all corresponding targets
targets = pd.DataFrame.from_dict(target_query)
# print(targets)

#Select target that you want to choose from database
selected_target = targets.target_chembl_id[2]
# print(selected_target)

#Find molecules that act on target
activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")

# print(res)
#Convert dictionary to datframe
df = pd.DataFrame.from_dict(res)
# Check for data contamination
df.standard_type.unique()
# Delete empty data
df2 = df[df.standard_value.notna()]


bioactivity_class = []
for i in df2.standard_value:
    if float(i) >= 10000:
        bioactivity_class.append("inactive")
    elif float(i) <= 1000:
        bioactivity_class.append("active")
    else:
        bioactivity_class.append("intermediate")
#Create list of molecules ChEMBL ID
molec_id = []
for i in df2.molecule_chembl_id:
  molec_id.append(i)

#Create list of smiles
canonical_smiles = []
for i in df2.canonical_smiles:
  canonical_smiles.append(i)

#Create list of standard values
standard_value = []
for i in df2.standard_value:
  standard_value.append(i)

# Create dataframe from multiple lists
data_tuples = list(zip(molec_id, canonical_smiles, bioactivity_class, standard_value))
df3 = pd.DataFrame(data_tuples,  columns=['ChEMBL ID', 'Canonical Smiles', 'Bioactivity class', 'standard value'])
print(df3)

# Convert results to excel
df3.to_excel("Output_bio.xlsx", sheet_name="ChEMBL DATABASE")
