ARG UBUNTU_VERSION
ARG CUDA_VERSION
ARG CUDNN_VERSION
ARG PYTHON_VERSION
ARG PYTORCH_VERSION
ARG PYTORCH_CUDA_VERSION
ARG TORCHVISION_VERSION
ARG TORCHAUDIO_VERSION

FROM nvidia/cuda:${CUDA_VERSION}-cudnn${CUDNN_VERSION}-runtime-ubuntu${UBUNTU_VERSION}

RUN apt update && \
    apt install -y wget build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev liblzma-dev

WORKDIR /temp

RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -xvf Python-${PYTHON_VERSION}.tgz

RUN cd Python-${PYTHON_VERSION} && \
    ./configure --enable-optimizations && \
    make && \
    make install

WORKDIR /workspace

RUN rm -r /temp && \
    ln -s /usr/local/bin/python3 /usr/local/bin/python && \
    ln -s /usr/local/bin/pip3 /usr/local/bin/pip

RUN pip install torch==${PYTORCH_VERSION}+${PYTORCH_CUDA_VERSION} torchvision==${TORCHVISION_VERSION}+${PYTORCH_CUDA_VERSION} torchaudio==${TORCHAUDIO_VERSION} -f https://download.pytorch.org/whl/torch_stable.html && \
    rm -r /root/.cache/pip
