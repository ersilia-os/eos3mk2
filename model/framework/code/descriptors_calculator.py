import numpy as np
import pandas as pd
import tempfile
from tqdm import tqdm
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.ML.Descriptors import MoleculeDescriptors
from rdkit.Chem import Descriptors


def calculate_conformers(smiles_list):

    smis_mini = smiles_list
    names_mini = ["molecule_{}".format(i) for i in range(len(smiles_list))]
    names = names_mini

    print("Creating temporary file to store conformers")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".sdf") as tmp:
        tmp_name = tmp.name

    print("Generating conformers")
    w = Chem.SDWriter(tmp_name)
    rms_dict = dict()
    valid_indices = []
    for j in tqdm(range(len(smis_mini))):
        try:
            m = Chem.MolFromSmiles(smis_mini[j])
            if m is None:
                raise ValueError("Could not parse SMILES: {}".format(smis_mini[j]))
            m2 = Chem.AddHs(m)
            # run the new CSD-based method
            cids = AllChem.EmbedMultipleConfs(m2, numConfs=10, params=AllChem.ETKDG())
            if len(cids) == 0:
                raise ValueError("Could not embed conformers for SMILES: {}".format(smis_mini[j]))
            for cid in cids:
                _ = AllChem.MMFFOptimizeMolecule(m2, confId=cid)
                m2.SetProp("_Name", names_mini[j])
                Chem.MolToMolBlock(m2)

                rmslist = []
                AllChem.AlignMolConformers(m2, RMSlist=rmslist)
                rms_dict[names[j]] = rmslist
            w.write(m2)
            valid_indices.append(j)
        except Exception as e:
            print("Warning: could not process SMILES at index {}: {}".format(j, e))
    w.close()

    print("Reading the conformers file")
    dataset = [mol for mol in Chem.SDMolSupplier(tmp_name) if mol is not None]
    return dataset, valid_indices


def descriptors_calculator(smiles_list):
    print("Calculating conformers")
    dataset, valid_indices = calculate_conformers(smiles_list)

    print("Calculating descriptors")
    nms=[x[0] for x in Descriptors._descList]
    calc = MoleculeDescriptors.MolecularDescriptorCalculator(nms)
    print(len(nms))

    datasetDescrs = [calc.CalcDescriptors(x) for x in dataset]
    datasetDescrs = np.array(datasetDescrs)

    df = pd.DataFrame(datasetDescrs, columns=nms)
    return df, valid_indices