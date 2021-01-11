#!/bin/bash
echo 'hello world'
nohup bash -c 'bash auto-upload.sh' </dev/null >./logs.txt 2>&1 &