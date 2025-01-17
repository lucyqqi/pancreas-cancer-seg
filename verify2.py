import json

# Read and verify the JSON file
with open('nnUNet_raw/Dataset001_PancreasCancerSeg/dataset.json', 'r') as f:
    data = json.load(f)

# Print the exact structure and type of the labels
print("Labels section:")
print(json.dumps(data['labels'], indent=2))
print("\nTypes:")
print(f"Type of labels dict: {type(data['labels'])}")
print(f"Type of '0' key: {type(next(iter(data['labels'].keys())))}")
print(f"Type of '0' value: {type(data['labels']['0'])}")

# Verify all keys are strings and values are strings
print("\nVerifying all entries:")
for k, v in data['labels'].items():
    print(f"Key: {k} ({type(k)}), Value: {v} ({type(v)})")
