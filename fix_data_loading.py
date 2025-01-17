import numpy as np
import os

def fix_numpy_loading():
    # Set numpy to allow pickle loading
    np.load = lambda *a,**k: np.load(*a, allow_pickle=True, **k)

# Add this to your custom trainer
class MultiTaskTrainer(nnUNetTrainer):
    def __init__(self, plans, configuration, fold):
        super().__init__(plans, configuration, fold)
        # Force CPU usage and fix numpy loading
        self.device = torch.device('cpu')
        fix_numpy_loading()
        
        self.network = MultiTaskUNet(
            input_channels=self.network.input_channels,
            n_stages=self.network.n_stages,
            features_per_stage=self.network.features_per_stage,
            conv_op=self.network.conv_op,
            kernel_sizes=self.network.kernel_sizes,
            strides=self.network.strides,
            num_classes=self.network.num_classes
        ).to(self.device) 