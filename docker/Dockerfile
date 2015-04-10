FROM ubuntu:14.04

# fix locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >> /etc/apt/sources.list
RUN cat /etc/apt/sources.list
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get -y install python-glade2 python-libtorrent avidemux avidemux-cli avidemux-qt wine1.6-i386:i386 mediainfo-gui gstreamer0.10-gnonlin gstreamer0.10-plugins-ugly python-xdg python-gst0.10

RUN apt-get -y install software-properties-common

# gstreamer0.10-ffmpeg aus PPA installieren und PPA wieder entfernen
RUN apt-add-repository -y ppa:mc3man/gstffmpeg-keep
RUN apt-get -y update
RUN apt-get -y install gstreamer0.10-ffmpeg
RUN apt-add-repository -y -r ppa:mc3man/gstffmpeg-keep

# mplayer aus PPA installieren und PPA wieder entfernen
RUN apt-add-repository -y ppa:mc3man/mplayer-test
RUN apt-get -y update
RUN apt-get -y install mplayer
RUN apt-add-repository -y -r ppa:mc3man/mplayer-test

# otrv++ laden
RUN wget -P ~/Downloads https://github.com/ReSqAr/otr-verwaltung/archive/master.zip
# und entpacken

RUN mkdir -p ~/otr
RUN unzip -uod ~/otr ~/Downloads/master.zip
RUN rm ~/Downloads/master.zip

# Link auf otrverwaltung setzen
RUN ln -sf $(eval echo ~)/otr/otr-verwaltung-master/bin/otrverwaltung /usr/local/bin/otrverwaltung

RUN apt-get -y install python2.7-dbus lxde-core lxterminal tightvncserver
#RUN apt-get -y install 

RUN mkdir -p /root/.vnc
RUN echo "abcdef\nabcdef\n\n" | vncpasswd

ADD my_conf /root/otr/otr-verwaltung-master/conf

# RUN: sudo docker run -it --rm -p 5901:5901 -e USER=root -v /home/yasin/Videos:/host otr-verwaltung bash -c "vncserver :1 -geometry 1024x768 -depth 24 && tail -F /root/.vnc/*.log"
