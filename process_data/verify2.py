import json
import os

# Define the dataset information
dataset = {
    "channel_names": {
        "0": "CT"
    },
    "labels": {
        "background": 0,
        "pancreas": 1,
        "lesion": 2
    },
    "numTraining": 288,
    "numTest": 72,
    "file_ending": ".nii.gz",
    "regions_class_order": ["background", "pancreas", "lesion"]
}

# Add training data
training_data = []
labelsTr_path = "nnUNet_raw/Dataset001_PancreasCancerSeg/labelsTr"
for label_file in sorted(os.listdir(labelsTr_path)):
    if label_file.endswith('.nii.gz'):
        case_id = label_file.replace('.nii.gz', '')
        training_data.append({
            "image": f"./imagesTr/{case_id}_0000.nii.gz",
            "label": f"./labelsTr/{label_file}"
        })

dataset["training"] = training_data

# Add test data
test_data = []
imagesTs_path = "nnUNet_raw/Dataset001_PancreasCancerSeg/imagesTs"
if os.path.exists(imagesTs_path):
    for image_file in sorted(os.listdir(imagesTs_path)):
        if image_file.endswith('_0000.nii.gz'):
            test_data.append(f"./imagesTs/{image_file}")

dataset["test"] = test_data
dataset["validation"] = []

# Write the new dataset.json
output_path = "nnUNet_raw/Dataset001_PancreasCancerSeg/dataset.json"
with open(output_path, 'w') as f:
    json.dump(dataset, f, indent=2)

print(f"Created new dataset.json at {output_path}")