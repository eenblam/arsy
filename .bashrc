#!/bin/bash
# .bashrc

for f in ~/.arsy/*.on
do
	if [ -f  $f ]; then
		. $f
	fi
done
