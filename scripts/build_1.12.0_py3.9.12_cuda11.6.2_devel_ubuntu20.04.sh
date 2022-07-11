#!/bin/sh

export BASE_IMAGE=nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04

export PYTHON_VERSION=3.9.12

export PYTORCH_VERSION=1.12.0
export PYTORCH_VERSION_SUFFIX=+cu116
export TORCHVISION_VERSION=0.13.0
export TORCHVISION_VERSION_SUFFIX=+cu116
export TORCHAUDIO_VERSION=0.12.0
export TORCHAUDIO_VERSION_SUFFIX=+cu116
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/cu116/torch_stable.html

export IMAGE_TAG=1.12.0-py3.9.12-cuda11.6.2-devel-ubuntu20.04

./docker/ubuntu/build.sh
