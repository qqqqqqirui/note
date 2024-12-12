---
---
---

# INFO 250: Information Visualization (Fall, 2024)

# Project2 

### Project Title: Chart visualization analysis

### Team ID:26 (Class 2)

### Student(s):Sihan Li, Qirui Zhang, Chenbang You,Boyuan Chen

### School:Lanzhou University

### Date:2024/12/13

---   
### PS:Considering the problem of image display or code running failure due to different configuration environments, we uploaded our notebook document online for easy viewing. Here is the link of our collection of notebook, markdown file and html file:    
https://www.kaggle.com/code/qiruizhang123/project2     
---
# Introduction

In today's society, with the increasing economic downturn, the incidence of global anxiety and depression is rising year by year, making the treatment of depression an increasingly important public health issue. The pathogenesis of depression is complex, involving multiple biological, psychological, and socio-environmental factors. Consequently, there are various medical treatment options for depression, including pharmacological and psychological therapies.

In the pharmacological treatment of depression, recent research has begun to focus on the molecular mechanisms of depression and explore new therapeutic targets. The interaction of death-associated protein kinase 1 (DAPK1) with the C-terminus of the 2B subunit (GluN2B) of the N-methyl-D-aspartate receptor (NMDAR) plays a critical role in the pathophysiology of depression and is considered a potential target for the structure-based discovery of new antidepressants. We have noted that researchers from Zhejiang University and Chongqing University published a study in 2018 on the interaction between DAPK1 and GluN2B, titled "Prediction of GluN2B-CT1290-1310/DAPK1 Interaction by Protein–Peptide Docking and Molecular Dynamics Simulation" [1]. 

This paper primarily used computational methods such as protein-peptide docking and molecular dynamics (MD) simulation to predict the mechanism of interaction between DAPK1 and the C-terminal residues 1290-1310 of GluN2B. Additionally, through per-residue free energy decomposition and in silico alanine scanning analysis, the study identified hot spots within the DAPK1 and GluN2B-CT1290-1310 complex. The research revealed the mechanism of interaction between GluN2B-CT1290-1310 and DAPK1 and provided insights for the discovery of drugs with this novel binding mechanism based on structural information.

Furthermore, upon carefully reviewing this paper, we identified areas where improvements could be made in the visualization of the experimental results and have proposed our suggestions for enhancement.


<div style="page-break-after: always;"></div>


---
# Background of Selected Visualization  


When reviewing the aforementioned paper, we observed that the researchers initially conducted per-residue binding free energy decomposition calculations for the simulated DAPK1 and Glu2B-CT1290-1310 complex, obtaining separate energy contribution estimates for 21 major residues of the simulated DAPK1-Glu2B complex. Based on the results of the per-residue binding energy decomposition of the simulated complex, the researchers identified the nine hotspot residues with the greatest contributions. Subsequently, the researchers performed alanine scanning on the selected nine hotspot residues to obtain their binding free energies. Finally, the researchers draws bar charts for both the per-residue binding energy decomposition results of the simulated complex and the binding free energies of the hotspot residues obtained from alanine scanning, placing one above the other for comparative verification.

As shown in the figure below, the chart is divided into two parts: the upper and lower halves.
The upper half of the chart's orange bar graph displays the 21 major residues of the simulated DAPK1-Glu2B complex, with estimated energy contributions calculated using the per-residue binding energy decomposition method. Each residue's calculated absolute binding free energy value (absolute value) exceeded 0.60 kcal/mol, which are: Gly20, Val27, Glu100, Lys141, Glu143, Met146, Ile160, Asp161, Arg302, Gln1291, Asn1294, Leu1298, Arg1300, His1302, Ser1303, Tyr1304, Asp1305. Among them, Glu100, Gln1291, and Arg1300 had the most significant contributions, with values of -5.85 kcal/mol, -6.36 kcal/mol, and -5.92 kcal/mol, respectively. The combined energy contribution of these residues accounts for 78% of the total binding free energy, leading the article to conclude that these residues are key parts of the DAPK1-Glu2B complex.

The lower half of the chart's black bar graph illustrates the binding free energies of the hotspot residues determined by alanine scanning of the DAPK1-Glu2B complex interface, with each residue's absolute binding free energy value (absolute value) exceeding 2 kcal/mol. There are a total of 9 residues, which are: Gly20, Val27, Glu143, Met146, Ile160, Asp161, Gln1291, Arg1300. These residues have significantly lower binding free energies (larger negative values), indicating a stronger affinity for ligand binding and a significant role in enhancing the stability of the DAPK1-Glu2B complex. Additionally, by analyzing the results of the alanine scanning, it can be determined that Glu100 has the greatest impact on binding free energy and is a relatively key residue in the DAPK1-Glu2B complex.

Overall, the chart displays the calculated energy contributions of each residue in the simulated complex and the actual binding free energies of the top nine contributing residues, essentially showcasing the effectiveness of the simulated complex in experimental validation.

Explanation of some experimental terms:

- Residue: In the structure of proteins and peptides, a residue typically refers to the structural unit of an amino acid molecule. In a polypeptide chain, the carboxyl and amino groups of amino acids connect sequentially to form peptide bonds. After losing a molecule of water, a specific amino acid in the polypeptide is called a "residue." For example, a part of glutamic acid (Glu) in a polypeptide chain is referred to as a "glutamic acid residue," generally denoted by its one-letter code (E) or three-letter code (Glu).
  
- DAPK1, Glu2B, GluN2B-CT1290-1310: DAPK1 refers to Death-Associated Protein Kinase 1, GluN2B is the Glutamate Receptor, Ionotropic, N-Methyl-D-Aspartate 2B subunit, and GluN2B-CT1290-1310 denotes the C-terminal sequence of amino acids 1290 to 1310 of the GluN2B subunit, which together play a significant role in the pathophysiology of depression and are targets for the development of new antidepressant drugs.
  
- Simulated complex: The original paper used a combined strategy of protein-peptide docking and molecular dynamics (MD) simulation to simulate the interaction of DAPK1 with GluN2B-CT1290-1310. The complex was assessed using methods such as MD simulation, binding free energy calculation, and molecular mechanics Poisson-Boltzmann surface area (MM/GBSA).
  
- Alanine scanning: Alanine scanning is a commonly used experimental technique for identifying important amino acid residues in proteins. By replacing an amino acid at a specific position with alanine, researchers can assess the importance of that amino acid in maintaining the protein's structure and function. The replaced residue is usually denoted by a one-letter code-number-alanine code (A).
  
- Binding free energy:
Binding free energy refers to the change in free energy involved when a ligand binds to its target protein. Generally, a negative binding free energy value indicates a stronger affinity between the ligand and the protein, and higher stability. The analysis of binding free energy is often used to quantify the interaction strength between two molecules and to predict the activity of the complex in the body.

- Hotspot residues:
Hotspot residues are amino acid residues that significantly affect the binding energy or function in proteins or protein complexes.

- Residue naming method: In this paper, there are three main methods of residue naming. The first is the three-letter (identifying a specific amino acid)-position number format, the second is directly using the position number to represent the residue, and the third is the one-letter (identifying an amino acid)-position number-alanine number (A) format, indicating that in the alanine scanning experiment, the amino acid identified by a single letter was replaced with alanine (A).
  
- Per-residue binding energy decomposition: Per-residue binding energy decomposition is a computational method used to determine the contribution of individual amino acid residues to the overall binding affinity of a complex. It typically includes the following steps:
  
- Molecular dynamics; energy calculation: Using methods such as molecular mechanics/Poisson-Boltzmann surface area (MM/PBSA) or molecular mechanics/Generalized Born surface area (MM/GBSA) to calculate binding free energy and estimate the contributions of individual residues.That is, using the aforementioned methods, the total binding energy is decomposed into the contributions of each residue, highlighting the positive and negative roles.

[![2024-12-11-19-42-16.png](https://i.postimg.cc/Kjxvs25j/2024-12-11-19-42-16.png)](https://postimg.cc/5YKV6DTW)

---
# Issues with the Original Chart


The bar charts of residue binding energy contributions and relative binding free energies in the paper present the results of the analysis and decomposition of the simulated DAPK1-Glu2B complex, but they are rather confusing and require the following improvements:

- High information density: The original chart has a high information density, which can easily confuse readers (or other researchers). We hope that the improved chart will make the data easier to interpret.
  
- Misaligned label positions: In the original chart, some x-axis labels (residues) in the upper and lower parts represent the energy contributions of the same residue and the relative binding free energy obtained from alanine scanning as a hotspot residue, but it is actually difficult for readers to identify the corresponding bars for the same residue above and below, affecting the readability of the experimental results.
  
- Inconsistent residue naming: The upper labels represent residues by their position in the protein amino acid sequence, while the lower representation uses a one-letter-code-position number-alanine number (A) format to identify the relative free binding energy of different residues. Residues labeled in two different ways can easily mislead readers into thinking they are two different residues.
  
- Inconsistent subplot directions: The energy contribution values and relative binding free energy values represented in the upper and lower parts of the original chart are both negative, but the original chart uses different directions to represent the two types of energy values, which can easily mislead readers into thinking the energy values are one positive and one negative.
  
- Unclear comparison of calculation and scanning results: In the original chart, after calculating the binding energy contributions of 21 residues in the simulated Glu100-CT1290-1310/DAPK1 complex, the researchers selected the 9 residues with the greatest contributions and verified them through alanine scanning, but the original chart does not highlight the comparison results of the calculation and scanning results.
  
- Label sorting does not highlight key information: The residue labels in the original chart are sorted by the position number of the amino acids, but the original chart focuses on selecting hotspot residues and displaying the relative free binding energy obtained from the scanning of the selected hotspot residues, but the original chart's sorting does not highlight the hotspot residues with greater contributions, therefore improvements are needed.


We choose to improve this part of the chart to better support the visualization of the paper, facilitating the understanding and citation by subsequent researchers. Our work can play a certain role in lubricating the reading and research of this paper within the field.






&nbsp;

[![2024-12-11-00-11-36.png](https://i.postimg.cc/rF5b8Yqq/2024-12-11-00-11-36.png)](https://postimg.cc/w7TF22tr)

<div style="page-break-after: always;"></div>

---
# Improved Chart 1


Based on the above analysis, we have made preliminary changes to the chart:
- First, we standardized the chart labels, and in this chart, we represent residues by their position numbers.

- In the middle section, we list all residues by their numbers. If there are common residues in the upper and lower synthetic subgraphs, then the residue will have both an upward and a downward bar chart.

- The upward part represents the hot spot residues' binding free energy obtained from the alanine scan, and the downward part represents the energy contribution of the residues, allowing us to more directly observe the energy contribution and the difference in relative binding free energy values of the 9 hot spot residues.

Through the optimized chart, we can draw some new conclusions:

- For the 9 hot spot residues, most residues with a larger energy contribution also tend to have a larger relative binding free energy value, generally showing a relationship where the relative binding free energy value is several times the energy contribution.

- However, it should be noted that this characteristic does not apply to residues Leu1298 and Ser1303. The energy contribution of residue Ser1303 is slightly larger than its relative binding free energy value, while the energy contribution of Leu1298 is more than double its relative binding free energy value.

- Therefore, special attention should be paid to residues Leu1298 and Ser1303. Based on the above analysis, these two residues may not play a significant role in the stability of protein structure and function. In subsequent research, we can attempt to remove these two residues to see if it affects the protein's structure and function.

The shortcomings of this image are:
- Indicating residues by their position numbers, this method, which only uses numbers, makes it difficult for readers to understand the specific meaning of the residues.
  
- The x-axis is sorted in ascending order according to the position numbers, which does not help researchers quickly grasp the key points.

- Both the energy contribution and the hot spot binding free energy are negative values, but using an upward and a downward method to describe them can lead to misunderstandings among readers.

- The upper half of the chart with hot spot binding free energy is rather sparse, and the data is too dispersed.



&nbsp;

[![2024-12-11-18-26-25.png](https://i.postimg.cc/XJ9TYTDL/2024-12-11-18-26-25.png)](https://postimg.cc/MMKssrwf)



&nbsp;
---
# Improved Chart 2


Based on the issues identified in the previous chart, we have made the following changes to the chart:
- First, we have re-sorted both the energy contribution values and the relative binding free energy values in ascending order according to their magnitude to more clearly display the order of energy contributions of the residues.

- Next, we have standardized the x-axis labels (residues) by adopting a three-letter (identifying specific amino acids) - position number format for uniform naming.

- Then, we have placed the sorted bar charts in an up-down manner. Different from the original chart, we have chosen to place the binding free energy of hot spot residues obtained from the alanine scan, which has relatively smaller data volume, on top. We have adjusted the orientation of the bar charts and represented this data with blue bars to more easily observe the binding free energy relationships of the hot spot residues.

- Finally, we have placed the 21 main residues of the simulated DAPK1-Glu2B complex in the lower half, and represented the 9 most contributing hot spot residues in blue, while the remaining residues are indicated in orange.

From the optimized chart, we can draw some new conclusions:
For the upper half of the chart:

- The lower half of the graph describes the 21 major residues of the simulated DAPK1-GluN2B complex. The estimated values of the energy contributions of each residue are calculated using a per-residue binding energy decomposition method. Each residue's calculated absolute binding free energy value (the absolute value) exceeds 0.60 kcal/mol.

- Among the 9 most contributing hot spot residues, Glu100 has the lowest (most negative) binding free energy, playing the greatest role in enhancing the stability of the DAPK1-Glu2B complex and having the strongest affinity for the ligand.

- Arg1300, Arg302, His1302, and Gln1291 have slightly lower binding free energy compared to Glu100, but these residues have relatively low (more negative) binding free energy and strong affinity for the ligand, greatly contributing to the stability of the DAPK1-Glu2B complex. The remaining residues Tyr1304, Lys141, Leu1298, and Ser1303 have relatively smaller binding free energy compared to the previously mentioned residues.

- Therefore, Glu100, Arg1300, Arg302, His1302, and Gln1291 have significant importance in maintaining the protein structure and function. Residues Tyr1304, Lys141, Leu1298, and Ser1303 play a smaller role in maintaining the protein structure and function compared to other residues. In the research process, we can prioritize retaining the more important residues and further study their specific relationships with the protein structure and function to discover which residues in the DAPK1-Glu2B complex are essential for maintaining the protein's structure and function.

For the lower half of the chart:
- Regarding the absolute binding free energy values of the 21 main residues, we can observe that Gln1291 has the largest energy contribution at -6.36 kcal/mol, while Arg1300 contributes -5.92 kcal/mol, and Glu100 is third at -5.85 kcal/mol.

- There is a small difference in energy contributions between residues in close proximity, but overall, the difference between the maximum and minimum energy contributions of the residues is too large, with Gln1291 contributing the most at -6.36 kcal/mol, while Arg301 contributes only -0.73 kcal/mol.

- Therefore, we can identify Glu100, Gln1291, and Arg1300 as the most significant contributors. These residues have a higher interaction strength between the two molecules and are more active. We can focus on these residues, but residues Met146, Phe299, Asn1294, and Arg301 have lower contributions, less than 1 kcal/mol, indicating that these residues may not be key parts of the DAPK1-Glu2B complex.

The shortcomings of this chart are:
- Due to the large amount of data and high information density for the 21 main residues, it is inconvenient to observe.

- The chart is divided into two parts, making it difficult to clearly observe the relationship between the energy contributions and relative binding free energy values of the same residue.

<video width="1600" height="450" controls>
    <source src="https://media-hosting.imagekit.io//1f77477d51ab4a8c/%E5%B1%8F%E5%B9%95%E5%BD%95%E5%88%B6%202024-12-10%20232739.mp4?Expires=1734093835&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=s5DR3GoDWSUZfF5Un6tMWWqYxXxYlIl7DDcHC8LlyWmHFZnbTtftY7TscCw0X3D6cwigYxeDCCqp~0avwjGg4DmyvI1dM6OV~dB1HoiDXd~q2UVnHSs7jKNWzpvB9lEYDUiE7mjhRqjfa8egrh5ivKS43dT3d0lM9A2XrzF33N4gSai2gEihIjdcYJODLzuzGjTQXG4NM-yXsDTJe9d6xGqjybW0mSUVvpSVCYtWyjHyk9Mi-~EOTG~n5s8GZNu-w9spmCvoYv9amOIVGw1RtLE1ls-7HhL30TQZfToqSGjdkwEwjtYWXkiNpu1dGttN2ux0BeuOGDynzP7RahBBxA" type="video/mp4">
</video>      


---
# Improved Chart 3


We have made dynamic modifications to the chart here:
- The x-axis is uniformly named in the format of three-letter (identifying specific amino acids) - position number.

- The 9 most contributing hot spot residues are placed in the upper half, sorted in ascending order by value and represented by blue bars.

- Here, we place the 21 main residues in the lower half, sorted in ascending order by value, with the 9 hot spot residues represented by blue bars and the rest by orange bars.

- By hovering the mouse over each bar, we can get a specific description of that bar, including the name of the residue, the name of the described value (such as relative binding free energy, energy contribution), the corresponding unit, and the specific value.

- By placing our mouse over a residue that has both energy contribution and relative binding free energy values, the color of the bars corresponding to the energy contribution and relative binding free energy of that residue will change.

Here, we have resolved all the issues and drawbacks mentioned above through visualization. This chart has the following characteristics:

- The data intervals are appropriate, making it easy to observe.

- The text labels are unified, named in the format of three-letter (identifying specific amino acids) - position number, which is easy for researchers to read.

- Related information is linked, allowing for easy comparison of the energy contributions and relative binding free energy values of the 9 main contributing residues.

- The direction of the sub-charts is unified, causing no misunderstanding to the readers.

- The original chart highlights the comparison results of computational and scanning results.

- The labels highlight key information, and by hovering the mouse over the required bar chart, key information can be obtained.

From observing the chart, we draw the following conclusions:

- For the absolute binding free energy values of the 21 main residues which is DAPK1-Glu2B compound and simulated by researchers, we can observe that Gln1291 has the largest energy contribution at -6.36 kcal/mol, while Arg1300 contributes -5.92 kcal/mol, and Glu100 is third at -5.85 kcal/mol.

- There is a small difference in energy contributions between residues in close proximity, but overall, the difference between the maximum and minimum energy contributions of the residues is too large, with Gln1291 contributing the most at -6.36 kcal/mol, while Arg301 contributes only -0.73 kcal/mol.

- Therefore, we can identify Glu100, Gln1291, and Arg1300 as the most significant contributors. These residues have a higher interaction strength between the two molecules, are more active, and we can focus on these residues. However, residues Met146, Phe299, Asn1294, and Arg301 have lower contributions, less than 1 kcal/mol, indicating that these residues may not be key parts of the DAPK1-Glu2B complex.

- The 9 most contributing residues have significantly lower (more negative) binding free energy, indicating a stronger affinity for the ligand and a significant role in enhancing the stability of the DAPK1-Glu2B complex. Additionally, by analyzing the alanine scan results, we can determine that Glu100 has the greatest impact on binding free energy and is a more critical residue in the DAPK1-Glu2B complex.

- For the 9 hot spot residues, most residues with a larger energy contribution also tend to have a larger relative binding free energy value, generally showing a relationship where the relative binding free energy value is several times the energy contribution.

- However, it should be noted that this characteristic does not apply to residues Leu1298 and Ser1303. The energy contribution of residue Ser1303 is slightly larger than its relative binding free energy value, while the energy contribution of Leu1298 is more than double its relative binding free energy value.

- Therefore, special attention should be paid to residues Leu1298 and Ser1303. Based on the above analysis, these two residues may not play a significant role in the stability of protein structure and function. In subsequent research, we can attempt to remove these two residues to see if it affects the protein's structure and function.

---
# Conclusion

In today's society, depression is gradually becoming an increasingly important public health issue. In the pharmacological treatment of depression, recent research has begun to focus on the molecular mechanisms of depression and explore new therapeutic targets. We have noted that researchers from Zhejiang University and Chongqing University published a study in 2018 on the interaction between DAPK1 and GluN2B, titled "Prediction of GluN2B-CT1290-1310/DAPK1 Interaction by Protein–Peptide Docking and Molecular Dynamics Simulation" [1]. This study revealed the mechanism of interaction between GluN2B-CT1290-1310 and DAPK1. Regarding the bar chart depicting the results of the per-residue binding energy decomposition and the binding free energy of the nine hot spot residues obtained from alanine scanning in the simulated complex presented in the paper, we have proposed improvements in the visualization. We found that the chart had issues such as high information density, misaligned labels, inconsistent residue naming, and a lack of uniformity in the direction of the subplots. Therefore, we have improved the chart by reordering it according to the magnitude of values, standardizing the naming format for labels (residues), and dynamicizing the image.

Furthermore, by observing the improved chart, we have reached the following conclusions: Glu100, Arg1300, Arg302, His1302, and Gln1291 play a significant role in enhancing the stability of the DAPK1-GluN2B complex and may be crucial for maintaining protein function and structure. However, Leu1298 and Ser1303 have energy contributions that are slightly larger than their relative binding free energy values, suggesting that they may not be as significant for maintaining protein function and structure.

