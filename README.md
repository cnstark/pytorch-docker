# Pytorch Docker Images

[DockerHub]: https://hub.docker.com/r/cnstark/pytorch

[![LICENSE](https://img.shields.io/github/license/cnstark/pytorch_docker.svg)](https://github.com/cnstark/pytorch_docker/blob/master/LICENSE)
[![Docker Stars](https://img.shields.io/docker/stars/cnstark/pytorch?logo=docker)][DockerHub]
[![Docker Pulls](https://img.shields.io/docker/pulls/cnstark/pytorch?logo=docker)][DockerHub]

Pure pytorch docker images with different os, cuda, and python versions.

Github: https://github.com/cnstark/pytorch_docker

Docker Hub: https://hub.docker.com/r/cnstark/pytorch

## Image List (More images are on the way ~)

<!-- Pytorch versions -->
[pytorch1.12.1]: https://img.shields.io/badge/Pytorch-1.12.1-orange?logo=pytorch
[pytorch1.12.0]: https://img.shields.io/badge/Pytorch-1.12.0-orange?logo=pytorch
[pytorch1.11.0]: https://img.shields.io/badge/Pytorch-1.11.0-orange?logo=pytorch
[pytorch1.10.2]: https://img.shields.io/badge/Pytorch-1.10.2-orange?logo=pytorch
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
[python3.9.12]: https://img.shields.io/badge/Python-3.9.12-blue?logo=python
[python3.8.13]: https://img.shields.io/badge/Python-3.8.13-blue?logo=python
[python3.7.13]: https://img.shields.io/badge/Python-3.7.13-blue?logo=python

<!-- OS versions -->
[ubuntu20.04]: https://img.shields.io/badge/Ubuntu-20.04-orange?logo=ubuntu
[ubuntu18.04]: https://img.shields.io/badge/Ubuntu-18.04-orange?logo=ubuntu
[centOS8]: https://img.shields.io/badge/CentOS-8-blue?logo=centos

<!-- CUDA versions -->
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

| Image | Pull Command |
|-|-|
| ![pytorch1.12.1]  ![python3.9.12]   ![cuda11.6]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.1-py3.9.12-cuda11.6.2-ubuntu20.04)][DockerHub]         | `docker pull cnstark/pytorch:1.12.1-py3.9.12-cuda11.6.2-ubuntu20.04` |
| ![pytorch1.12.1]  ![python3.9.12]   ![cuda11.6-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.1-py3.9.12-cuda11.6.2-devel-ubuntu20.04)][DockerHub]   | `docker pull cnstark/pytorch:1.12.1-py3.9.12-cuda11.6.2-devel-ubuntu20.04` |
| ![pytorch1.12.1]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.1-py3.9.12-ubuntu20.04)][DockerHub]                    | `docker pull cnstark/pytorch:1.12.1-py3.9.12-ubuntu20.04` |
| ![pytorch1.12.0]  ![python3.9.12]   ![cuda11.6]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.0-py3.9.12-cuda11.6.2-ubuntu20.04)][DockerHub]         | `docker pull cnstark/pytorch:1.12.0-py3.9.12-cuda11.6.2-ubuntu20.04` |
| ![pytorch1.12.0]  ![python3.9.12]   ![cuda11.6-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.0-py3.9.12-cuda11.6.2-devel-ubuntu20.04)][DockerHub]   | `docker pull cnstark/pytorch:1.12.0-py3.9.12-cuda11.6.2-devel-ubuntu20.04` |
| ![pytorch1.12.0]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.12.0-py3.9.12-ubuntu20.04)][DockerHub]                    | `docker pull cnstark/pytorch:1.12.0-py3.9.12-ubuntu20.04` |
| ![pytorch1.11.0]  ![python3.9.12]   ![cuda11.3]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.11.0-py3.9.12-cuda11.3.1-ubuntu20.04)][DockerHub]         | `docker pull cnstark/pytorch:1.11.0-py3.9.12-cuda11.3.1-ubuntu20.04` |
| ![pytorch1.11.0]  ![python3.9.12]   ![cuda11.3-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.11.0-py3.9.12-cuda11.3.1-devel-ubuntu20.04)][DockerHub]   | `docker pull cnstark/pytorch:1.11.0-py3.9.12-cuda11.3.1-devel-ubuntu20.04` |
| ![pytorch1.11.0]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.11.0-py3.9.12-ubuntu20.04)][DockerHub]                    | `docker pull cnstark/pytorch:1.11.0-py3.9.12-ubuntu20.04` |
| ![pytorch1.10.2]  ![python3.9.12]   ![cuda11.3]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.2-py3.9.12-cuda11.3.1-ubuntu20.04)][DockerHub]         | `docker pull cnstark/pytorch:1.10.2-py3.9.12-cuda11.3.1-ubuntu20.04` |
| ![pytorch1.10.2]  ![python3.9.12]   ![cuda11.3-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.2-py3.9.12-cuda11.3.1-devel-ubuntu20.04)][DockerHub]   | `docker pull cnstark/pytorch:1.10.2-py3.9.12-cuda11.3.1-devel-ubuntu20.04` |
| ![pytorch1.10.2]  ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.10.2-py3.9.12-ubuntu20.04)][DockerHub]                    | `docker pull cnstark/pytorch:1.10.2-py3.9.12-ubuntu20.04` |
| ![pytorch1.9.1]   ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.1-py3.9.12-cuda11.1-ubuntu20.04)][DockerHub]            | `docker pull cnstark/pytorch:1.9.1-py3.9.12-cuda11.1-ubuntu20.04` |
| ![pytorch1.9.1]   ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.1-py3.9.12-cuda11.1-devel-ubuntu20.04)][DockerHub]      | `docker pull cnstark/pytorch:1.9.1-py3.9.12-cuda11.1-devel-ubuntu20.04` |
| ![pytorch1.9.1]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.1-py3.9.12-ubuntu20.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.9.1-py3.9.12-ubuntu20.04` |
| ![pytorch1.9.0]   ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.0-py3.9.12-cuda11.1-ubuntu20.04)][DockerHub]            | `docker pull cnstark/pytorch:1.9.0-py3.9.12-cuda11.1-ubuntu20.04` |
| ![pytorch1.9.0]   ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.0-py3.9.12-cuda11.1-devel-ubuntu20.04)][DockerHub]      | `docker pull cnstark/pytorch:1.9.0-py3.9.12-cuda11.1-devel-ubuntu20.04` |
| ![pytorch1.9.0]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.9.0-py3.9.12-ubuntu20.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.9.0-py3.9.12-ubuntu20.04` |
| ![pytorch1.8.1]   ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.1-py3.9.12-cuda11.1-ubuntu20.04)][DockerHub]            | `docker pull cnstark/pytorch:1.8.1-py3.9.12-cuda11.1-ubuntu20.04` |
| ![pytorch1.8.1]   ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.1-py3.9.12-cuda11.1-devel-ubuntu20.04)][DockerHub]      | `docker pull cnstark/pytorch:1.8.1-py3.9.12-cuda11.1-devel-ubuntu20.04` |
| ![pytorch1.8.1]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.1-py3.9.12-ubuntu20.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.8.1-py3.9.12-ubuntu20.04` |
| ![pytorch1.8.0]   ![python3.9.12]   ![cuda11.1]         ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.0-py3.9.12-cuda11.1-ubuntu20.04)][DockerHub]            | `docker pull cnstark/pytorch:1.8.0-py3.9.12-cuda11.1-ubuntu20.04` |
| ![pytorch1.8.0]   ![python3.9.12]   ![cuda11.1-devel]   ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.0-py3.9.12-cuda11.1-devel-ubuntu20.04)][DockerHub]      | `docker pull cnstark/pytorch:1.8.0-py3.9.12-cuda11.1-devel-ubuntu20.04` |
| ![pytorch1.8.0]   ![python3.9.12]   ![cpu]              ![ubuntu20.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.8.0-py3.9.12-ubuntu20.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.8.0-py3.9.12-ubuntu20.04` |
| ![pytorch1.7.1]   ![python3.9.12]   ![cuda11.0]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.1-py3.9.12-cuda11.0-ubuntu18.04)][DockerHub]            | `docker pull cnstark/pytorch:1.7.1-py3.9.12-cuda11.0-ubuntu18.04` |
| ![pytorch1.7.1]   ![python3.9.12]   ![cuda11.0-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.1-py3.9.12-cuda11.0-devel-ubuntu18.04)][DockerHub]      | `docker pull cnstark/pytorch:1.7.1-py3.9.12-cuda11.0-devel-ubuntu18.04` |
| ![pytorch1.7.1]   ![python3.9.12]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.1-py3.9.12-ubuntu18.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.7.1-py3.9.12-ubuntu18.04` |
| ![pytorch1.7.0]   ![python3.8.13]   ![cuda11.0]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.0-py3.8.13-cuda11.0-ubuntu18.04)][DockerHub]            | `docker pull cnstark/pytorch:1.7.0-py3.8.13-cuda11.0-ubuntu18.04` |
| ![pytorch1.7.0]   ![python3.8.13]   ![cuda11.0-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.0-py3.8.13-cuda11.0-devel-ubuntu18.04)][DockerHub]      | `docker pull cnstark/pytorch:1.7.0-py3.8.13-cuda11.0-devel-ubuntu18.04` |
| ![pytorch1.7.0]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.7.0-py3.8.13-ubuntu18.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.7.0-py3.8.13-ubuntu18.04` |
| ![pytorch1.6.0]   ![python3.8.13]   ![cuda10.2]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.6.0-py3.8.13-cuda10.2-ubuntu18.04)][DockerHub]            | `docker pull cnstark/pytorch:1.6.0-py3.8.13-cuda10.2-ubuntu18.04` |
| ![pytorch1.6.0]   ![python3.8.13]   ![cuda10.2-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.6.0-py3.8.13-cuda10.2-devel-ubuntu18.04)][DockerHub]      | `docker pull cnstark/pytorch:1.6.0-py3.8.13-cuda10.2-devel-ubuntu18.04` |
| ![pytorch1.6.0]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.6.0-py3.8.13-ubuntu18.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.6.0-py3.8.13-ubuntu18.04` |
| ![pytorch1.5.1]   ![python3.8.13]   ![cuda10.2]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.1-py3.8.13-cuda10.2-ubuntu18.04)][DockerHub]            | `docker pull cnstark/pytorch:1.5.1-py3.8.13-cuda10.2-ubuntu18.04` |
| ![pytorch1.5.1]   ![python3.8.13]   ![cuda10.2-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.1-py3.8.13-cuda10.2-devel-ubuntu18.04)][DockerHub]      | `docker pull cnstark/pytorch:1.5.1-py3.8.13-cuda10.2-devel-ubuntu18.04` |
| ![pytorch1.5.1]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.1-py3.8.13-ubuntu18.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.5.1-py3.8.13-ubuntu18.04` |
| ![pytorch1.5.0]   ![python3.8.13]   ![cuda10.2]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.0-py3.8.13-cuda10.2-ubuntu18.04)][DockerHub]            | `docker pull cnstark/pytorch:1.5.0-py3.8.13-cuda10.2-ubuntu18.04` |
| ![pytorch1.5.0]   ![python3.8.13]   ![cuda10.2-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.0-py3.8.13-cuda10.2-devel-ubuntu18.04)][DockerHub]      | `docker pull cnstark/pytorch:1.5.0-py3.8.13-cuda10.2-devel-ubuntu18.04` |
| ![pytorch1.5.0]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.5.0-py3.8.13-ubuntu18.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.5.0-py3.8.13-ubuntu18.04` |
| ![pytorch1.4.0]   ![python3.8.13]   ![cuda10.1]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.4.0-py3.8.13-cuda10.1-ubuntu18.04)][DockerHub]            | `docker pull cnstark/pytorch:1.4.0-py3.8.13-cuda10.1-ubuntu18.04` |
| ![pytorch1.4.0]   ![python3.8.13]   ![cuda10.1-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.4.0-py3.8.13-cuda10.1-devel-ubuntu18.04)][DockerHub]      | `docker pull cnstark/pytorch:1.4.0-py3.8.13-cuda10.1-devel-ubuntu18.04` |
| ![pytorch1.4.0]   ![python3.8.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.4.0-py3.8.13-ubuntu18.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.4.0-py3.8.13-ubuntu18.04` |
| ![pytorch1.2.0]   ![python3.7.13]   ![cuda10.0]         ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.2.0-py3.7.13-cuda10.0-ubuntu18.04)][DockerHub]            | `docker pull cnstark/pytorch:1.2.0-py3.7.13-cuda10.0-ubuntu18.04` |
| ![pytorch1.2.0]   ![python3.7.13]   ![cuda10.0-devel]   ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.2.0-py3.7.13-cuda10.0-devel-ubuntu18.04)][DockerHub]      | `docker pull cnstark/pytorch:1.2.0-py3.7.13-cuda10.0-devel-ubuntu18.04` |
| ![pytorch1.2.0]   ![python3.7.13]   ![cpu]              ![ubuntu18.04]    [![](https://img.shields.io/docker/image-size/cnstark/pytorch/1.2.0-py3.7.13-ubuntu18.04)][DockerHub]                     | `docker pull cnstark/pytorch:1.2.0-py3.7.13-ubuntu18.04` |

## Other Images

### Generate Build Script

Generate build script by following command (available versions see [Available Versions](#Available-Versions)):

```shell
python generate_build_script.py -os <ubuntu or centos> --os-version <e.g. 20.04, 8> --python <e.g. 3.9.12> --pytorch <e.g. 1.9.1> --cuda <e.g. 11.1, cpu>
```

```shell
usage: generate_build_script.py [-h] --os OS --os-version OS_VERSION --python PYTHON --pytorch PYTORCH [--cuda CUDA]

Generate docker build script.

optional arguments:
  -h, --help            show this help message and exit
  --os OS               Operating system.
  --os-version OS_VERSION
                        Operating system version.
  --python PYTHON       Python version.
  --pytorch PYTORCH     Pytorch version.
  --cuda CUDA           CUDA version, `cpu` means CPU version.
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
| Ubuntu | 20.04, 18.04, 16.04, 14.04 |
| CentOS | 8, 7, 6 |

### CUDA Versions

| CUDA | CuDNN | OS(version) |
| - | - | - |
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
