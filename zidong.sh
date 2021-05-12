#!/bin/bash
cat "run.list"|
while read line
do
	apt-get build-dep $line -y --force-yes
	apt-get -b source $line -y
	echo $line  >> done.txt
done