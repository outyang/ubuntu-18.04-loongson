#!/bin/bash
cat "run3000.list"|
while read line
do
	mkdir $line && cd $line \
	&& apt-get build-dep $line -y --force-yes \
	&& apt-get -b source $line -y \
	&& cd .. \
	&& echo $line  >> done.txt
done
