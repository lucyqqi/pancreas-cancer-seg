import torch.nn as nn
from nnunetv2.training.network.model.dim2.generic_UNet2D import PlainConvUNet2D

class MultiTaskUNet(PlainConvUNet2D):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Get number of channels from encoder's last layer
        encoder_channels = self.encoder.all_modules[-1].output_channels
        
        # Add classification head
        self.classification_head = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),  # Global average pooling
            nn.Flatten(),
            nn.Linear(encoder_channels, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 3)  # 3 subtypes (0,1,2)
        )

    def forward(self, x):
        # Get encoder features
        encoder_features = self.encoder(x)
        
        # Get segmentation output
        seg_output = self.decoder(encoder_features)
        
        # Get classification output using the deepest encoder features
        class_output = self.classification_head(encoder_features[-1])
        
        return seg_output, class_output 