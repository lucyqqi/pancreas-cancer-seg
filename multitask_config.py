from nnunetv2.training.nnUNetTrainer.nnUNetTrainer import nnUNetTrainer

class MultiTaskConfiguration:
    def __init__(self):
        self.trainer_class = MultiTaskTrainer
        self.plans_name = "nnUNetPlans"
        self.network_name = "MultiTaskUNet"
        
        # Training configuration
        self.batch_size = 4
        self.patch_size = [256, 256]  # For 2D
        self.num_epochs = 1000
        self.initial_lr = 1e-2
        
        # Loss weights
        self.seg_weight = 0.7
        self.class_weight = 0.3 