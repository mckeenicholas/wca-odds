# !/bin/bash
curl https://www.worldcubeassociation.org/results/misc/WCA_export.tsv.zip --output WCA_export.zip
unzip WCA_export.zip
grep -E '[A-Za-z]2022\s|[A-Za-z]2023\s' WCA_export_Results.tsv > ../WCA_export_Results.tsv
rm *.tsv WCA_export.zip README.md metadata.json
