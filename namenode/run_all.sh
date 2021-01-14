#!/bin/bash

/scripts/hadoop/auto-upload.sh </dev/null >./upload_logs.txt 2>&1 &
/run.sh