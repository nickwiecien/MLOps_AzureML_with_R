FROM rocker/r-ver:3.6.3-ubuntu18.04
 
# Install python
RUN apt-get update -qq && \
 apt-get install -y python3
 
# Create link for python
RUN ln -f /usr/bin/python3 /usr/bin/python

RUN conda install -c r -y pip=20.1.1 openssl=1.1.1c r-base rpy2
RUN conda install -c conda-force -y mscorefonts
RUN conda clean -ay
RUN pip install --no-cache-dir azureml-defaults

ENV TAR="bin/tar"

# Install additional R packages
RUN R -e "install.packages(c('remotes', \
        'reticulate', \
        'optparse', \
        'azuremlsdk'), repos='https://cloud.r-project.org/')"
        