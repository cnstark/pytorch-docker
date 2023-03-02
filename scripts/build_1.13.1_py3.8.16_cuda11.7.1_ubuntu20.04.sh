#!/bin/sh

export BASE_IMAGE=ubuntu:20.04

export PYTHON_VERSION=3.8.16

export PYTORCH_VERSION=1.13.1
export PYTORCH_VERSION_SUFFIX=+cu117
export TORCHVISION_VERSION=0.14.1
export TORCHVISION_VERSION_SUFFIX=+cu117
export TORCHAUDIO_VERSION=0.13.1
export TORCHAUDIO_VERSION_SUFFIX=+cu117
export PYTORCH_DOWNLOAD_URL=https://download.pytorch.org/whl/cu117/torch_stable.html

export IMAGE_TAG=1.13.1-py3.8.16-cuda11.7.1-ubuntu20.04

./docker/ubuntu/build.sh
