#!/bin/sh

export BASE_IMAGE=nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04

export PYTHON_VERSION=3.8.13

export PYTORCH_VERSION=1.10.2
export PYTORCH_VERSION_SUFFIX=+cu113
export TORCHVISION_VERSION=0.11.3
export TORCHVISION_VERSION_SUFFIX=+cu113
export TORCHAUDIO_VERSION=0.10.2
export TORCHAUDIO_VERSION_SUFFIX=+cu113
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/cu113/torch_stable.html

export IMAGE_TAG=1.10.2-py3.8.13-cuda11.3.1-devel-ubuntu20.04

./docker/ubuntu/build.sh
