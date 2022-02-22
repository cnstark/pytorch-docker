#!/bin/sh

export CENTOS_VERSION=8

export PYTHON_VERSION=3.9.7

export PYTORCH_VERSION=1.9.1
export PYTORCH_VERSION_SUFFIX=+cpu
export TORCHVISION_VERSION=0.10.1
export TORCHVISION_VERSION_SUFFIX=+cpu
export TORCHAUDIO_VERSION=0.9.1
export TORCHAUDIO_VERSION_SUFFIX=
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/torch_stable.html

./docker/centos/build.sh
