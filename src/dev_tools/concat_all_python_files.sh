#!/bin/bash

# Define the output file
output_file="all_py_files_concatenated.txt"

# Clear the output file if it already exists
> "$output_file"

# Find all .tf files recursively and concatenate them
find . -type f -name "*.py" | while read -r tf_file; do
  echo "Processing file: $tf_file"
  echo '"""' >> "$output_file"
  cat "$tf_file" >> "$output_file"
  echo '"""' >> "$output_file"
  echo >> "$output_file"  # Add a newline for separation
done

echo "Concatenation complete. Output saved to $output_file."
