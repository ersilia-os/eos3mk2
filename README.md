# BBBP model tested on marine-derived kinase inhibitors

Judges whether a compound is likely to reach the brain, developed by Plisson and Piggott to triage marine-derived kinase inhibitors as candidates for neurodegenerative disease. Random forest, gradient boosting and logistic regression classifiers were fitted to a training set of 332 previously reported small molecules, reaching 80 to 82% cross-validated accuracy, then applied to 471 marine natural products with reported kinase inhibition, of which 13 were predicted to cross the barrier. Ersilia distributes a replicated implementation; those 13 predictions were never tested experimentally.

This model was incorporated on 2024-10-23.Last packaged on 2026-04-13.

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
- **Interpretation:** Three classifier scores for blood-brain barrier permeability, from random forest, gradient boosting and logistic regression.

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
- **Model Size (Mb):** `9`
- **Environment Size (Mb):** `711`
- **Image Size (Mb):** `741.72`

**Computational Performance (seconds):**
- 10 inputs: `32.45`
- 100 inputs: `249.57`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/plissonf/BBB-Models](https://github.com/plissonf/BBB-Models)
- **Publication**: [https://doi.org/10.3390/md17020081](https://doi.org/10.3390/md17020081)
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
