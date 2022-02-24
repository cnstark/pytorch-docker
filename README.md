# Pytorch Docker Images

[![LICENSE](https://img.shields.io/github/license/cnstark/pytorch_docker.svg)](https://github.com/cnstark/pytorch_docker/blob/master/LICENSE)
[![Docker Stars](https://img.shields.io/docker/stars/yuhaow/pytorch?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch)
[![Docker Pulls](https://img.shields.io/docker/pulls/yuhaow/pytorch?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch)

Pytorch docker images with different os, cuda, and python versions.

Docker Hub: https://hub.docker.com/repository/docker/yuhaow/pytorch

## Image List (More images are on the way ~)

| Pytorch | Python | CUDA | OS | Status | Pull command
|-|-|-|-|-|-|
| 1.10.2 | 3.9.10 | ![](https://img.shields.io/badge/CUDA-11.3-green?logo=nvidia) | ![](https://img.shields.io/badge/Ubuntu-20.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.10.2_py3.9.10_cuda11.3.1_ubuntu20.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.10.2-py3.9.10-cuda11.3.1-ubuntu20.04` |
| 1.10.2 | 3.9.10 | ![](https://img.shields.io/badge/CPU-amd64-lightgray) | ![](https://img.shields.io/badge/Ubuntu-20.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.10.2_py3.9.10_ubuntu20.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.10.2-py3.9.10-ubuntu20.04` |
| 1.10.2 | 3.8.12 | ![](https://img.shields.io/badge/CUDA-11.3-green?logo=nvidia) | ![](https://img.shields.io/badge/Ubuntu-20.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.10.2_py3.8.12_cuda11.3.1_ubuntu20.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.10.2-py3.8.12-cuda11.3.1-ubuntu20.04` |
| 1.9.1 | 3.9.7 | ![](https://img.shields.io/badge/CUDA-11.1-green?logo=nvidia) | ![](https://img.shields.io/badge/Ubuntu-20.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.9.1_py3.9.7_cuda11.1_ubuntu20.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.9.1-py3.9.7-cuda11.1-ubuntu20.04` |
| 1.9.1 | 3.9.7 | ![](https://img.shields.io/badge/CUDA-11.1-green?logo=nvidia) | ![](https://img.shields.io/badge/Ubuntu-18.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.9.1_py3.9.7_cuda11.1_ubuntu18.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.9.1-py3.9.7-cuda11.1-ubuntu18.04` |
| 1.9.1 | 3.9.7 | ![](https://img.shields.io/badge/CUDA-11.1-green?logo=nvidia) | ![](https://img.shields.io/badge/CentOS-8-blue?logo=centos) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.9.1_py3.9.7_cuda11.1_centos8)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.9.1-py3.9.7-cuda11.1-centos8` |
| 1.9.1 | 3.9.7 | ![](https://img.shields.io/badge/CPU-amd64-lightgray) | ![](https://img.shields.io/badge/Ubuntu-20.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.9.1_py3.9.7_ubuntu20.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.9.1-py3.9.7-ubuntu20.04` |
| 1.9.1 | 3.9.7 | ![](https://img.shields.io/badge/CPU-amd64-lightgray) | ![](https://img.shields.io/badge/CentOS-8-blue?logo=centos) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.9.1_py3.9.7_centos8)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.9.1-py3.9.7-centos8` |
| 1.9.1 | 3.8.12 | ![](https://img.shields.io/badge/CPU-amd64-lightgray) | ![](https://img.shields.io/badge/Ubuntu-20.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.9.1_py3.8.12_ubuntu20.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.9.1-py3.8.12-ubuntu20.04` |
| 1.7.1 | 3.7.12 | ![](https://img.shields.io/badge/CUDA-10.2-green?logo=nvidia) | ![](https://img.shields.io/badge/Ubuntu-18.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.7.1_py3.7.12_cuda10.2_ubuntu18.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.7.1-py3.7.12-cuda10.2-ubuntu18.04` |
| 1.6.0 | 3.8.12 | ![](https://img.shields.io/badge/CPU-amd64-lightgray) | ![](https://img.shields.io/badge/Ubuntu-18.04-orange?logo=ubuntu) | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cnstark/pytorch_docker/Build%20Docker%20Image%20CI%20(1.6.0_py3.8.12_ubuntu18.04)?logo=docker)](https://hub.docker.com/repository/docker/yuhaow/pytorch) | `docker pull yuhaow/pytorch:1.6.0-py3.8.12-ubuntu18.04` |

## Other Images

### Generate Build Script

Generate build script by following command (available versions see [Available Versions](#Available-Versions)):

```shell
python generate_build_script.py -os <ubuntu or centos> --os-version <e.g. 20.04, 8> --python <e.g. 3.9.10> --pytorch <e.g. 1.9.1> --cuda <e.g. 11.1, cpu>
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
| CentOS | 8, 7, 6|

### CUDA Versions

| CUDA | CuDNN | OS(version) |
| - | - | - |
| 11.3 | 8 | Ubuntu(20.04, 18.04, 16.04), CentOS(8, 7) |
| 11.2 | 8 | Ubuntu(20.04, 18.04, 16.04), CentOS(8, 7) |
| 11.1 | 8 | Ubuntu(20.04, 18.04, 16.04), CentOS(8, 7) |
| 11.0 | 8 | Ubuntu(18.04, 16.04), CentOS(8, 7) |
| 10.2 | 7 | Ubuntu(18.04, 16.04), CentOS(8, 7, 6) |
| 10.1 | 7 | Ubuntu(18.04, 16.04, 14.04), CentOS(7, 6) |
| 9.2 | 7 | Ubuntu(16.04, 14.04), CentOS(7, 6) |

### Pytorch Versions

| Version | CUDA/CPU |
| - | - |
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
