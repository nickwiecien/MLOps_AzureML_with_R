FROM mcr.microsoft.com/azureml/base:openmpi3.1.2-ubuntu18.04

RUN conda install -c r -y pip=20.1.1 openssl=1.1.1c r-base rpy2
RUN conda install -c conda-forge -y mscorefonts
RUN conda clean -ay
RUN pip install cryptography==3.3.1
RUN pip install --no-cache-dir azureml-defaults 

ENV TAR="bin/tar"
ENV BLANK="blank"

# Install additional R packages
RUN R -e "install.packages(c('remotes', \
        'reticulate', \
        'optparse', \
        'azuremlsdk'), repos='https://cloud.r-project.org/')"
        
