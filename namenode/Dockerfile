FROM bde2020/hadoop-namenode:2.0.0-hadoop2.7.4-java8
RUN apt-get install inotify-tools -y
COPY --from=python:3 / /
#RUN apt-get update && apt-get upgrade
#RUN apt install -y --force-yes build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
#RUN wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tar.xz
#RUN tar -xf Python-3.8.0.tar.xz
#WORKDIR Python-3.8.0
#RUN ./configure --enable-optimizations
#RUN make
#RUN make altinstall
#WORKDIR /
#RUN apt-get install -y python3-pip
RUN pip3 install requests
RUN mkdir /uploads
RUN chmod 777 /uploads
COPY namenode/run_all.sh run_all.sh
RUN chmod a+x /run_all.sh

CMD /run_all.sh