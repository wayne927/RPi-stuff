#!/bin/bash

# This is a scheduled script to delete pasta

file=/home/pi/web/copypasta/pasta.txt

rm -f $file
touch $file

dir=/home/pi/web/PicTransfer/files
rm -rf $dir
mkdir $dir

