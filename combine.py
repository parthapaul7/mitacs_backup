import os
import json
import glob

# Directory pattern to search for the JSON files
pattern = 'patrick_set/0*/*opt*/*uwb97xd_def2tzvpd*/data_denspart.json'

# Initialize an empty dictionary to store the combined data

combined_data={}
# Loop through each JSON file matching the pattern
for file_path in glob.glob(pattern, recursive=True):
    # Extract the directory name part that contains the numeric key
    dir_name = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
    
    # Extract the first four digits from the directory name
    numeric_part = ''.join(filter(str.isdigit, dir_name))[:4]
    
    # Read the JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Initialize the main structure if the key doesn't exist
    if numeric_part not in combined_data:
        combined_data[numeric_part] = {}
    
    # Merge atnums and atcoords directly under the main key if they exist
    # give me the first key of data 
    
    first_key = list(data.keys())[0]
    if "atnums" in data[first_key]:
        combined_data[numeric_part]["atnums"] = data[first_key]["atnums"]
    if "atcoords" in data[first_key]:
        combined_data[numeric_part]["atcoords"] = data[first_key]["atcoords"]
    
    # Add the rest of the data under their respective keys
    combined_data[numeric_part][first_key] = {}
    for key, value in data[first_key].items():
        if key not in ["atnums", "atcoords"]:
            combined_data[numeric_part][first_key][key] = value

# Sort the combined data by keys in increasing order
sorted_combined_data = dict(sorted(combined_data.items()))

# Output file path
output_file = 'data_database_uwb97xd.json'

# Write the combined data to the output JSON file
with open(output_file, 'w') as outfile:
    json.dump(sorted_combined_data, outfile, indent=4)

print(f"Combined data has been written to {output_file}")