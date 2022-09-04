#!/bin/sh

wget -O 1.html https://freeproxyupdate.com/
cat 1.html | python obr.py > res.txt