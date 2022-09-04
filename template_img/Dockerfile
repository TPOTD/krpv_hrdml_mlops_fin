FROM ubuntu:18.04 

RUN apt-get update && apt-get install -y --no-install-recommends \
         build-essential \ 
         git \
         curl \
         ca-certificates \
         libjpeg-dev \
         libpng-dev && \
     rm -rf /var/lib/apt/lists/*

RUN curl -L -o ~/miniconda.sh -O  https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \     
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda install numpy==1.19.2 pyyaml==5.4.1 \
     flask==1.1.2 
RUN /opt/conda/bin/conda install -c pytorch faiss-cpu && \ 
     /opt/conda/bin/conda clean -ya 
ENV PATH /opt/conda/bin:$PATH
RUN pip install joblib sentence-transformers
