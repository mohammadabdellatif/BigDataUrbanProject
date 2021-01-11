#!/bin/bash

hadoop dfs -mkdir /uploads
hadoop dfs -mkdir /output

while true
do
  file=`inotifywait --format %f -e close_write /urban/uploads `
  echo "upload ${file} hadoop"
  hadoop dfs -put -f /urban/uploads/${file} /uploads/
  echo "uploaded successfully"
  hadoop jar /opt/hadoop-2.7.4/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar \
    -files /psut_scripts/water_meters_mapper.py,/psut_scripts/water_meters_reducer.py \
    -mapper water_meters_mapper.py \
    -reducer water_meters_reducer.py \
    -input /uploads/${file} -output /output/${file}
  echo "================================"
done