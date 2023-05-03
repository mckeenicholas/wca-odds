# !/bin/bash
curl https://www.worldcubeassociation.org/results/misc/WCA_export.tsv.zip --output WCA_export.zip
unzip WCA_export.zip
grep -E '2022\t|2023\t' WCA_export_Results.tsv > ../WCA_export_Results.tsv
rm *.tsv WCA_export.zip README.md metadata.json
    