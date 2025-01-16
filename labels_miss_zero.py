import os
import nibabel as nib
import numpy as np

labels_dir = "./nnUNet_raw/Dataset001_PancreasCancerSeg/labelsTr"

for label_file in os.listdir(labels_dir):
    if label_file.endswith(".nii.gz"):
        label_path = os.path.join(labels_dir, label_file)
        label_data = nib.load(label_path).get_fdata()
        unique_labels = np.unique(label_data)
        if 0 not in unique_labels:
            print(f"Error: {label_file} does not contain label 0 (background).")
