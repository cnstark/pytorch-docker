import os
from argparse import ArgumentParser


PYTORCH_VERSIONS = {
    '1.10.2': {
        'cpu': [
            '1.10.2', 'cpu', '0.11.3', 'cpu', '0.10.2', 'cpu',
            'https://download.pytorch.org/whl/cpu/torch_stable.html',
        ],
        '10.2': [
            '', '', '', '', '', '',
            '',
        ],
        '11.3': [
            '1.10.2', 'cu113', '0.11.3', 'cu113', '0.10.2', 'cu113',
            'https://download.pytorch.org/whl/cu113/torch_stable.html',
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
            '1.7.0', 'cpu', '0.8.0', 'cpu', '0.7.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '9.2': [
            '1.7.0', 'cu92', '0.8.0', 'cu92', '0.7.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.1': [
            '1.7.0', 'cu101', '0.8.0', 'cu101', '0.7.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
        '10.2': [
            '1.7.0', '', '0.8.0', '', '0.7.0', '',
            '',
        ],
        '11.0': [
            '1.7.0', 'cu110', '0.8.0', 'cu110', '0.7.0', '',
            'https://download.pytorch.org/whl/torch_stable.html',
        ],
    },
}


OS_VERSIONS = {
    'ubuntu': ['14.04', '16.04', '18.04', '20.04'],
    'centos': ['6', '7', '8']
}


CUDA_VERSIONS = {
    '9.2': {
        'version_name': '9.2',
        'cudnn': '7',
        'ubuntu_available': ['16.04', '18.04'],
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
        'version_name': '11.0',
        'cudnn': '8',
        'ubuntu_available': ['16.04', '18.04'],
        'centos_available': ['7', '8'],
    },
    '11.1': {
        'version_name': '11.1',
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
}


BUILD_SH_TEMPLATE_UBUNTU = """#!/bin/sh

export UBUNTU_VERSION={os_version}

export PYTHON_VERSION={python_version}

export PYTORCH_VERSION={}
export PYTORCH_VERSION_SUFFIX={}
export TORCHVISION_VERSION={}
export TORCHVISION_VERSION_SUFFIX={}
export TORCHAUDIO_VERSION={}
export TORCHAUDIO_VERSION_SUFFIX={}
export PYTORCH_DOWNLOAD_URL={}

./docker/ubuntu/build.sh
"""


BUILD_SH_TEMPLATE_UBUNTU_CUDA = """#!/bin/sh

export UBUNTU_VERSION={os_version}
export CUDA_VERSION={cuda_version}
export CUDNN_VERSION={cudnn_version}

export PYTHON_VERSION={python_version}

export PYTORCH_VERSION={}
export PYTORCH_VERSION_SUFFIX={}
export TORCHVISION_VERSION={}
export TORCHVISION_VERSION_SUFFIX={}
export TORCHAUDIO_VERSION={}
export TORCHAUDIO_VERSION_SUFFIX={}
export PYTORCH_DOWNLOAD_URL={}

./docker/ubuntu-cuda/build.sh
"""


BUILD_SH_TEMPLATE_CENTOS = """#!/bin/sh

export CENTOS_VERSION={os_version}

export PYTHON_VERSION={python_version}

export PYTORCH_VERSION={}
export PYTORCH_VERSION_SUFFIX={}
export TORCHVISION_VERSION={}
export TORCHVISION_VERSION_SUFFIX={}
export TORCHAUDIO_VERSION={}
export TORCHAUDIO_VERSION_SUFFIX={}
export PYTORCH_DOWNLOAD_URL={}

./docker/centos/build.sh
"""


BUILD_SH_TEMPLATE_CENTOS_CUDA = """#!/bin/sh

export CENTOS_VERSION={os_version}
export CUDA_VERSION={cuda_version}
export CUDNN_VERSION={cudnn_version}

export PYTHON_VERSION={python_version}

export PYTORCH_VERSION={}
export PYTORCH_VERSION_SUFFIX={}
export TORCHVISION_VERSION={}
export TORCHVISION_VERSION_SUFFIX={}
export TORCHAUDIO_VERSION={}
export TORCHAUDIO_VERSION_SUFFIX={}
export PYTORCH_DOWNLOAD_URL={}

./docker/centos-cuda/build.sh
"""


BUILD_SH_TEMPLATE = {
    'ubuntu': {
        'cpu': BUILD_SH_TEMPLATE_UBUNTU,
        'cuda': BUILD_SH_TEMPLATE_UBUNTU_CUDA,
    },
    'centos': {
        'cpu': BUILD_SH_TEMPLATE_CENTOS,
        'cuda': BUILD_SH_TEMPLATE_CENTOS_CUDA,
    },
}


GITHUB_BUILD_YML_TEMPLATE_UBUNTU = """name: Build Docker Image CI ({name})

env:
  UBUNTU_VERSION: "{os_version}"

  PYTHON_VERSION: "{python_version}"

  PYTORCH_VERSION: "{}"
  PYTORCH_VERSION_SUFFIX: "{}"
  TORCHVISION_VERSION: "{}"
  TORCHVISION_VERSION_SUFFIX: "{}"
  TORCHAUDIO_VERSION: "{}"
  TORCHAUDIO_VERSION_SUFFIX: "{}"
  PYTORCH_DOWNLOAD_URL: "{}"

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
        run: docker push yuhaow/pytorch:${{PYTORCH_VERSION}}-py${{PYTHON_VERSION}}-ubuntu${{UBUNTU_VERSION}}
"""


GITHUB_BUILD_YML_TEMPLATE_UBUNTU_CUDA = """name: Build Docker Image CI ({name})

env:
  UBUNTU_VERSION: "{os_version}"
  CUDA_VERSION: "{cuda_version}"
  CUDNN_VERSION: "{cudnn_version}"

  PYTHON_VERSION: "{python_version}"

  PYTORCH_VERSION: "{}"
  PYTORCH_VERSION_SUFFIX: "{}"
  TORCHVISION_VERSION: "{}"
  TORCHVISION_VERSION_SUFFIX: "{}"
  TORCHAUDIO_VERSION: "{}"
  TORCHAUDIO_VERSION_SUFFIX: "{}"
  PYTORCH_DOWNLOAD_URL: "{}"

on:
  push:
    branches:
      - main
    paths:
      - 'docker/ubuntu-cuda/**'
      - '.github/workflows/docker_build_{name}.yml'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Login DockerHub
        run: docker login --username=${{{{ secrets.DOCKER_USERNAME }}}} --password=${{{{ secrets.DOCKER_PASSWORD }}}}

      - name: Build docker image
        run: docker/ubuntu-cuda/build.sh

      - name: Push docker image
        run: docker push yuhaow/pytorch:${{PYTORCH_VERSION}}-py${{PYTHON_VERSION}}-cuda${{CUDA_VERSION}}-ubuntu${{UBUNTU_VERSION}}
"""


GITHUB_BUILD_YML_TEMPLATE_CENTOS = """name: Build Docker Image CI ({name})

env:
  CENTOS_VERSION: "{os_version}"

  PYTHON_VERSION: "{python_version}"

  PYTORCH_VERSION: "{}"
  PYTORCH_VERSION_SUFFIX: "{}"
  TORCHVISION_VERSION: "{}"
  TORCHVISION_VERSION_SUFFIX: "{}"
  TORCHAUDIO_VERSION: "{}"
  TORCHAUDIO_VERSION_SUFFIX: "{}"
  PYTORCH_DOWNLOAD_URL: "{}"

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
        run: docker push yuhaow/pytorch:${{PYTORCH_VERSION}}-py${{PYTHON_VERSION}}-centos${{CENTOS_VERSION}}
"""


GITHUB_BUILD_YML_TEMPLATE_CENTOS_CUDA = """name: Build Docker Image CI ({name})

env:
  CENTOS_VERSION: "{os_version}"
  CUDA_VERSION: "{cuda_version}"
  CUDNN_VERSION: "{cudnn_version}"

  PYTHON_VERSION: "{python_version}"

  PYTORCH_VERSION: "{}"
  PYTORCH_VERSION_SUFFIX: "{}"
  TORCHVISION_VERSION: "{}"
  TORCHVISION_VERSION_SUFFIX: "{}"
  TORCHAUDIO_VERSION: "{}"
  TORCHAUDIO_VERSION_SUFFIX: "{}"
  PYTORCH_DOWNLOAD_URL: "{}"

on:
  push:
    branches:
      - main
    paths:
      - 'docker/centos-cuda/**'
      - '.github/workflows/docker_build_{name}.yml'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Login DockerHub
        run: docker login --username=${{{{ secrets.DOCKER_USERNAME }}}} --password=${{{{ secrets.DOCKER_PASSWORD }}}}

      - name: Build docker image
        run: docker/centos-cuda/build.sh

      - name: Push docker image
        run: docker push yuhaow/pytorch:${{PYTORCH_VERSION}}-py${{PYTHON_VERSION}}-cuda${{CUDA_VERSION}}-centos${{CENTOS_VERSION}}
"""


GITHUB_BUILD_YML_TEMPLATE = {
    'ubuntu': {
        'cpu': GITHUB_BUILD_YML_TEMPLATE_UBUNTU,
        'cuda': GITHUB_BUILD_YML_TEMPLATE_UBUNTU_CUDA,
    },
    'centos': {
        'cpu': GITHUB_BUILD_YML_TEMPLATE_CENTOS,
        'cuda': GITHUB_BUILD_YML_TEMPLATE_CENTOS_CUDA,
    },
}


def generate_build_sh(os_name, os_version, python_version, pytorch_version, cuda_version, save_dir='scripts'):
    if os_version not in OS_VERSIONS[os_name]:
        raise ValueError(f'OS {os_name} {os_version} is not available')
    template = BUILD_SH_TEMPLATE[os_name]['cpu' if cuda_version == 'cpu' else 'cuda']

    kwargs = {
        'os_version': os_version,
        'python_version': python_version
    }
    if cuda_version == 'cpu':
        img_name = '{}_py{}_{}{}'.format(pytorch_version, python_version, os_name, os_version)
    else:
        if os_version not in CUDA_VERSIONS[cuda_version][os_name + '_available']:
            raise ValueError(f'CUDA {cuda_version} is not available in {os_name} {os_version}!')
        kwargs['cuda_version'] = CUDA_VERSIONS[cuda_version]['version_name']
        kwargs['cudnn_version'] = CUDA_VERSIONS[cuda_version]['cudnn']

        img_name = '{}_py{}_cuda{}_{}{}'.format(
            pytorch_version, python_version, CUDA_VERSIONS[cuda_version]['version_name'], os_name, os_version
        )

    pytorch_args = PYTORCH_VERSIONS[pytorch_version][cuda_version].copy()
    for i in [1, 3, 5]:
        if pytorch_args[i] != '':
            pytorch_args[i]  = '+' + pytorch_args[i]

    content = template.format(*pytorch_args, **kwargs)

    file_path = os.path.join(save_dir, 'build_{}.sh'.format(img_name))
    with open(file_path, 'w') as f:
        f.write(content)

    os.system('chmod +x {}'.format(file_path))


def generate_github_build_yml(os_name, os_version, python_version, pytorch_version, cuda_version, save_dir='.github/workflows'):
    if os_version not in OS_VERSIONS[os_name]:
        raise ValueError(f'OS {os_name} {os_version} is not available')
    template = GITHUB_BUILD_YML_TEMPLATE[os_name]['cpu' if cuda_version == 'cpu' else 'cuda']

    kwargs = {
        'os_version': os_version,
        'python_version': python_version
    }
    if cuda_version == 'cpu':
        img_name = '{}_py{}_{}{}'.format(pytorch_version, python_version, os_name, os_version)
        kwargs['name'] = img_name
    else:
        if os_version not in CUDA_VERSIONS[cuda_version][os_name + '_available']:
            raise ValueError(f'CUDA {cuda_version} is not available in {os_name} {os_version}!')
        kwargs['cuda_version'] = CUDA_VERSIONS[cuda_version]['version_name']
        kwargs['cudnn_version'] = CUDA_VERSIONS[cuda_version]['cudnn']

        img_name = '{}_py{}_cuda{}_{}{}'.format(
            pytorch_version, python_version, CUDA_VERSIONS[cuda_version]['version_name'], os_name, os_version
        )
        kwargs['name'] = img_name

    pytorch_args = PYTORCH_VERSIONS[pytorch_version][cuda_version].copy()
    for i in [1, 3, 5]:
        if pytorch_args[i] != '':
            pytorch_args[i]  = '+' + pytorch_args[i]

    content = template.format(*pytorch_args, **kwargs)

    file_path = os.path.join(save_dir, 'docker_build_{}.yml'.format(img_name))
    with open(file_path, 'w') as f:
        f.write(content)


def parse_args():
    parser = ArgumentParser(description='Generate docker build script.')
    parser.add_argument('--os', help='Operating system.', required=True)
    parser.add_argument('--os-version', help='Operating system version.', required=True)
    parser.add_argument('--python', help='Python version.', required=True)
    parser.add_argument('--pytorch', help='Pytorch version.', required=True)
    parser.add_argument('--cuda', help='CUDA version, `cpu` means CPU version.', default='cpu')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    generate_build_sh(args.os, args.os_version, args.python, args.pytorch, args.cuda)
    generate_github_build_yml(args.os, args.os_version, args.python, args.pytorch, args.cuda)
