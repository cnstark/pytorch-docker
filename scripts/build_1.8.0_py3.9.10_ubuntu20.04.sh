#!/bin/sh

export UBUNTU_VERSION=20.04

export PYTHON_VERSION=3.9.10

export PYTORCH_VERSION=1.8.0
export PYTORCH_VERSION_SUFFIX=+cpu
export TORCHVISION_VERSION=0.9.0
export TORCHVISION_VERSION_SUFFIX=+cpu
export TORCHAUDIO_VERSION=0.8.0
export TORCHAUDIO_VERSION_SUFFIX=
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/torch_stable.html

./docker/ubuntu/build.sh
