#!/bin/sh

export BASE_IMAGE=nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

export PYTHON_VERSION=3.7.13

export PYTORCH_VERSION=1.2.0
export PYTORCH_VERSION_SUFFIX=
export TORCHVISION_VERSION=0.5.0
export TORCHVISION_VERSION_SUFFIX=
export TORCHAUDIO_VERSION=
export TORCHAUDIO_VERSION_SUFFIX=
export PYTORCH_DOWNLOAD_URL=

export IMAGE_TAG=1.2.0-py3.7.13-cuda10.0-devel-ubuntu18.04

./docker/ubuntu/build.sh
