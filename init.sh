#!/usr/bin/env bash
mkdir png
mkdir bmp

wget https://flagcdn.com/w2560.zip -P png
unzip png/w2560.zip -d png

chmod +x c.py
chmod +x zip.pl
chmod +x m.py

./c.py
./zip.pl
./m.py > result.txt
