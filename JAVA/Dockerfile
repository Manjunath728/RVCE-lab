FROM ubuntu:latest
ARG CACHEBURST=1
RUN apt-get -y update
ADD pc.tar.gz .
ENV TZ=England/London
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install tzdata
RUN apt-get install -y  nautilus 
