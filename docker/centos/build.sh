docker build \
    --build-arg CENTOS_VERSION=${CENTOS_VERSION} \
    --build-arg PYTHON_VERSION=${PYTHON_VERSION} \
    --build-arg PYTORCH_VERSION=${PYTORCH_VERSION} \
    --build-arg TORCHVISION_VERSION=${TORCHVISION_VERSION} \
    --build-arg TORCHAUDIO_VERSION=${TORCHAUDIO_VERSION} \
    -t yuhaow/pytorch:${PYTORCH_VERSION}-py${PYTHON_VERSION}-centos${CENTOS_VERSION} \
    -f docker/centos/Dockerfile \
    .
