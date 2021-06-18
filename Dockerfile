# Base image
FROM ubuntu:16.04

MAINTAINER Noemi G. lois <noemigonzalezlois@gmail.com>

# Update and install library dependencies
RUN apt-get update &&\
	apt-get update -y &&\
	apt-get install build-essential -y &&\
	apt-get install git -y &&\
	apt-get install libtool m4 automake pkg-config -y &&\
	apt-get install libssl-dev libxml2-dev zlib1g-dev libboost-dev pbs-drmaa-dev gperf -y

RUN apt-get install environment-modules wget unzip default-jre -y

# Install minimal version of Anaconda
RUN wget --no-check-certificate https://repo.continuum.io/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh &&\
	bash Miniconda3-py37_4.9.2-Linux-x86_64.sh -b -p /opt/conda && \
	rm Miniconda3-py37_4.9.2-Linux-x86_64.sh
ENV PATH /opt/conda/bin:${PATH}
ENV LANG C.UTF-8

# Install package versions specified in the setup.py
WORKDIR /
COPY setup.py setup.py
RUN pip install -e .
COPY pcntoolkit/ pcntoolkit

WORKDIR /pcntoolkit
COPY tests/ tests
WORKDIR /
RUN chmod -R 777 /pcntoolkit/*
ENTRYPOINT /bin/bash 

