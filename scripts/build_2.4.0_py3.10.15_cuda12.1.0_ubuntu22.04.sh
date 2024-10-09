#!/bin/sh

export BASE_IMAGE=ubuntu:22.04

export PYTHON_VERSION=3.10.15

export PYTORCH_VERSION=2.4.0
export PYTORCH_VERSION_SUFFIX=+cu121
export TORCHVISION_VERSION=0.19.0
export TORCHVISION_VERSION_SUFFIX=+cu121
export TORCHAUDIO_VERSION=2.4.0
export TORCHAUDIO_VERSION_SUFFIX=+cu121
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/cu121/torch_stable.html

export IMAGE_TAG=2.4.0-py3.10.15-cuda12.1.0-ubuntu22.04

./docker/ubuntu/build.sh
