docker build \
    --build-arg UBUNTU_VERSION=${UBUNTU_VERSION} \
    --build-arg CUDA_VERSION=${CUDA_VERSION} \
    --build-arg CUDNN_VERSION=${CUDNN_VERSION} \
    --build-arg PYTHON_VERSION=${PYTHON_VERSION} \
    --build-arg PYTORCH_VERSION=${PYTORCH_VERSION} \
    --build-arg PYTORCH_CUDA_VERSION=${PYTORCH_CUDA_VERSION} \
    --build-arg TORCHVISION_VERSION=${TORCHVISION_VERSION} \
    --build-arg TORCHAUDIO_VERSION=${TORCHAUDIO_VERSION} \
    -t yuhaow/pytorch:${PYTORCH_VERSION}-py${PYTHON_VERSION}-cuda${CUDA_VERSION}-ubuntu${UBUNTU_VERSION} \
    -f docker/ubuntu-cuda/Dockerfile \
    .
