import json

# Load JSON data from a file
with open('patrick_set/data_database_uwb97xd.json', 'r') as file:
    data = json.load(file)


with open('patricks_set_data/data_database_uwb97xd.json', 'r') as file:
    reference = json.load(file)

ref_keys = list(reference.keys())
keys = list(data.keys())

to_del = []

for key in keys:
    if key not in ref_keys:
        to_del.append(key) 

print(to_del)

# delete some keys 

# Create a list of keys to iterate over
for key in keys:
    if key in to_del:
        del data[key]
        print("deleting", key)

# Remove the specified key
keys = list(data.keys())  # Update the list of keys after deletion
for key in keys:
    subkeys = list(data[key].keys())
    for subkey in subkeys:
        if subkey.endswith("def2qzvpd.fchk") or subkey.endswith("def2svpd.fchk"):
            print("deleting", subkey)
            del data[key][subkey]

keys = list(data.keys())  # Update the list of keys after deletion
for key in keys:
    subkeys = list(data[key].keys())  # Convert to list to avoid modification during iteration
    for subkey in subkeys:
        if subkey.endswith(".fchk"):
            inside = data[key][subkey]['denspart']
            sub_subkeys = list(inside.keys())  # Convert to list to avoid modification during iteration
            for sub_subkey in sub_subkeys:
                if not sub_subkey.endswith("AVH") and not sub_subkey.endswith("MBIS"):
                    print("deleting", sub_subkey)
                    del inside[sub_subkey]

# Save the modified JSON data to a new file
with open('output.json', 'w') as file:
     json.dump(data, file, indent=4)

print("The specified key has been removed and the modified JSON has been saved to 'output.json'.")
