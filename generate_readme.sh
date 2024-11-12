#!/bin/bash

# run the python script to scrape the solutions
python meta/scrape_solutions.py

# Extract everything before the include-solutions placeholder
sed '/<!-- include-solutions -->/q' README.md > temp_README.md

# # Add the start placeholder
# echo "<!-- include-solutions -->" >> temp_README.md

# Append meta/solutions.md content
cat meta/solutions.md >> temp_README.md

# Add the end placeholder
echo "<!-- stop-solutions -->" >> temp_README.md

# Append everything after the stop-solutions placeholder
sed -n '/<!-- stop-solutions -->/,$p' README.md | tail -n +2 >> temp_README.md

# Overwrite README.md with the new file
mv temp_README.md README.md
