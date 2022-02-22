#!/bin/sh

export UBUNTU_VERSION=20.04

export PYTHON_VERSION=3.9.10

export PYTORCH_VERSION=1.10.2
export PYTORCH_VERSION_SUFFIX=+cpu
export TORCHVISION_VERSION=0.11.3
export TORCHVISION_VERSION_SUFFIX=+cpu
export TORCHAUDIO_VERSION=0.10.2
export TORCHAUDIO_VERSION_SUFFIX=+cpu
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/cpu/torch_stable.html

./docker/ubuntu/build.sh
