#!/bin/bash

rm -f count.txt

for i in {1..100}
do
    echo $i | tee -a count.txt
    sleep 1
done
