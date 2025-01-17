import nibabel as nib
import os
import numpy as np

def fix_labels(input_path):
    # Load the image
    img = nib.load(input_path)
    data = img.get_fdata()
    
    # Round the values to nearest integer
    data = np.round(data).astype(np.uint8)
    
    # Create new nifti image with same header but integer data
    new_img = nib.Nifti1Image(data, img.affine, img.header)
    
    # Save the fixed image
    nib.save(new_img, input_path)
    print(f"Fixed {input_path}")

# Process all label files
labelsTr_path = "nnUNet_raw/Dataset001_PancreasCancerSeg/labelsTr"
for label_file in os.listdir(labelsTr_path):
    if label_file.endswith('.nii.gz'):
        file_path = os.path.join(labelsTr_path, label_file)
        fix_labels(file_path)

print("All label files have been fixed!") 