import os

# Path to your dataset directory
base_dir = 'nnUNet_raw/Dataset001_PancreasCancerSeg'

images_dir = os.path.join(base_dir, 'imagesTr')
labels_dir = os.path.join(base_dir, 'labelsTr')

image_files = {f for f in os.listdir(images_dir) if f.endswith('.nii.gz')}
label_files = {f for f in os.listdir(labels_dir) if f.endswith('.nii.gz')}

print("Missing label files:", [f for f in image_files if f.replace('_0000', '') not in label_files])
print("Missing image files:", [f for f in label_files if f + '_0000' not in image_files])
