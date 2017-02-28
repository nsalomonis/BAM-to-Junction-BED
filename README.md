# BAM-to-Junction-BED
Uses SAMTools, Python 2.7 and PySam to extract either junctions or exon read counts for known and novel junctions and exons. Requires an indexed BAM file with genomic coordinates. 

# Example Commands

Produce a junction.bed coordinate file from a BAM file
```
python BAMtoJunctionBED.py --i /Users/me/sample1.bam
```

Produce a junction.bed coordinate file from a BAM file without strand predictions (e.g., STAR)
```
python BAMtoJunctionBED.py --i /Users/me/sample1.bam --g /Application/BAM-to-Junction-BED/ReferenceExonCoordinates/Mm_Ensembl_exon_Mm10.txt
```
Batch analysis of many BAM files in a single directory to obtain junction.bed and exon.bed results
```
python multiBAMtoBED.py --i /Users/me/BAMfiles --g /Application/BAM-to-Junction-BED/ReferenceExonCoordinates/Hs_Ensembl_exon_hg19.txt --r /Users/me/ExonBEDRef/Hs_Ensembl_exon-cancer_hg19.bed --a exon --a junction --a reference
```
Produce a junction.bed coordinate file from a BAM file using multi-processing
```
python multiBAMtoBED.py --i /Users/me/BAMfiles --a junction --m yes 
```
Produce an exon.bed file using a reference bed file created by multiBAMtoBED or custom coordinates
```
python BAMtoExonBED.py --i /Users/me/sample1.bam --r /Users/me/Hs_exon-cancer_hg19.bed"
```
