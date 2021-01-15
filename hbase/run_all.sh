#!/bin/bash

echo 'start hbase'
/opt/hbase-$HBASE_VERSION/bin/start-hbase.sh
echo 'create tables'

echo "create 'hbase:labels', 'f'" | hbase shell -n
echo "create 'water_meters',{NAME => 'basic'},{NAME => 'reading'},{NAME => 'location'}" | hbase shell -n
echo 'run importer in background'
/import.sh </dev/null >./import_logs.txt 2>&1 &
echo 'tail hbase logs'
#tail -f /opt/hbase-$HBASE_VERSION/logs/*
tail -f /import_logs.txt