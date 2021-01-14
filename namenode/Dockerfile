FROM bde2020/hadoop-namenode:2.0.0-hadoop2.7.4-java8

RUN apt-get update; exit 0
RUN apt-get install python -y --force-yes
RUN apt-get install inotify-tools -y
RUN mkdir /uploads
RUN chmod 777 /uploads
COPY namenode/run_all.sh run_all.sh
RUN chmod a+x /run_all.sh

CMD /run_all.sh