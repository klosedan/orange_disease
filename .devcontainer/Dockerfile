FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Install NVIDIA support
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     cuda-cudart-11-0 \
#     libcudnn8=8.0.4.30-1+cuda11.0 \
#     libcudnn8-dev=8.0.4.30-1+cuda11.0 \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install numpy pandas matplotlib seaborn torch scikit-learn jupyterlab
RUN pip install kaggle