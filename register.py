import os

def register_custom_components():
    # Set environment variables for custom components
    os.environ['nnUNet_trainer'] = 'MultiTaskTrainer'
    os.environ['nnUNet_network'] = 'MultiTaskUNet'
    os.environ['nnUNet_preprocessor'] = 'DefaultPreprocessor'  # Using default preprocessor
    
    print("Custom components registered successfully!")

if __name__ == "__main__":
    register_custom_components() 