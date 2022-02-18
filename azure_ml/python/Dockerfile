FROM FROM mcr.microsoft.com/azureml/base:openmpi3.1.2-ubuntu18.04

RUN conda install -c r -y pip=20.1.1 openssl=1.1.1c r-base rpy2
RUN conda install -c conda-forge -y mscorefonts
RUN conda clean -ay
RUN pip install cryptography==3.3.1
RUN pip install --no-cache-dir azureml-defaults==1.37 azureml-core==1.37

ENV TAR="bin/tar"

# Install additional R packages
RUN R -e "install.packages(c('remotes', \
        'optparse', \
        'azuremlsdk'), repos='https://cloud.r-project.org/')"
        
RUN R -e "install.packages('https://cran.r-project.org/src/contrib/Archive/reticulate/reticulate_1.22.tar.gz')"

