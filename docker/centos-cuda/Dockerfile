ARG CENTOS_VERSION
ARG CUDA_VERSION
ARG CUDNN_VERSION

FROM nvidia/cuda:${CUDA_VERSION}-cudnn${CUDNN_VERSION}-runtime-centos${CENTOS_VERSION}

ARG PYTHON_VERSION
ARG PYTORCH_VERSION
ARG PYTORCH_CUDA_VERSION
ARG TORCHVISION_VERSION
ARG TORCHAUDIO_VERSION

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* && \
    yum install -y wget gcc make openssl-devel tk-devel xz-devel zlib-devel bzip2-devel ncurses-devel gdbm-devel \
        readline-devel sqlite-devel libffi-devel

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

RUN pip install torch==${PYTORCH_VERSION}${PYTORCH_CUDA_VERSION} torchvision==${TORCHVISION_VERSION}${PYTORCH_CUDA_VERSION} torchaudio==${TORCHAUDIO_VERSION} -f https://download.pytorch.org/whl/torch_stable.html && \
    rm -r /root/.cache/pip
