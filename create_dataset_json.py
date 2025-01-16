import os
import json
from pathlib import Path

def create_dataset_json(base_path):
    # Define paths
    images_tr_path = os.path.join(base_path, "imagesTr")
    labels_tr_path = os.path.join(base_path, "labelsTr")
    images_ts_path = os.path.join(base_path, "imagesTs")
    
    # Verify paths exist
    for path in [images_tr_path, labels_tr_path, images_ts_path]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Directory not found: {path}")
    
    # Get all training files
    training_files = []
    for img_file in sorted(os.listdir(images_tr_path)):
        if img_file.endswith("_0000.nii.gz"):  # Only get the first timepoint
            base_name = img_file.replace("_0000.nii.gz", "")
            label_file = f"{base_name}.nii.gz"
            
            if os.path.exists(os.path.join(labels_tr_path, label_file)):
                training_files.append({
                    "image": f"./imagesTr/{img_file}",
                    "label": f"./labelsTr/{label_file}"
                })
            else:
                print(f"Warning: Label file missing for {img_file}")
    
    # Get all test files
    test_files = []
    for img_file in sorted(os.listdir(images_ts_path)):
        if img_file.endswith(".nii.gz"):
            test_files.append(f"./imagesTs/{img_file}")
        else:
            print(f"Warning: Ignoring non-NIFTI file in test set: {img_file}")
    
    # Create dataset dictionary
    dataset = {
        "labels": {
            "0": "background",
            "1": "pancreas",
            "2": "lesion"
        },
        "channel_names": {
            "0": "CT"
        },
        "numTraining": len(training_files),
        "numTest": len(test_files),
        "file_ending": ".nii.gz",
        "regions_class_order": [],
        "training": training_files,
        "validation": [],
        "test": test_files
    }
    
    # Save to JSON file
    output_file = os.path.join(base_path, "dataset.json")
    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=2)
    
    print(f"Created dataset.json with {len(training_files)} training files and {len(test_files)} test files")
    print(f"Output file saved to: {output_file}")

# Usage
if __name__ == "__main__":
    base_path = "nnUNet_raw/Dataset001_PancreasCancerSeg"  # Adjust this if needed
    create_dataset_json(base_path)
