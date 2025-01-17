from nnunetv2.training.nnUNetTrainer.nnUNetTrainer import nnUNetTrainer
import torch

class MultiTaskTrainer(nnUNetTrainer):
    def __init__(self, plans, configuration, fold):
        super().__init__(plans, configuration, fold)
        # Force CPU usage
        self.device = torch.device('cpu')
        print(f"Using device: {self.device}")
        
        self.network = MultiTaskUNet(
            input_channels=self.network.input_channels,
            n_stages=self.network.n_stages,
            features_per_stage=self.network.features_per_stage,
            conv_op=self.network.conv_op,
            kernel_sizes=self.network.kernel_sizes,
            strides=self.network.strides,
            num_classes=self.network.num_classes
        ).to(self.device)
    
    def train_step(self, batch):
        data, target = batch
        seg_output, class_output = self.network(data)
        
        # Calculate segmentation loss
        seg_loss = self.loss(seg_output, target)
        
        # Calculate classification loss (you'll need to add class labels to your dataset)
        class_loss = nn.CrossEntropyLoss()(class_output, class_labels)
        
        # Combined loss
        total_loss = seg_loss + class_loss
        
        return total_loss 