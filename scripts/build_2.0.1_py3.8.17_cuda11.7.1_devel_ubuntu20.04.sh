#!/bin/sh

export BASE_IMAGE=nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04

export PYTHON_VERSION=3.8.17

export PYTORCH_VERSION=2.0.1
export PYTORCH_VERSION_SUFFIX=+cu117
export TORCHVISION_VERSION=0.15.2
export TORCHVISION_VERSION_SUFFIX=+cu117
export TORCHAUDIO_VERSION=2.0.2
export TORCHAUDIO_VERSION_SUFFIX=+cu117
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/cu117/torch_stable.html

export IMAGE_TAG=2.0.1-py3.8.17-cuda11.7.1-devel-ubuntu20.04

./docker/ubuntu/build.sh
