import os
import json
from pathlib import Path

def create_dataset_json(base_path):
    dataset = {
        "labels": {
            "0": "background",
            "1": "pancreas",
            "2": "lesion"
        },
        "channel_names": {
            "0": "CT"
        },
        "numTraining": 252,
        "numTest": 3,
        "file_ending": ".nii.gz",
        "training": [],
        "validation": [],
        "test": []
    }
    
    # Add training cases
    for subtype in range(3):
        train_path = Path(base_path) / f"train/subtype{subtype}"
        for img_file in sorted(train_path.glob("*_0000.nii.gz")):
            label_file = str(img_file).replace("_0000.nii.gz", ".nii.gz")
            dataset["training"].append({
                "image": f"./train/subtype{subtype}/{img_file.name}",
                "label": f"./train/subtype{subtype}/{Path(label_file).name}"
            })
    
    # Add validation cases
    for subtype in range(3):
        val_path = Path(base_path) / f"validation/subtype{subtype}"
        for img_file in sorted(val_path.glob("*_0000.nii.gz")):
            label_file = str(img_file).replace("_0000.nii.gz", ".nii.gz")
            dataset["validation"].append({
                "image": f"./validation/subtype{subtype}/{img_file.name}",
                "label": f"./validation/subtype{subtype}/{Path(label_file).name}"
            })
    
    # Add test cases
    test_path = Path(base_path) / "test"
    dataset["test"] = [f"./test/{f.name}" for f in sorted(test_path.glob("*_0000.nii.gz"))]
    
    # Write the JSON file
    with open(Path(base_path) / "dataset.json", "w") as f:
        json.dump(dataset, f, indent=2)

# Use it like this:
if __name__ == "__main__":
    base_path = "nnUNet_raw/Dataset001_PancreasCancerSeg"
    create_dataset_json(base_path)