#!/bin/bash
sleep 10
hadoop dfs -mkdir /uploads
hadoop dfs -mkdir /output

while true
do
  #wait for a new csv file to be uploaded to this folder
  file=`inotifywait --format %f -e close_write /uploads `
  cm=$(($(date +%s%N)/1000000))
  echo "upload ${file} hadoop"
  hadoop dfs -put -f /uploads/${file} /uploads/
  echo "uploaded successfully"
  hadoop jar /opt/hadoop-2.7.4/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar \
    -files /scripts/hadoop/water_meters_mapper.py,/scripts/hadoop/water_meters_reducer.py \
    -mapper water_meters_mapper.py \
    -reducer water_meters_reducer.py \
    -input /uploads/${file} -output /output/${file}-$cm
  touch /hbase_trigger/${file}-$cm
  echo "================================"
done