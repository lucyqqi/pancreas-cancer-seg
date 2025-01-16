import os
import json
import shutil
from pathlib import Path

def fix_dataset():
    # Load the dataset.json
    with open("nnUNet_raw/Dataset001_PancreasCancerSeg/dataset.json", 'r') as f:
        dataset = json.load(f)

    # Create necessary directories if they don't exist
    base_path = Path("nnUNet_raw/Dataset001_PancreasCancerSeg")
    (base_path / "imagesTr").mkdir(exist_ok=True)
    (base_path / "labelsTr").mkdir(exist_ok=True)
    (base_path / "imagesTs").mkdir(exist_ok=True)

    # Move training files from your current structure to nnUNet structure
    data_path = Path("data")  # Your current data path
    
    # Process training data
    for subtype in ["subtype0", "subtype1", "subtype2"]:
        train_path = data_path / "train" / subtype
        if train_path.exists():
            # Move image files
            for img_file in train_path.glob("*_0000.nii.gz"):
                shutil.copy2(img_file, base_path / "imagesTr" / img_file.name)
            # Move label files
            for label_file in train_path.glob("*[!0000].nii.gz"):  # Files without _0000
                shutil.copy2(label_file, base_path / "labelsTr" / label_file.name)

    # Process test data
    test_path = data_path / "test"
    if test_path.exists():
        for img_file in test_path.glob("*.nii.gz"):
            shutil.copy2(img_file, base_path / "imagesTs" / img_file.name)

    print("Files have been reorganized according to nnUNet structure")

if __name__ == "__main__":
    fix_dataset()