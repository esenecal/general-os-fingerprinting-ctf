FROM ubuntu:24.04
WORKDIR /

RUN apt update
RUN apt upgrade -y

RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install build-essential libpcap-dev -y
RUN apt install python3-dev -y
RUN pip3 install pypacker --break-system-packages
RUN pip3 install pcapyplus --break-system-packages
RUN pip3 install untangle --break-system-packages
RUN pip3 install requests --break-system-packages
RUN pip3 install netifaces --break-system-packages

COPY pof-ctf /pof-ctf
COPY satori-master /satori-master

# apt update
# apt upgrade -y
# apt install python3 -y
# (gographic location)
# 2
# 2 (anchorage)


# apt install python3 -y
# apt install python3-pip -y
# apt install build-essential libpcap-dev -y
# apt install python3-dev -y
# pip3 install pypacker --break-system-packages
# pip3 install pcapyplus --break-system-packages
# pip3 install untangle --break-system-packages
# pip3 install requests --break-system-packages
# pip3 install netifaces --break-system-packages