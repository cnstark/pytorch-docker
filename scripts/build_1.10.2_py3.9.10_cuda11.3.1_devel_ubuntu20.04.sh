#!/bin/sh

export UBUNTU_VERSION=20.04
export CUDA_VERSION=11.3.1
export CUDNN_VERSION=8
export CUDA_FLAVOR=devel

export PYTHON_VERSION=3.9.10

export PYTORCH_VERSION=1.10.2
export PYTORCH_VERSION_SUFFIX=+cu113
export TORCHVISION_VERSION=0.11.3
export TORCHVISION_VERSION_SUFFIX=+cu113
export TORCHAUDIO_VERSION=0.10.2
export TORCHAUDIO_VERSION_SUFFIX=+cu113
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/cu113/torch_stable.html

./docker/ubuntu-cuda/build.sh
