#!/bin/sh

export UBUNTU_VERSION=18.04
export CUDA_VERSION=11.0
export CUDNN_VERSION=8
export CUDA_FLAVOR=runtime

export PYTHON_VERSION=3.9.10

export PYTORCH_VERSION=1.7.1
export PYTORCH_VERSION_SUFFIX=+cu110
export TORCHVISION_VERSION=0.8.2
export TORCHVISION_VERSION_SUFFIX=+cu110
export TORCHAUDIO_VERSION=0.7.2
export TORCHAUDIO_VERSION_SUFFIX=
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/torch_stable.html

./docker/ubuntu-cuda/build.sh
