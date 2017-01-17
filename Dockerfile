MAINTAINER leocborgess@gmail.com
FROM ubuntu:14.04

RUN apt-get update 
RUN apt-get install -y build-essential autoconf \
    libogg-dev libvorbis-dev pkg-config zlib1g-dev \
    libboost-all-dev libcurl4-openssl-dev rake 

COPY ./ ./mkvtoolnix

WORKDIR /mkvtoolnix/dependencias/libebml-1.2.2/libebml-1.2.2/make/linux

RUN make install_headers install_staticlib

WORKDIR /mkvtoolnix/dependencias/libmatroska-1.3.0/libmatroska-1.3.0/make/linux

RUN make install_headers install_staticlib

WORKDIR /mkvtoolnix

RUN ./autogen.sh

RUN ./configure --with-boost-libdir=/usr/lib/x86_64-linux-gnu

RUN mkdir /mkvtemp

RUN rake; exit 0

RUN rake install; exit 0 

RUN locale-gen en_US.UTF-8

ENV LANGUAGE="en_US.UTF-8"
RUN echo 'LANGUAGE="en_US.UTF-8"' >> /etc/default/locale
ENV LC_ALL="en_US.UTF-8"
RUN echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale

WORKDIR /mkvtemp

#RUN apt-get install -y python-software-properties software-properties-common

#RUN add-apt-repository ppa:fkrull/deadsnakes

#RUN apt-get update

#RUN apt-get install -y python3.5

#RUN apt-get install -y curl

#RUN curl -O https://bootstrap.pypa.io/get-pip.py

#RUN python3.5 get-pip.py

#RUN pip install --upgrade setuptools
#RUN pip install pyunpack
#RUN pip install patool
