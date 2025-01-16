import json
import os

# Update path to match your structure
dataset_path = os.path.join("nnUNet_raw", "Dataset001_PancreasCancerSeg", "dataset.json")

with open(dataset_path, 'r') as f:
    dataset = json.load(f)

print("Raw labels content:", dataset["labels"])
print("Background label value:", dataset["labels"].get("0"))

# Verify folder structure
expected_folders = [
    os.path.join("nnUNet_raw", "Dataset001_PancreasCancerSeg", "imagesTr"),
    os.path.join("nnUNet_raw", "Dataset001_PancreasCancerSeg", "labelsTr"),
    os.path.join("nnUNet_raw", "Dataset001_PancreasCancerSeg", "imagesTs")
]

for folder in expected_folders:
    if not os.path.exists(folder):
        print(f"Missing folder: {folder}")
    else:
        print(f"Found folder: {folder}")
