FROM mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20211221.v1

RUN conda install -c r -y pip=20.1.1 openssl=1.1.1c r-base rpy2
RUN conda install -c conda-forge -y mscorefonts
RUN conda clean -ay
RUN pip install cryptography==3.3.1
RUN pip install --no-cache-dir azureml-defaults

ENV TAR="bin/tar"

# Install additional R packages
RUN R -e "install.packages('https://cran.r-project.org/src/contrib/Archive/reticulate/reticulate_1.22.tar.gz')"
RUN R -e "install.packages(c('remotes', \
        'optparse', \
        'azuremlsdk'), repos='https://cloud.r-project.org/')"
        
RUN python -m pip install azureml
RUN python -m pip install azureml.core
