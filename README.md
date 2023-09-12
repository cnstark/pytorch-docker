# Pytorch Docker Images

[DockerHub]: https://hub.docker.com/r/cnstark/pytorch

[![LICENSE](https://img.shields.io/github/license/cnstark/pytorch_docker.svg)](https://github.com/cnstark/pytorch_docker/blob/master/LICENSE)
[![Docker Stars](https://img.shields.io/docker/stars/cnstark/pytorch?logo=docker)][DockerHub]
[![Docker Pulls](https://img.shields.io/docker/pulls/cnstark/pytorch?logo=docker)][DockerHub]

Pure pytorch docker images with different os, cuda, and python versions.

Github: https://github.com/cnstark/pytorch-docker

Docker Hub: https://hub.docker.com/r/cnstark/pytorch

## Changelog

* 2023/07/10: Support for pytorch 2.0.1.
* 2023/05/04: Support for pytorch 2.0.

## Usage

### Preparation

* [Docker](https://docs.docker.com/engine/install/)
* [Nvidia-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html) (If a CUDA is required)

### Use pytorch docker

As same as [Pytorch Official](https://github.com/pytorch/pytorch#docker-image).

```shell
docker run -it --rm \
    --gpus all \
    --net host 
    -v /path/to/project:/path/to/project \
    -v /path/to/dataset:/path/to/dataset \
    cnstark/pytorch:[TAG]
```

Note: `/path/to/project` and `/path/to/dataset` is your **own** project path and dataset path, should be replaced in use.

## Image List (More images are on the way ~)

<!-- Pytorch versions -->
[pytorch2.0.1]: https://img.shields.io/badge/Pytorch-2.0.1-orange?logo=pytorch
[pytorch2.0.0]: https://img.shields.io/badge/Pytorch-2.0.0-orange?logo=pytorch
[pytorch1.13.1]: https://img.shields.io/badge/Pytorch-1.13.1-orange?logo=pytorch
[pytorch1.13.0]: https://img.shields.io/badge/Pytorch-1.13.0-orange?logo=pytorch
[pytorch1.12.1]: https://img.shields.io/badge/Pytorch-1.12.1-orange?logo=pytorch
[pytorch1.12.0]: https://img.shields.io/badge/Pytorch-1.12.0-orange?logo=pytorch
[pytorch1.11.0]: https://img.shields.io/badge/Pytorch-1.11.0-orange?logo=pytorch
[pytorch1.10.2]: https://img.shields.io/badge/Pytorch-1.10.2-orange?logo=pytorch
[pytorch1.10.1]: https://img.shields.io/badge/Pytorch-1.10.1-orange?logo=pytorch
[pytorch1.10.0]: https://img.shields.io/badge/Pytorch-1.10.0-orange?logo=pytorch
[pytorch1.9.1]: https://img.shields.io/badge/Pytorch-1.9.1-orange?logo=pytorch
[pytorch1.9.0]: https://img.shields.io/badge/Pytorch-1.9.0-orange?logo=pytorch
[pytorch1.8.1]: https://img.shields.io/badge/Pytorch-1.8.1-orange?logo=pytorch
[pytorch1.8.0]: https://img.shields.io/badge/Pytorch-1.8.0-orange?logo=pytorch
[pytorch1.7.1]: https://img.shields.io/badge/Pytorch-1.7.1-orange?logo=pytorch
[pytorch1.7.0]: https://img.shields.io/badge/Pytorch-1.7.0-orange?logo=pytorch
[pytorch1.6.0]: https://img.shields.io/badge/Pytorch-1.6.0-orange?logo=pytorch
[pytorch1.5.1]: https://img.shields.io/badge/Pytorch-1.5.1-orange?logo=pytorch
[pytorch1.5.0]: https://img.shields.io/badge/Pytorch-1.5.0-orange?logo=pytorch
[pytorch1.4.0]: https://img.shields.io/badge/Pytorch-1.4.0-orange?logo=pytorch
[pytorch1.2.0]: https://img.shields.io/badge/Pytorch-1.2.0-orange?logo=pytorch

<!-- Python versions -->
[python3.10.11]: https://img.shields.io/badge/Python-3.10.11-blue?logo=python
[python3.9.17]: https://img.shields.io/badge/Python-3.9.17-blue?logo=python
[python3.9.16]: https://img.shields.io/badge/Python-3.9.16-blue?logo=python
[python3.9.12]: https://img.shields.io/badge/Python-3.9.12-blue?logo=python
[python3.8.13]: https://img.shields.io/badge/Python-3.8.13-blue?logo=python
[python3.8.16]: https://img.shields.io/badge/Python-3.8.16-blue?logo=python
[python3.7.13]: https://img.shields.io/badge/Python-3.7.13-blue?logo=python

<!-- OS versions -->
[ubuntu22.04]: https://img.shields.io/badge/Ubuntu-22.04-orange?logo=ubuntu
[ubuntu20.04]: https://img.shields.io/badge/Ubuntu-20.04-orange?logo=ubuntu
[ubuntu18.04]: https://img.shields.io/badge/Ubuntu-18.04-orange?logo=ubuntu
[centOS8]: https://img.shields.io/badge/CentOS-8-blue?logo=centos

<!-- CUDA versions -->
[cuda11.8]: https://img.shields.io/badge/CUDA-11.8-green?logo=nvidia
[cuda11.8-devel]: https://img.shields.io/badge/CUDA-11.8--devel-green?logo=nvidia
[cuda11.7]: https://img.shields.io/badge/CUDA-11.7-green?logo=nvidia
[cuda11.7-devel]: https://img.shields.io/badge/CUDA-11.7--devel-green?logo=nvidia
[cuda11.6]: https://img.shields.io/badge/CUDA-11.6-green?logo=nvidia
[cuda11.6-devel]: https://img.shields.io/badge/CUDA-11.6--devel-green?logo=nvidia
[cuda11.3]: https://img.shields.io/badge/CUDA-11.3-green?logo=nvidia
[cuda11.3-devel]: https://img.shields.io/badge/CUDA-11.3--devel-green?logo=nvidia
[cuda11.1]: https://img.shields.io/badge/CUDA-11.1-green?logo=nvidia
[cuda11.1-devel]: https://img.shields.io/badge/CUDA-11.1--devel-green?logo=nvidia
[cuda11.0]: https://img.shields.io/badge/CUDA-11.0-green?logo=nvidia
[cuda11.0-devel]: https://img.shields.io/badge/CUDA-11.0--devel-green?logo=nvidia
[cuda10.2]: https://img.shields.io/badge/CUDA-10.2-green?logo=nvidia
[cuda10.2-devel]: https://img.shields.io/badge/CUDA-10.2--devel-green?logo=nvidia
[cuda10.1]: https://img.shields.io/badge/CUDA-10.1-green?logo=nvidia
[cuda10.1-devel]: https://img.shields.io/badge/CUDA-10.1--devel-green?logo=nvidia
[cuda10.0]: https://img.shields.io/badge/CUDA-10.0-green?logo=nvidia
[cuda10.0-devel]: https://img.shields.io/badge/CUDA-10.0--devel-green?logo=nvidia
[cpu]: https://img.shields.io/badge/CPU-amd64-lightgray

<!-- order: cuda, python, os -->

### 2.0.1

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch2.0.1] ![python3.10.11] ![cuda11.8] ![ubuntu22.04] [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.1-py3.10.11-cuda11.8.0-ubuntu22.04)][DockerHub] | `docker pull cnstark/pytorch:2.0.1-py3.10.11-cuda11.8.0-ubuntu22.04` |
| ![pytorch2.0.1] ![python3.9.17] ![cuda11.8] ![ubuntu20.04] [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.1-py3.9.17-cuda11.8.0-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:2.0.1-py3.9.17-cuda11.8.0-ubuntu20.04` |
| ![pytorch2.0.1] ![python3.9.17] ![cuda11.8-devel] ![ubuntu20.04] [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.1-py3.9.17-cuda11.8.0-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:2.0.1-py3.9.17-cuda11.8.0-devel-ubuntu20.04` |
| ![pytorch2.0.1] ![python3.10.11] ![cpu] ![ubuntu22.04] [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.1-py3.10.11-ubuntu22.04)][DockerHub] | `docker pull cnstark/pytorch:2.0.1-py3.10.11-ubuntu22.04` |
| ![pytorch2.0.1] ![python3.9.17] ![cpu] ![ubuntu20.04] [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.1-py3.9.17-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:2.0.1-py3.9.17-ubuntu20.04` |

### 2.0.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch2.0.0]   ![python3.9.12]   ![cuda11.8]         ![ubuntu22.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.0-py3.9.12-cuda11.8.0-ubuntu22.04)][DockerHub]        | `docker pull cnstark/pytorch:2.0.0-py3.9.12-cuda11.8.0-ubuntu22.04` |
| ![pytorch2.0.0]   ![python3.9.12]   ![cuda11.8]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.0-py3.9.12-cuda11.8.0-ubuntu20.04)][DockerHub]        | `docker pull cnstark/pytorch:2.0.0-py3.9.12-cuda11.8.0-ubuntu20.04` |
| ![pytorch2.0.0]   ![python3.9.12]   ![cuda11.8-devel]   ![ubuntu22.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.0-py3.9.12-cuda11.8.0-devel-ubuntu22.04)][DockerHub]  | `docker pull cnstark/pytorch:2.0.0-py3.9.12-cuda11.8.0-devel-ubuntu22.04` |
| ![pytorch2.0.0]   ![python3.9.12]   ![cuda11.8-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.0-py3.9.12-cuda11.8.0-devel-ubuntu20.04)][DockerHub]  | `docker pull cnstark/pytorch:2.0.0-py3.9.12-cuda11.8.0-devel-ubuntu20.04` |
| ![pytorch2.0.0]   ![python3.9.12]   ![cuda11.7]         ![ubuntu22.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.0-py3.9.12-cuda11.7.1-ubuntu22.04)][DockerHub]        | `docker pull cnstark/pytorch:2.0.0-py3.9.12-cuda11.7.1-ubuntu22.04` |
| ![pytorch2.0.0]   ![python3.9.12]   ![cuda11.7-devel]   ![ubuntu22.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.0-py3.9.12-cuda11.7.1-devel-ubuntu22.04)][DockerHub]  | `docker pull cnstark/pytorch:2.0.0-py3.9.12-cuda11.7.1-devel-ubuntu22.04` |
| ![pytorch2.0.0]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/2.0.0-py3.9.12-ubuntu20.04)][DockerHub]                   | `docker pull cnstark/pytorch:2.0.0-py3.9.12-ubuntu20.04` |

### 1.13.1

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.13.1]  ![python3.9.16]   ![cuda11.7]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.1-py3.9.16-cuda11.7.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.13.1-py3.9.16-cuda11.7.1-ubuntu20.04` |
| ![pytorch1.13.1]  ![python3.9.12]   ![cuda11.7]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.1-py3.9.12-cuda11.7.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.13.1-py3.9.12-cuda11.7.1-ubuntu20.04` |
| ![pytorch1.13.1]  ![python3.8.16]   ![cuda11.7]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.1-py3.8.16-cuda11.7.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.13.1-py3.8.16-cuda11.7.1-ubuntu20.04` |
| ![pytorch1.13.1]  ![python3.9.16]   ![cuda11.7-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.1-py3.9.16-cuda11.7.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.13.1-py3.9.16-cuda11.7.1-devel-ubuntu20.04` |
| ![pytorch1.13.1]  ![python3.9.12]   ![cuda11.7-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.1-py3.9.12-cuda11.7.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.13.1-py3.9.12-cuda11.7.1-devel-ubuntu20.04` |
| ![pytorch1.13.1]  ![python3.8.16]   ![cuda11.7-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.1-py3.8.16-cuda11.7.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.13.1-py3.8.16-cuda11.7.1-devel-ubuntu20.04` |
| ![pytorch1.13.1]  ![python3.9.16]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.1-py3.9.16-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.13.1-py3.9.16-ubuntu20.04` |
| ![pytorch1.13.1]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.1-py3.9.12-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.13.1-py3.9.12-ubuntu20.04` |

### 1.13.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.13.0]  ![python3.9.12]   ![cuda11.7]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.0-py3.9.12-cuda11.7.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.13.0-py3.9.12-cuda11.7.1-ubuntu20.04` |
| ![pytorch1.13.0]  ![python3.9.12]   ![cuda11.7-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.0-py3.9.12-cuda11.7.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.13.0-py3.9.12-cuda11.7.1-devel-ubuntu20.04` |
| ![pytorch1.13.0]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.13.0-py3.9.12-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.13.0-py3.9.12-ubuntu20.04` |

### 1.12.1

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.12.1]  ![python3.9.12]   ![cuda11.6]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.1-py3.9.12-cuda11.6.2-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.12.1-py3.9.12-cuda11.6.2-ubuntu20.04` |
| ![pytorch1.12.1]  ![python3.9.12]   ![cuda11.6-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.1-py3.9.12-cuda11.6.2-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.12.1-py3.9.12-cuda11.6.2-devel-ubuntu20.04` |
| ![pytorch1.12.1]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.1-py3.9.12-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.12.1-py3.9.12-ubuntu20.04` |

### 1.12.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.12.0]  ![python3.9.12]   ![cuda11.6]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.0-py3.9.12-cuda11.6.2-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.12.0-py3.9.12-cuda11.6.2-ubuntu20.04` |
| ![pytorch1.12.0]  ![python3.9.12]   ![cuda11.6-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.0-py3.9.12-cuda11.6.2-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.12.0-py3.9.12-cuda11.6.2-devel-ubuntu20.04` |
| ![pytorch1.12.0]  ![python3.9.12]   ![cuda11.3]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.0-py3.9.12-cuda11.3.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.12.0-py3.9.12-cuda11.3.1-ubuntu20.04` |
| ![pytorch1.12.0]  ![python3.9.12]   ![cuda11.3-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.0-py3.9.12-cuda11.3.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.12.0-py3.9.12-cuda11.3.1-devel-ubuntu20.04` |
| ![pytorch1.12.0]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.0-py3.9.12-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.12.0-py3.9.12-ubuntu20.04` |

### 1.11.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.11.0]  ![python3.9.12]   ![cuda11.3]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.11.0-py3.9.12-cuda11.3.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.11.0-py3.9.12-cuda11.3.1-ubuntu20.04` |
| ![pytorch1.11.0]  ![python3.9.12]   ![cuda11.3-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.11.0-py3.9.12-cuda11.3.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.11.0-py3.9.12-cuda11.3.1-devel-ubuntu20.04` |
| ![pytorch1.11.0]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.11.0-py3.9.12-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.11.0-py3.9.12-ubuntu20.04` |

### 1.10.2

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.10.2]  ![python3.9.12]   ![cuda11.3]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.2-py3.9.12-cuda11.3.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.10.2-py3.9.12-cuda11.3.1-ubuntu20.04` |
| ![pytorch1.10.2]  ![python3.9.12]   ![cuda11.3-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.2-py3.9.12-cuda11.3.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.10.2-py3.9.12-cuda11.3.1-devel-ubuntu20.04` |
| ![pytorch1.10.2]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.2-py3.9.12-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.10.2-py3.9.12-ubuntu20.04` |

### 1.10.1

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.10.1]  ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.1-py3.9.12-cuda11.1.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.10.1-py3.9.12-cuda11.1.1-ubuntu20.04` |
| ![pytorch1.10.1]  ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.1-py3.9.12-cuda11.1.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.10.1-py3.9.12-cuda11.1.1-devel-ubuntu20.04` |
| ![pytorch1.10.1]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.1-py3.9.12-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.10.1-py3.9.12-ubuntu20.04` |

### 1.10.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.10.0]  ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.0-py3.9.12-cuda11.1.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.10.0-py3.9.12-cuda11.1.1-ubuntu20.04` |
| ![pytorch1.10.0]  ![python3.8.16]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.0-py3.8.16-cuda11.1.1-ubuntu20.04)][DockerHub]       | `docker pull cnstark/pytorch:1.10.0-py3.8.16-cuda11.1.1-ubuntu20.04` |
| ![pytorch1.10.0]  ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.0-py3.9.12-cuda11.1.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.10.0-py3.9.12-cuda11.1.1-devel-ubuntu20.04` |
| ![pytorch1.10.0]  ![python3.8.16]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.0-py3.8.16-cuda11.1.1-devel-ubuntu20.04)][DockerHub] | `docker pull cnstark/pytorch:1.10.0-py3.8.16-cuda11.1.1-devel-ubuntu20.04` |
| ![pytorch1.10.0]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.0-py3.9.12-ubuntu20.04)][DockerHub]                  | `docker pull cnstark/pytorch:1.10.0-py3.9.12-ubuntu20.04` |

### 1.9.1

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.9.1]   ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.1-py3.9.12-cuda11.1.1-ubuntu20.04)][DockerHub]        | `docker pull cnstark/pytorch:1.9.1-py3.9.12-cuda11.1.1-ubuntu20.04` |
| ![pytorch1.9.1]   ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.1-py3.9.12-cuda11.1.1-devel-ubuntu20.04)][DockerHub]  | `docker pull cnstark/pytorch:1.9.1-py3.9.12-cuda11.1.1-devel-ubuntu20.04` |
| ![pytorch1.9.1]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.1-py3.9.12-ubuntu20.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.9.1-py3.9.12-ubuntu20.04` |

### 1.9.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.9.0]   ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.0-py3.9.12-cuda11.1.1-ubuntu20.04)][DockerHub]        | `docker pull cnstark/pytorch:1.9.0-py3.9.12-cuda11.1.1-ubuntu20.04` |
| ![pytorch1.9.0]   ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.0-py3.9.12-cuda11.1.1-devel-ubuntu20.04)][DockerHub]  | `docker pull cnstark/pytorch:1.9.0-py3.9.12-cuda11.1.1-devel-ubuntu20.04` |
| ![pytorch1.9.0]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.0-py3.9.12-ubuntu20.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.9.0-py3.9.12-ubuntu20.04` |

### 1.8.1

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.8.1]   ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.1-py3.9.12-cuda11.1.1-ubuntu20.04)][DockerHub]        | `docker pull cnstark/pytorch:1.8.1-py3.9.12-cuda11.1.1-ubuntu20.04` |
| ![pytorch1.8.1]   ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.1-py3.9.12-cuda11.1.1-devel-ubuntu20.04)][DockerHub]  | `docker pull cnstark/pytorch:1.8.1-py3.9.12-cuda11.1.1-devel-ubuntu20.04` |
| ![pytorch1.8.1]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.1-py3.9.12-ubuntu20.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.8.1-py3.9.12-ubuntu20.04` |

### 1.8.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.8.0]   ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.0-py3.9.12-cuda11.1.1-ubuntu20.04)][DockerHub]        | `docker pull cnstark/pytorch:1.8.0-py3.9.12-cuda11.1.1-ubuntu20.04` |
| ![pytorch1.8.0]   ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.0-py3.9.12-cuda11.1.1-devel-ubuntu20.04)][DockerHub]  | `docker pull cnstark/pytorch:1.8.0-py3.9.12-cuda11.1.1-devel-ubuntu20.04` |
| ![pytorch1.8.0]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.0-py3.9.12-ubuntu20.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.8.0-py3.9.12-ubuntu20.04` |


### 1.7.1

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.7.1]   ![python3.9.12]   ![cuda11.0]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.1-py3.9.12-cuda11.0.3-ubuntu18.04)][DockerHub]        | `docker pull cnstark/pytorch:1.7.1-py3.9.12-cuda11.0.3-ubuntu18.04` |
| ![pytorch1.7.1]   ![python3.9.12]   ![cuda11.0-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.1-py3.9.12-cuda11.0.3-devel-ubuntu18.04)][DockerHub]  | `docker pull cnstark/pytorch:1.7.1-py3.9.12-cuda11.0.3-devel-ubuntu18.04` |
| ![pytorch1.7.1]   ![python3.9.12]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.1-py3.9.12-ubuntu18.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.7.1-py3.9.12-ubuntu18.04` |


### 1.7.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.7.0]   ![python3.8.13]   ![cuda11.0]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.0-py3.8.13-cuda11.0.3-ubuntu18.04)][DockerHub]        | `docker pull cnstark/pytorch:1.7.0-py3.8.13-cuda11.0.3-ubuntu18.04` |
| ![pytorch1.7.0]   ![python3.8.13]   ![cuda11.0-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.0-py3.8.13-cuda11.0.3-devel-ubuntu18.04)][DockerHub]  | `docker pull cnstark/pytorch:1.7.0-py3.8.13-cuda11.0.3-devel-ubuntu18.04` |
| ![pytorch1.7.0]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.0-py3.8.13-ubuntu18.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.7.0-py3.8.13-ubuntu18.04` |


### 1.6.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.6.0]   ![python3.8.13]   ![cuda10.2]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.6.0-py3.8.13-cuda10.2-ubuntu18.04)][DockerHub]          | `docker pull cnstark/pytorch:1.6.0-py3.8.13-cuda10.2-ubuntu18.04` |
| ![pytorch1.6.0]   ![python3.8.13]   ![cuda10.2-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.6.0-py3.8.13-cuda10.2-devel-ubuntu18.04)][DockerHub]    | `docker pull cnstark/pytorch:1.6.0-py3.8.13-cuda10.2-devel-ubuntu18.04` |
| ![pytorch1.6.0]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.6.0-py3.8.13-ubuntu18.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.6.0-py3.8.13-ubuntu18.04` |


### 1.5.1

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.5.1]   ![python3.8.13]   ![cuda10.2]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.1-py3.8.13-cuda10.2-ubuntu18.04)][DockerHub]          | `docker pull cnstark/pytorch:1.5.1-py3.8.13-cuda10.2-ubuntu18.04` |
| ![pytorch1.5.1]   ![python3.8.13]   ![cuda10.2-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.1-py3.8.13-cuda10.2-devel-ubuntu18.04)][DockerHub]    | `docker pull cnstark/pytorch:1.5.1-py3.8.13-cuda10.2-devel-ubuntu18.04` |
| ![pytorch1.5.1]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.1-py3.8.13-ubuntu18.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.5.1-py3.8.13-ubuntu18.04` |


### 1.5.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.5.0]   ![python3.8.13]   ![cuda10.2]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.0-py3.8.13-cuda10.2-ubuntu18.04)][DockerHub]          | `docker pull cnstark/pytorch:1.5.0-py3.8.13-cuda10.2-ubuntu18.04` |
| ![pytorch1.5.0]   ![python3.8.13]   ![cuda10.2-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.0-py3.8.13-cuda10.2-devel-ubuntu18.04)][DockerHub]    | `docker pull cnstark/pytorch:1.5.0-py3.8.13-cuda10.2-devel-ubuntu18.04` |
| ![pytorch1.5.0]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.0-py3.8.13-ubuntu18.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.5.0-py3.8.13-ubuntu18.04` |


### 1.4.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.4.0]   ![python3.8.13]   ![cuda10.1]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.4.0-py3.8.13-cuda10.1-ubuntu18.04)][DockerHub]          | `docker pull cnstark/pytorch:1.4.0-py3.8.13-cuda10.1-ubuntu18.04` |
| ![pytorch1.4.0]   ![python3.8.13]   ![cuda10.1-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.4.0-py3.8.13-cuda10.1-devel-ubuntu18.04)][DockerHub]    | `docker pull cnstark/pytorch:1.4.0-py3.8.13-cuda10.1-devel-ubuntu18.04` |
| ![pytorch1.4.0]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.4.0-py3.8.13-ubuntu18.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.4.0-py3.8.13-ubuntu18.04` |


### 1.2.0

| Image | Pull Command | 
| -------------| -------------|
| ![pytorch1.2.0]   ![python3.7.13]   ![cuda10.0]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.2.0-py3.7.13-cuda10.0-ubuntu18.04)][DockerHub]          | `docker pull cnstark/pytorch:1.2.0-py3.7.13-cuda10.0-ubuntu18.04` |
| ![pytorch1.2.0]   ![python3.7.13]   ![cuda10.0-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.2.0-py3.7.13-cuda10.0-devel-ubuntu18.04)][DockerHub]    | `docker pull cnstark/pytorch:1.2.0-py3.7.13-cuda10.0-devel-ubuntu18.04` |
| ![pytorch1.2.0]   ![python3.7.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.2.0-py3.7.13-ubuntu18.04)][DockerHub]                   | `docker pull cnstark/pytorch:1.2.0-py3.7.13-ubuntu18.04` |

## Other Images

### Generate Build Script

Generate build script by following command (available versions see [Available Versions](#Available-Versions)):

```shell
python generate_build_script.py --os <ubuntu or centos> --os-version <e.g. 20.04, 8> --python <e.g. 3.9.12> --pytorch <e.g. 1.9.1> --cuda <e.g. 11.1, cpu>
```

```shell
usage: generate_build_script.py [-h] --os OS --os-version OS_VERSION --python PYTHON --pytorch PYTORCH [--cuda CUDA] [--cuda-flavor CUDA_FLAVOR]

Generate docker build script.

optional arguments:
  -h, --help            show this help message and exit
  --os OS               Operating system.
  --os-version OS_VERSION
                        Operating system version.
  --python PYTHON       Python version.
  --pytorch PYTORCH     Pytorch version.
  --cuda CUDA           CUDA version, `cpu` means CPU version.
  --cuda-flavor CUDA_FLAVOR
                        CUDA flavor, `runtime` or `devel`, default is None, means use base image
```

### Build Pytorch Docker Image

```
scripts/build_xxx.sh
```

### Commit the Version (Optional)

If you want to build and release specific versions using github actions, you can fork this repository and submit a pull request. The pull request should include only `scripts/build_xxx.sh` and `.github/workflows/docker_build_xxx.yml` generated by `generate_build_script.py`

## Available Versions

### OS Versions

| OS | OS version |
| - | - |
| Ubuntu | 22.04, 20.04, 18.04, 16.04, 14.04 |
| CentOS | 8, 7, 6 |

### CUDA Versions

| CUDA | CuDNN | OS(version) |
| - | - | - |
| 11.8 | 8 | Ubuntu(22.04, 20.04, 18.04), CentOS(7) |
| 11.7 | 8 | Ubuntu(22.04, 20.04, 18.04), CentOS(7) |
| 11.6 | 8 | Ubuntu(20.04, 18.04), CentOS(7) |
| 11.3 | 8 | Ubuntu(20.04, 18.04, 16.04), CentOS(8, 7) |
| 11.2 | 8 | Ubuntu(20.04, 18.04, 16.04), CentOS(8, 7) |
| 11.1 | 8 | Ubuntu(20.04, 18.04, 16.04), CentOS(8, 7) |
| 11.0 | 8 | Ubuntu(18.04, 16.04), CentOS(8, 7) |
| 10.2 | 7 | Ubuntu(18.04, 16.04), CentOS(8, 7, 6) |
| 10.1 | 7 | Ubuntu(18.04, 16.04, 14.04), CentOS(7, 6) |
| 10.0 | 7 | Ubuntu(18.04, 16.04, 14.04), CentOS(7, 6) |
| 9.2 | 7 | Ubuntu(16.04, 14.04), CentOS(7, 6) |

### Pytorch Versions

| Version | CUDA/CPU |
| - | - |
| 2.0.1 | cpu, 11.8, 11.7 |
| 2.0.0 | cpu, 11.8, 11.7 |
| 1.13.1 | cpu, 11.7, 11.6 |
| 1.13.0 | cpu, 11.7, 11.6 |
| 1.12.1 | cpu, 11.6, 11.3, 10.2 |
| 1.12.0 | cpu, 11.6, 11.3, 10.2 |
| 1.11.0 | cpu, 11.3, 10.2 |
| 1.10.2 | cpu, 11.3, 10.2 |
| 1.9.1 | cpu, 11.1, 10.2 |
| 1.9.0 | cpu, 11.1, 10.2 |
| 1.8.1 | cpu, 11,1, 10.2, 10.1 |
| 1.8.0 | cpu, 11.1, 10.2 |
| 1.7.1 | cpu, 11.0, 10.2, 10.1, 9.2 |
| 1.7.0 | cpu, 11.0, 10.2, 10.1, 9.2 |
| 1.6.0 | cpu, 10.2, 10.1, 9.2 |
| 1.5.1 | cpu, 10.2, 10.1, 9.2 |
| 1.5.0 | cpu, 10.2, 10.1, 9.2 |
| 1.4.0 | cpu, 10.1, 9.2 |
| 1.2.0 | cpu, 10.0, 9.2 |
