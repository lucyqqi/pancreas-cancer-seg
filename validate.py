import json
import os

dataset_path = os.path.join("nnUNet_raw", "Dataset001_PancreasCancerSeg", "dataset.json")  # Path to the json file

with open(dataset_path, 'r') as f:
    dataset = json.load(f)

# Print labels to verify
print("Labels:", dataset.get("labels"))

# Check for background label
if "0" not in dataset["labels"] or dataset["labels"]["0"] != "background":
    raise ValueError("Background label not declared correctly!")
else:
    print("Labels are correctly defined.")
