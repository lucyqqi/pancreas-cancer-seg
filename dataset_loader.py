from nnunetv2.training.dataloading.base_data_loader import nnUNetDataLoaderBase
import numpy as np

class MultiTaskDataLoader(nnUNetDataLoaderBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Extract subtype from file path (0, 1, or 2)
        self.subtypes = []
        for case in self.dataset:
            # Extract subtype from the path structure (subtype0, subtype1, subtype2)
            path = case['image']
            subtype = int(path.split('subtype')[1][0])
            self.subtypes.append(subtype)

    def generate_train_batch(self):
        # Get regular batch with image and segmentation
        batch = super().generate_train_batch()
        
        # Add subtype labels
        selected_indices = batch['indices']
        subtypes = [self.subtypes[i] for i in selected_indices]
        batch['subtype'] = torch.tensor(subtypes, dtype=torch.long)
        
        return batch 