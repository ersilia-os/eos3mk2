# BBBP model tested on marine-derived kinase inhibitors

A set of three binary classifiers (random forest, gradient boosting classifier, and logistic regression) to predict the Blood-Brain Barrier (BBB) permeability of small organic compounds. The best models were applied to natural products of marine origin, able to inhibit kinases associated with neurodegenerative disorders. The training set size was around 300 compounds.

This model was incorporated on 2024-10-23.

## Information
### Identifiers
- **Ersilia Identifier:** `eos3mk2`
- **Slug:** `bbbp-marine-kinase-inhibitors`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Drug-likeness`, `Permeability`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `3`
- **Output Consistency:** `Fixed`
- **Interpretation:** Classification score over three classifiers, namely random forest (rfc), gradient boosting classifier (gbc), and logistic regression (logreg).

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| rfc_score | float | high | Random forest classifier score estimating the likelihood that the compound will permeate through the blood-brain barrier |
| gbc_score | float | high | Gradient boosting classifier score estimating the likelihood that the compound will permeate through the blood-brain barrier |
| logreg_score | float | high | Logistic regression classifier score estimating the likelihood that the compound will permeate through the blood-brain barrier |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Replicated`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos3mk2](https://hub.docker.com/r/ersiliaos/eos3mk2)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3mk2.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3mk2.zip)

### Resource Consumption
- **Model Size (Mb):** `8`
- **Environment Size (Mb):** `708`


### References
- **Source Code**: [https://github.com/plissonf/BBB-Models](https://github.com/plissonf/BBB-Models)
- **Publication**: [https://pubmed.ncbi.nlm.nih.gov/30699889/](https://pubmed.ncbi.nlm.nih.gov/30699889/)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos3mk2
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos3mk2
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
