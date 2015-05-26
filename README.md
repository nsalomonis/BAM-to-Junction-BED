# BAM-to-Junction-BED
Uses SAMTools, Python 2.7 and PySam to extract either junctions or exon read counts for known and novel junctions and exons. Requires an indexed BAM file with genomic coordinates. 

# Example Commands
python BAMtoJunctionBED.py --i /Users/me/sample1.bam

python multiBAMtoBED.py --i /Users/me/BAMfiles --g /Users/me/ReferenceExonCoordinates/Hs_Ensembl_exon_hg19.txt --r /Users/me/ExonBEDRef/Hs_Ensembl_exon-cancer_hg19.bed --a exon --a junction --a reference

python multiBAMtoBED.py --i /Users/me/BAMfiles --a junction

python BAMtoExonBED.py --i /Users/me/sample1.bam --r /Users/me/Hs_exon-cancer_hg19.bed"
