FROM bde2020/hbase-standalone:1.0.0-hbase1.2.6

RUN apt-get update
RUN apt-get install inotify-tools -y
RUN mkdir /uploads
COPY scripts/hbase/import.sh /import.sh
COPY hbase/run_all.sh /run_all.sh
RUN chmod a+x /import.sh
RUN chmod a+x /run_all.sh
CMD /run_all.sh