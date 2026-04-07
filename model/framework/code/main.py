# imports
import os
import csv
import sys
import joblib
import numpy as np
import pandas as pd

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.join(root, "..", "..", "checkpoints")

# append system path
sys.path.append(root)
from charge_neutralizer import NeutraliseCharges
from descriptors_calculator import descriptors_calculator

# loading scaler
scaler = joblib.load(os.path.join(checkpoints_dir, "scaler.joblib"))

# loading models
model_1 = joblib.load(os.path.join(checkpoints_dir, "model1_rfc.joblib"))
model_2 = joblib.load(os.path.join(checkpoints_dir, "model2_gbc.joblib"))
model_3 = joblib.load(os.path.join(checkpoints_dir, "model3_logreg.joblib"))

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# neutralize charges
neutralized_smiles = []
for smiles in smiles_list:
    neutralized_smiles += [NeutraliseCharges(smiles)[0]]

print(neutralized_smiles)

# calculate descriptors
descriptors, valid_indices = descriptors_calculator(neutralized_smiles)
descriptors = np.array(descriptors)

# normalize descriptors
descriptors = np.array(pd.DataFrame(scaler.transform(descriptors)).fillna(0))

# run models
output_1 = model_1.predict_proba(descriptors)[:, 1]
output_2 = model_2.predict_proba(descriptors)[:, 1]
output_3 = model_3.predict_proba(descriptors)[:, 1]

# reconstruct output preserving original order; use " " for failed entries
valid_pos = {orig_idx: pos for pos, orig_idx in enumerate(valid_indices)}
outputs = []
for i in range(len(smiles_list)):
    if i in valid_pos:
        pos = valid_pos[i]
        outputs.append([float(output_1[pos]), float(output_2[pos]), float(output_3[pos])])
    else:
        outputs.append([" ", " ", " "])

#check input and output have the same length
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["rfc_score", "gbc_score", "logreg_score"])  # header
    for o in outputs:
        writer.writerow(o)
