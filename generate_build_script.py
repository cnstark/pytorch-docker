import os
from argparse import ArgumentParser

# Schema:
# {
#    "pytorch_version": {
#       "cuda_version": [
#           "pytorch_version", "cuda_version", "torchvision_version", "cuda_version",
#           "torchaudio_version", "cuda_version", "url"
#       ],
#    }
# }
PYTORCH_VERSIONS = {
    '2.0.1': {
        'cpu': [
            '2.0.1', 'cpu', '0.15.2', 'cpu', '2.0.2', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '11.8' : [
            '2.0.1', 'cu118', '0.15.2', 'cu118', '2.0.2', 'cu118',
            'https://download.pytorch.org/whl/cu118/torch_stable.html'
        ],
        '11.7': [
            '2.0.1', 'cu117', '0.15.2', 'cu117', '2.0.2', 'cu117',
            'https://download.pytorch.org/whl/cu117/torch_stable.html'
        ],
    },
    '2.0.0': {
        'cpu': [
            '2.0.0', 'cpu', '0.15.0', 'cpu', '2.0.0', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '11.8' : [
            '2.0.0', 'cu118', '0.15.0', 'cu118', '2.0.0', 'cu118',
            'https://download.pytorch.org/whl/cu118/torch_stable.html'
        ],
        '11.7': [
            '2.0.0', 'cu117', '0.15.0', 'cu117', '2.0.0', 'cu117',
            'https://download.pytorch.org/whl/cu117/torch_stable.html'
        ],
    },
    '1.13.1': {
        'cpu': [
            '1.13.1', 'cpu', '0.14.1', 'cpu', '0.13.1', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '11.6': [
            '1.13.1', 'cu116', '0.14.1', 'cu116', '0.13.1', 'cu116',
            'https://download.pytorch.org/whl/cu116/torch_stable.html',
        ],
        '11.7': [
            '1.13.1', 'cu117', '0.14.1', 'cu117', '0.13.1', 'cu117',
            'https://download.pytorch.org/whl/cu117/torch_stable.html',
        ],
    },
    '1.13.0': {
        'cpu': [
            '1.13.0', 'cpu', '0.14.0', 'cpu', '0.13.0', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '11.6': [
            '1.13.0', 'cu116', '0.14.0', 'cu116', '0.13.0', 'cu116',
            'https://download.pytorch.org/whl/cu116/torch_stable.html',
        ],
        '11.7': [
            '1.13.0', 'cu117', '0.14.0', 'cu117', '0.13.0', 'cu117',
            'https://download.pytorch.org/whl/cu117/torch_stable.html',
        ],
    },
    '1.12.1': {
        'cpu': [
            '1.12.1', 'cpu', '0.13.1', 'cpu', '0.12.1', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '10.2': [
            '1.12.1', 'cu102', '0.13.1', 'cu102', '0.12.1', 'cu102',
            'https://download.pytorch.org/whl/cu102/torch_stable.html',
        ],
        '11.3': [
            '1.12.1', 'cu113', '0.13.1', 'cu113', '0.12.1', 'cu113',
            'https://download.pytorch.org/whl/cu113/torch_stable.html',
        ],
        '11.6': [
            '1.12.1', 'cu116', '0.13.1', 'cu116', '0.12.1', 'cu116',
            'https://download.pytorch.org/whl/cu116/torch_stable.html',
        ],
    },
    '1.12.0': {
        'cpu': [
            '1.12.0', 'cpu', '0.13.0', 'cpu', '0.12.0', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '10.2': [
            '', '', '', '', '', '',
            '',
        ],
        '11.3': [
            '1.12.0', 'cu113', '0.13.0', 'cu113', '0.12.0', 'cu113',
            'https://download.pytorch.org/whl/cu113/torch_stable.html',
        ],
        '11.6': [
            '1.12.0', 'cu116', '0.13.0', 'cu116', '0.12.0', 'cu116',
            'https://download.pytorch.org/whl/cu116/torch_stable.html',
        ],
    },
    '1.11.0': {
        'cpu': [
            '1.11.0', 'cpu', '0.12.0', 'cpu', '0.11.0', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '10.2': [
            '1.11.0', 'cu102', '0.12.0', 'cu102', '0.11.0', 'cu102',
            'https://download.pytorch.org/whl/cu102/torch_stable.html',
        ],
        '11.3': [
            '1.11.0', 'cu113', '0.12.0', 'cu113', '0.11.0', 'cu113',
            'https://download.pytorch.org/whl/cu113/torch_stable.html',
        ],
    },
    '1.10.2': {
        'cpu': [
            '1.10.2', 'cpu', '0.11.3', 'cpu', '0.10.2', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '10.2': [
            '1.10.2', 'cu102', '0.11.3', 'cu102', '0.10.2', 'cu102',
            'https://download.pytorch.org/whl/cu102/torch_stable.html',
        ],
        '11.3': [
            '1.10.2', 'cu113', '0.11.3', 'cu113', '0.10.2', 'cu113',
            'https://download.pytorch.org/whl/cu113/torch_stable.html',
        ],
    },
    '1.10.1': {
        'cpu': [
            '1.10.1', 'cpu', '0.11.2', 'cpu', '0.10.1', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '10.2': [
            '1.10.1', 'cu102', '0.11.2', 'cu102', '0.10.1', 'cu102',
            'https://download.pytorch.org/whl/cu102/torch_stable.html',
        ],
        '11.1': [
            '1.10.1', 'cu111', '0.11.2', 'cu111', '0.10.1', 'cu111',
            'https://download.pytorch.org/whl/cu111/torch_stable.html',
        ],
    },
    '1.10.0': {
        'cpu': [
            '1.10.0', 'cpu', '0.11.0', 'cpu', '0.10.0', 'cpu',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.10.0', 'cu102', '0.11.0', 'cu102', '0.10.0', 'cu102',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '11.1': [
            '1.10.0', 'cu111', '0.11.0', 'cu111', '0.10.0', 'cu111',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
    },
    '1.9.1': {
        'cpu': [
            '1.9.1', 'cpu', '0.10.1', 'cpu', '0.9.1', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.9.1', 'cu102', '0.10.1', 'cu102', '0.9.1', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '11.1': [
            '1.9.1', 'cu111', '0.10.1', 'cu111', '0.9.1', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
    },
    '1.9.0': {
        'cpu': [
            '1.9.0', 'cpu', '0.10.0', 'cpu', '0.9.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.9.0', 'cu102', '0.10.0', 'cu102', '0.9.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '11.1': [
            '1.9.0', 'cu111', '0.10.0', 'cu111', '0.9.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
    },
    '1.8.1': {
        'cpu': [
            '1.8.1', 'cpu', '0.9.1', 'cpu', '0.8.1', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.1': [
            '1.8.1', 'cu101', '0.9.1', 'cu101', '0.8.1', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.8.1', 'cu102', '0.9.1', 'cu102', '0.8.1', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '11.1': [
            '1.8.1', 'cu111', '0.9.1', 'cu111', '0.8.1', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
    },
    '1.8.0': {
        'cpu': [
            '1.8.0', 'cpu', '0.9.0', 'cpu', '0.8.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.8.0', '', '0.9.0', '', '0.8.0', '',
            '',
        ],
        '11.1': [
            '1.8.0', 'cu111', '0.9.0', 'cu111', '0.8.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
    },
    '1.7.1': {
        'cpu': [
            '1.7.1', 'cpu', '0.8.2', 'cpu', '0.7.2', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '9.2': [
            '1.7.1', 'cu92', '0.8.2', 'cu92', '0.7.2', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.1': [
            '1.7.1', 'cu101', '0.8.2', 'cu101', '0.7.2', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.7.1', '', '0.8.2', '', '0.7.2', '',
            '',
        ],
        '11.0': [
            '1.7.1', 'cu110', '0.8.2', 'cu110', '0.7.2', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
    },
    '1.7.0': {
        'cpu': [
            '1.7.0', 'cpu', '0.8.1', 'cpu', '0.7.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '9.2': [
            '1.7.0', 'cu92', '0.8.1', 'cu92', '0.7.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.1': [
            '1.7.0', 'cu101', '0.8.1', 'cu101', '0.7.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.7.0', '', '0.8.1', '', '0.7.0', '',
            '',
        ],
        '11.0': [
            '1.7.0', 'cu110', '0.8.1', 'cu110', '0.7.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
    },
    '1.6.0': {
        'cpu': [
            '1.6.0', 'cpu', '0.7.0', 'cpu', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '9.2': [
            '1.6.0', 'cu92', '0.7.0', 'cu92', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.1': [
            '1.6.0', 'cu101', '0.7.0', 'cu101', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.6.0', '', '0.7.0', '', '', '',
            '',
        ],
    },
    '1.5.1': {
        'cpu': [
            '1.5.1', 'cpu', '0.6.1', 'cpu', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '9.2': [
            '1.5.1', 'cu92', '0.6.1', 'cu92', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.1': [
            '1.5.1', 'cu101', '0.6.1', 'cu101', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.5.1', '', '0.6.1', '', '', '',
            '',
        ],
    },
    '1.5.0': {
        'cpu': [
            '1.5.0', 'cpu', '0.6.0', 'cpu', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '9.2': [
            '1.5.0', 'cu92', '0.6.0', 'cu92', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.1': [
            '1.5.0', 'cu101', '0.6.0', 'cu101', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.5.0', '', '0.6.0', '', '', '',
            '',
        ],
    },
    '1.4.0': {
        'cpu': [
            '1.4.0', 'cpu', '0.5.0', 'cpu', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '9.2': [
            '1.4.0', 'cu92', '0.5.0', 'cu92', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.1': [
            '1.4.0', '', '0.5.0', '', '', '',
            '',
        ],
    },
    '1.2.0': {
        'cpu': [
            '1.2.0', 'cpu', '0.4.0', 'cpu', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '9.2': [
            '1.2.0', 'cu92', '0.4.0', 'cu92', '', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.0': [
            '1.2.0', '', '0.4.0', '', '', '',
            '',
        ],
    },
}


OS_VERSIONS = {
    'ubuntu': ['14.04', '16.04', '18.04', '20.04', '22.04'],
    'centos': ['6', '7', '8']
}


CUDA_VERSIONS = {
    '9.2': {
        'version_name': '9.2',
        'cudnn': '7',
        'ubuntu_available': ['16.04', '18.04'],
        'centos_available': ['6', '7'],
    },
    '10.0': {
        'version_name': '10.0',
        'cudnn': '7',
        'ubuntu_available': ['14.04', '16.04', '18.04'],
        'centos_available': ['6', '7'],
    },
    '10.1': {
        'version_name': '10.1',
        'cudnn': '7',
        'ubuntu_available': ['14.04', '16.04', '18.04'],
        'centos_available': ['6', '7'],
    },
    '10.2': {
        'version_name': '10.2',
        'cudnn': '7',
        'ubuntu_available': ['16.04', '18.04'],
        'centos_available': ['6', '7', '8'],
    },
    '11.0': {
        'version_name': '11.0.3',
        'cudnn': '8',
        'ubuntu_available': ['16.04', '18.04'],
        'centos_available': ['7', '8'],
    },
    '11.1': {
        'version_name': '11.1.1',
        'cudnn': '8',
        'ubuntu_available': ['16.04', '18.04', '20.04'],
        'centos_available': ['7', '8'],
    },
    '11.2': {
        'version_name': '11.2.2',
        'cudnn': '8',
        'ubuntu_available': ['16.04', '18.04', '20.04'],
        'centos_available': ['7', '8'],
    },
    '11.3': {
        'version_name': '11.3.1',
        'cudnn': '8',
        'ubuntu_available': ['16.04', '18.04', '20.04'],
        'centos_available': ['7', '8'],
    },
    '11.6': {
        'version_name': '11.6.2',
        'cudnn': '8',
        'ubuntu_available': ['18.04', '20.04'],
        'centos_available': ['7'],
    },
    '11.7': {
        'version_name': '11.7.1',
        'cudnn': '8',
        'ubuntu_available': ['18.04', '20.04', '22.04'],
        'centos_available': ['7'],
    },
    '11.8': {
        'version_name': '11.8.0',
        'cudnn': '8',
        'ubuntu_available': ['18.04', '20.04', '22.04'],
        'centos_available': ['7'],
    },
}


BUILD_SH_TEMPLATE_UBUNTU = """#!/bin/sh

export BASE_IMAGE={base_image}

export PYTHON_VERSION={python_version}

export PYTORCH_VERSION={}
export PYTORCH_VERSION_SUFFIX={}
export TORCHVISION_VERSION={}
export TORCHVISION_VERSION_SUFFIX={}
export TORCHAUDIO_VERSION={}
export TORCHAUDIO_VERSION_SUFFIX={}
export PYTORCH_DOWNLOAD_URL={}

export IMAGE_TAG={image_tag}

./docker/ubuntu/build.sh
"""


BUILD_SH_TEMPLATE_CENTOS = """#!/bin/sh

export BASE_IMAGE={base_image}

export PYTHON_VERSION={python_version}

export PYTORCH_VERSION={}
export PYTORCH_VERSION_SUFFIX={}
export TORCHVISION_VERSION={}
export TORCHVISION_VERSION_SUFFIX={}
export TORCHAUDIO_VERSION={}
export TORCHAUDIO_VERSION_SUFFIX={}
export PYTORCH_DOWNLOAD_URL={}

export IMAGE_TAG={image_tag}

./docker/centos/build.sh
"""


BUILD_SH_TEMPLATE = {
    'ubuntu': BUILD_SH_TEMPLATE_UBUNTU,
    'centos': BUILD_SH_TEMPLATE_CENTOS,
}


GITHUB_BUILD_YML_TEMPLATE_UBUNTU = """name: Build({name})

env:
  BASE_IMAGE: "{base_image}"

  PYTHON_VERSION: "{python_version}"

  PYTORCH_VERSION: "{}"
  PYTORCH_VERSION_SUFFIX: "{}"
  TORCHVISION_VERSION: "{}"
  TORCHVISION_VERSION_SUFFIX: "{}"
  TORCHAUDIO_VERSION: "{}"
  TORCHAUDIO_VERSION_SUFFIX: "{}"
  PYTORCH_DOWNLOAD_URL: "{}"

  IMAGE_TAG: "{image_tag}"

on:
  push:
    branches:
      - main
    paths:
      - 'docker/ubuntu/**'
      - '.github/workflows/docker_build_{name}.yml'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Login DockerHub
        run: docker login --username=${{{{ secrets.DOCKER_USERNAME }}}} --password=${{{{ secrets.DOCKER_PASSWORD }}}}

      - name: Build docker image
        run: docker/ubuntu/build.sh

      - name: Push docker image
        run: docker push cnstark/pytorch:${{IMAGE_TAG}}
"""


GITHUB_BUILD_YML_TEMPLATE_CENTOS = """name: Build({name})

env:
  BASE_IMAGE: "{base_image}"

  PYTHON_VERSION: "{python_version}"

  PYTORCH_VERSION: "{}"
  PYTORCH_VERSION_SUFFIX: "{}"
  TORCHVISION_VERSION: "{}"
  TORCHVISION_VERSION_SUFFIX: "{}"
  TORCHAUDIO_VERSION: "{}"
  TORCHAUDIO_VERSION_SUFFIX: "{}"
  PYTORCH_DOWNLOAD_URL: "{}"

  IMAGE_TAG: "{image_tag}"

on:
  push:
    branches:
      - main
    paths:
      - 'docker/centos/**'
      - '.github/workflows/docker_build_{name}.yml'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Login DockerHub
        run: docker login --username=${{{{ secrets.DOCKER_USERNAME }}}} --password=${{{{ secrets.DOCKER_PASSWORD }}}}

      - name: Build docker image
        run: docker/centos/build.sh

      - name: Push docker image
        run: docker push cnstark/pytorch:${{IMAGE_TAG}}
"""


GITHUB_BUILD_YML_TEMPLATE = {
    'ubuntu': GITHUB_BUILD_YML_TEMPLATE_UBUNTU,
    'centos': GITHUB_BUILD_YML_TEMPLATE_CENTOS,
}

README_TEMPLATE = '| ![pytorch{}] ![python{}] ![{}] ![{}{}] [![](https://img.shields.io/docker/image-size/cnstark/pytorch/{})][DockerHub] | `docker pull cnstark/pytorch:{}` |'


def generate_build_args(os_name, os_version, python_version, pytorch_version, cuda_version, cuda_flavor=None):
    if os_version not in OS_VERSIONS[os_name]:
        raise ValueError(f'OS {os_name} {os_version} is not available: choose from {OS_VERSIONS[os_name]}!')

    if cuda_version == 'cpu':
        base_image = '{}:{}'.format(os_name, os_version)
        image_tag = '{}-py{}-{}{}'.format(pytorch_version, python_version, os_name, os_version)
    else:
        if os_version not in CUDA_VERSIONS[cuda_version][os_name + '_available']:
            raise ValueError(f'CUDA {cuda_version} is not available in {os_name} {os_version}!')
        if cuda_flavor is None:
            base_image = '{}:{}'.format(os_name, os_version)
            image_tag = '{}-py{}-cuda{}-{}{}'.format(
                pytorch_version, python_version, CUDA_VERSIONS[cuda_version]['version_name'],
                os_name, os_version
            )
        else:
            if cuda_flavor not in ('runtime', 'devel'):
                raise ValueError(f'CUDA flavor is not available!')

            base_image = 'nvidia/cuda:{}-cudnn{}-{}-{}{}'.format(
                CUDA_VERSIONS[cuda_version]['version_name'], CUDA_VERSIONS[cuda_version]['cudnn'],
                cuda_flavor, os_name, os_version
            )
            image_tag = '{}-py{}-cuda{}-{}-{}{}'.format(
                pytorch_version, python_version, CUDA_VERSIONS[cuda_version]['version_name'],
                cuda_flavor,os_name, os_version
            )
    kwargs = {
        'base_image': base_image,
        'python_version': python_version,
        'image_tag': image_tag
    }

    pytorch_args = PYTORCH_VERSIONS[pytorch_version][cuda_version].copy()
    for i in [1, 3, 5]:
        if pytorch_args[i] != '':
            pytorch_args[i]  = '+' + pytorch_args[i]
    return pytorch_args, kwargs


def generate_build_sh(os_name, os_version, python_version, pytorch_version, cuda_version, cuda_flavor=None, save_dir='scripts'):
    pytorch_args, kwargs = generate_build_args(os_name, os_version, python_version, pytorch_version, cuda_version, cuda_flavor)

    content = BUILD_SH_TEMPLATE[os_name].format(*pytorch_args, **kwargs)

    file_path = os.path.join(save_dir, 'build_{}.sh'.format(kwargs['image_tag'].replace('-', '_')))
    with open(file_path, 'w') as f:
        f.write(content)

    os.system('chmod +x {}'.format(file_path))


def generate_github_build_yml(os_name, os_version, python_version, pytorch_version, cuda_version, cuda_flavor=None, save_dir='.github/workflows'):
    pytorch_args, kwargs = generate_build_args(os_name, os_version, python_version, pytorch_version, cuda_version, cuda_flavor)

    kwargs['name'] = kwargs['image_tag'].replace('-', '_')
    content = GITHUB_BUILD_YML_TEMPLATE[os_name].format(*pytorch_args, **kwargs)

    file_path = os.path.join(save_dir, 'docker_build_{}.yml'.format(kwargs['image_tag'].replace('-', '_')))
    with open(file_path, 'w') as f:
        f.write(content)
    
    print('Image \'{}\' generated, please put the following content in the README.md: '.format(kwargs['image_tag']))
    print('=' * 50)
    print(README_TEMPLATE.format(
        pytorch_version, python_version,
        'cpu' if cuda_version == 'cpu' else ('cuda' + cuda_version + ('' if cuda_flavor is None else '-' + cuda_flavor)),
        os_name, os_version, kwargs['image_tag'], kwargs['image_tag']
    ))
    print('=' * 50)


def parse_args():
    parser = ArgumentParser(description='Generate docker build script.')
    parser.add_argument('--os', help='Operating system.', required=True)
    parser.add_argument('--os-version', help='Operating system version.', required=True)
    parser.add_argument('--python', help='Python version.', required=True)
    parser.add_argument('--pytorch', help='Pytorch version.', required=True)
    parser.add_argument('--cuda', help='CUDA version, `cpu` means CPU version.', default='cpu')
    parser.add_argument('--cuda-flavor', help='CUDA flavor, `runtime` or `devel`, default is None, means use base image')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    generate_build_sh(args.os, args.os_version, args.python, args.pytorch, args.cuda, args.cuda_flavor)
    generate_github_build_yml(args.os, args.os_version, args.python, args.pytorch, args.cuda, args.cuda_flavor)
