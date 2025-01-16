import json

# Load and print the exact content
with open("nnUNet_raw/Dataset001_PancreasCancerSeg/dataset.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
    
print("Type of labels dict:", type(data["labels"]))
print("Type of label '0' key:", type(list(data["labels"].keys())[0]))
print("Raw labels:", data["labels"])
print("Background label value:", repr(data["labels"].get("0")))  # repr shows hidden characters