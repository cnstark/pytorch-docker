#!/bin/sh

export BASE_IMAGE=nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04

export PYTHON_VERSION=3.9.12

export PYTORCH_VERSION=2.0.0
export PYTORCH_VERSION_SUFFIX=+cu117
export TORCHVISION_VERSION=0.15.0
export TORCHVISION_VERSION_SUFFIX=+cu117
export TORCHAUDIO_VERSION=2.0.0
export TORCHAUDIO_VERSION_SUFFIX=+cu117
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/cu117/torch_stable.html

export IMAGE_TAG=2.0.0-py3.9.12-cuda11.7.1-devel-ubuntu20.04

./docker/ubuntu/build.sh
