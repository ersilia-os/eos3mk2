# BBBP model tested on marine-derived kinase inhibitors

A set of three binary classifiers (random forest, gradient boosting classifier, and logistic regression) to predict the Blood-Brain Barrier (BBB) permeability of small organic compounds. The best models were applied to natural products of marine origin, able to inhibit kinases associated with neurodegenerative disorders. The training set size was around 300 compounds.

## Identifiers

* EOS model ID: `eos3mk2`
* Slug: `bbbp-marine-kinase-inhibitors`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Classification score over three classifiers, namely random forest (rfc), gradient boosting classifier (gbc), and logistic regression (logres).

## References

* [Publication](https://pubmed.ncbi.nlm.nih.gov/30699889/)
* [Source Code](https://github.com/plissonf/BBB-Models)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos3mk2)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3mk2.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos3mk2) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubmed.ncbi.nlm.nih.gov/30699889/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!