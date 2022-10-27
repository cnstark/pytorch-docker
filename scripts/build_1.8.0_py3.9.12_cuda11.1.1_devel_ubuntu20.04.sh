#!/bin/sh

export BASE_IMAGE=nvidia/cuda:11.1.1-cudnn8-devel-ubuntu20.04

export PYTHON_VERSION=3.9.12

export PYTORCH_VERSION=1.8.0
export PYTORCH_VERSION_SUFFIX=+cu111
export TORCHVISION_VERSION=0.9.0
export TORCHVISION_VERSION_SUFFIX=+cu111
export TORCHAUDIO_VERSION=0.8.0
export TORCHAUDIO_VERSION_SUFFIX=
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/torch_stable.html

export IMAGE_TAG=1.8.0-py3.9.12-cuda11.1.1-devel-ubuntu20.04

./docker/ubuntu/build.sh
