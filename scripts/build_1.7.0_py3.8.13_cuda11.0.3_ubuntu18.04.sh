#!/bin/sh

export BASE_IMAGE=ubuntu:18.04

export PYTHON_VERSION=3.8.13

export PYTORCH_VERSION=1.7.0
export PYTORCH_VERSION_SUFFIX=+cu110
export TORCHVISION_VERSION=0.8.1
export TORCHVISION_VERSION_SUFFIX=+cu110
export TORCHAUDIO_VERSION=0.7.0
export TORCHAUDIO_VERSION_SUFFIX=
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/torch_stable.html

export IMAGE_TAG=1.7.0-py3.8.13-cuda11.0.3-ubuntu18.04

./docker/ubuntu/build.sh
