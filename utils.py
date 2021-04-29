import os 

def get_last_checkpoint(output_dir):
    if os.path.exists(os.path.join(output_dir, 'pytorch_model.bin')):
        return output_dir
    return None

