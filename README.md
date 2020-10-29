# Optical Chemical Structure Recognition - Benchmark

- This repository contains the information related to the benchmark study on openly available OCSR tools

## Materials and methods

- In order to compare the results of the three available open-source OCSR tools Imago (version 2.0), MolVec (version 0.9.7) and OSRA (version 2.1.0), multiple datasets which are freely available online were analyzed according to the validation procedure of the OSRA developers (4). The datasets were::

  - A set of 5719 images of chemical structures and the corresponding molfiles (based on data from the USPTO) obtained from the OSRA online presence (4). 

  - The dataset (UOB) of 5740 images and molfiles of chemical structures developed by the University of Birmingham, United Kingdom, and published alongside MolRec  (6). 

  - The Conference and Labs of the Evaluation Forum (CLEF) test set of 961 images and molfiles published in 2012 (7).

  - A subset (450 images and SDfiles) of a dataset published with ChemInfty (see above) based on data from the Japanese Patent Office (JPO), obtained from the OSRA online presence (4). (Note that this dataset contains many labels (sometimes with Japanese characters) and irregular features, such as variations in the line thickness. Additionally, some images have a poor quality and contain a lot of noise.) 

- The TIFF images were converted to PNG images with a resolution of 72 dpi to assure comparability, as MolVec and Imago both showed problems handling those TIFF files in batch mode.

- Converted Images can be found on the [input](https://github.com/Kohulan/OCSR_Review/tree/master/assets/images) directory

### Running Imago
- Command line version of Imago (9) was used here.
```
./imago_console -dir /image/directory/path
```

### Running MolVec with parallelization
```
java -cp molvec-0.9.7.jar:common-image-3.4.1.jar:common-io-3.4.1.jar:common-lang-3.4.1.jar:commons-cli-1.4.jar:imageio-core-3.4.1.jar:imageio-metadata-3.4.1.jar:imageio-tiff-3.4.1.jar:ncats-common-0.3.3.jar:ncats-common-cli-0.9.1.jar gov.nih.ncats.molvec.Main -dir /image/directory/path -outDir /output/directory/path
```

### Running OSRA

- OSRA was installed in an Anaconda environment using the Conda recipe for PyOSRA which was published by Ed Beard (10). This was done analogously to the installation instructions in the ChemSchematicResover documentation (11). We use the PyOSRA environment because compiling OSRA from source code is excessively complex as it has a lot of dependencies that need to be compiled from their own source code as well. There is the option to obtain a commercial license to get a precompiled version of the software.

```
for image in *.png; do osra -f sdf -a /path/to/superatom/dictionary/superatom.txt -l /path/to/spelling/corrections/dictionary/spelling.txt -w /output/path/$image.sdf $image;done
```

### Results

- Time elapsed and accuracy reported for the open-source OCSR tools
 
  - The accuracies of the tools listed in Table above correspond to perfectly-recognized structures according to a perfect match of the Standard InChI strings (12) that were created based on the OCSR results and the reference files.

Dataset | | MolVec 0.9.7 | Imago 2.0 | OSRA 2.1
--- | --- | --- | --- | ---
USPTO | Time (min) | 28.65 | 72.83 | 145.04
*(5719 images)* | Accuracy | 88.41% | 87.20% | 87.69%
 UOB | Time (min) | 28.42 | 152.52 | 125.78
 *(5740 images)* | Accuracy | 88.39% | 63.54% | 86.50%
CLEF 2012 | Time (min) | 4.41 | 16.03 | 21.33
*(961 images)* | Accuracy | 80.96% | 65.45% | 94.90%
JPO | Time (min) | 7.50 | 22.55 | 16.68
*(450 images)* | Accuracy | 66.67% | 40.00% | 57.78%

- (a) Accuracy (Right: higher the better) and (b) Total time for processing (Left: lower the better)

Accuracy | Total time for processing
--- | ---
![GitHub Logo](https://github.com/Kohulan/OCSR_Review/blob/master/assets/OCSR_1.png?raw=true) | ![GitHub Logo](https://github.com/Kohulan/OCSR_Review/blob/master/assets/OCSR_2.png?raw=true)
Figure 1 | Figure 2

#### Conclusion

- As shown in the Table, MolVec processes the images significantly faster than its competitors. All three tools performed fairly well on the given set of images. As illustrated in Figure 1, the proportion of accurate results produced by MolVec and OSRA with the UOB, CLEF and JPO datasets was approximately 20% higher than in the results produced by Imago. The lower overall performance of all three tools with the JPO dataset is likely due to the lower quality of the depictions, the presence of labels and other irregular features. The extraordinarily good performance of OSRA on the CLEF dataset is a notable observation. The examination of the images in the dataset reveals a set of well-segmented, clean chemical structure depictions which is seemingly handled especially well by OSRA.

## References
1.	Smolov V, Zentsev F, Rybalkin M. Imago: Open-Source Toolkit for 2D Chemical Structure Image Recognition. In: TREC [Internet]. Citeseer; 2011. Available from: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.471.8925&rep=rep1&type=pdf\
2.	Nguyen D-T. Molvec [Internet]. ACS Meeting; 2019; San Diego. Available from: https://molvec.ncats.io
3.	Filippov IV, Nicklaus MC. Optical structure recognition software to recover chemical information: OSRA, an open source solution. J Chem Inf Model. 2009 Mar;49(3):740–3.
4.	OSRA validation datasets [Internet]. [cited 2020 Jun 24]. Available from: https://sourceforge.net/p/osra/wiki/Validation/
5.  Sadawi NM, Sexton AP, Sorge V. Chemical structure recognition: a rule-based approach [Internet]. Document Recognition and Retrieval XIX. 2012. Available from: http://dx.doi.org/10.1117/12.912185
6.	Molrec UOB Benchmark dataset [Internet]. [cited 2020 Jun 29]. Available from: http://www.cs.bham.ac.uk/research/groupings/reasoning/sdag/chemical.php
7.	CLEF-IP 2012 Structure Recognition Test Set [Internet]. [cited 2020 Jun 29]. Available from: http://www.ifs.tuwien.ac.at/~clef-ip/download/2012/qrels/clef-ip-2012-chem-recognition-qrels.tgz
8.  Fujiyoshi, Akio and Nakagawa, Koji and Suzuki, Masakazu. Robust Method of Segmentation and Recognition of Chemical Structure Images in ChemInfty. 2011; Available from: https://www.researchgate.net/publication/229042881_Robust_Method_of_Segmentation_and_Recognition_of_Chemical_Structure_Images_in_ChemInfty
9.	Imago Download [Internet]. [cited 2020 Jun 24]. Available from: https://lifescience.opensource.epam.com/download/imago.html
10.	Beard E. Pyosra Conda Recipe [Internet]. [cited 2020 Jun 24]. Available from: https://github.com/edbeard/conda_recipes/tree/master/pyosra
11.	ChemSchematicResolver Documentation [Internet]. [cited 2020 Jun 24]. Available from: https://www.chemschematicresolver.org/docs/install
12.	Heller S, McNaught A, Stein S, Tchekhovskoi D, Pletnev I. InChI - the worldwide chemical structure identifier standard. J Cheminform. 2013 Jan 24;5(1):7.

## Authors 
- [Kohulan](github.com/Kohulan)
- [Otto Brinkhaus](github.com/OBrink)

## Citation
- Use this bibtex to cite the work
```
@article{Rajan2020,
author = {Rajan, Kohulan and Brinkhaus, Henning Otto and Zielesny, Achim and Steinbeck, Christoph},
doi = {10.1186/s13321-020-00465-0},
file = {:Users/kohulanrajan/Downloads/s13321-020-00465-0.pdf:pdf},
issn = {1758-2946},
journal = {Journal of Cheminformatics},
keywords = {Chemical data extraction,Chemical structure,Data mining,Machine learning,Named entity recognition,Open data,Optical chemical structure recognition,chemical data extraction,chemical structure,data mining,machine learning,named entity recognition,open data,optical chemical structure recognition},
pages = {1--13},
publisher = {Springer International Publishing},
title = {{A review of optical chemical structure recognition tools}},
url = {https://doi.org/10.1186/s13321-020-00465-0},
year = {2020}
}
```

## More information about our research group
[![GitHub Logo](https://github.com/Kohulan/DECIMER-Image-to-SMILES/blob/master/assets/CheminfGit.png?raw=true)](https://cheminf.uni-jena.de)

## This work is part of the DECIMER project
[![GitHub Logo](https://github.com/Kohulan/DECIMER-Image-to-SMILES/raw/master/assets/DECIMER.gif)](https://kohulan.github.io/Decimer-Official-Site/)
