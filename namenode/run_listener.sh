#!/bin/bash
echo 'start service'
nohup bash -c 'bash /scripts/auto-upload.sh' </dev/null >./logs.txt 2>&1 &