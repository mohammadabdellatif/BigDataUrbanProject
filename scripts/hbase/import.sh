#!/bin/bash

while true
do
  #wait for a new csv file to be uploaded to this folder
  file=`inotifywait --format %f -e close_write /hbase_trigger `
  echo "import ${file} to hbase"
  hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.skip.bad.lines=false -Dimporttsv.separator="," -Dimporttsv.columns="HBASE_ROW_KEY,location:HOUSE_NO,location:STREET_NO,basic:ACCOUNT_NO,reading:FOLIO,basic:STATUS,location:GPS,location:Latitude,location:Longitude" water_meters hdfs://namenode:9000/output/${file}
  rm /hbase_trigger/${file}
  echo "================================"
done