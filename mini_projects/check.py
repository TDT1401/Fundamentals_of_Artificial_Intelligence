import torch

print("=== PyTorch Check ===")

# 1. Version
print(f"PyTorch version: {torch.__version__}")

# 2. CUDA availability
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

# 3. CUDA version (built with)
print(f"CUDA (torch built): {torch.version.cuda}")

# 4. Device info
if cuda_available:
    device = torch.device("cuda")
    print(f"Using device: GPU")
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
    print(f"GPU count: {torch.cuda.device_count()}")
else:
    device = torch.device("cpu")
    print(f"Using device: CPU")